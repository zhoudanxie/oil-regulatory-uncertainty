# %%
import pandas as pd
import os
import datetime
import statsmodels.formula.api as sm

import spacy
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

# %%
# Get directory
directory=os.path.dirname(os.path.realpath(__file__))

# %% [markdown]
# ## Functions to process data

# %%
# Function to merge with newspaper names (one newspaper name can correspond to multiple publication titles)
def merge_newspapers(df):
    newspapers = pd.read_csv(f'{directory}/../data/supplementary_data/pub_title_newspaper.csv')

    df = df.merge(newspapers[['PubTitle', 'Newspaper']], on='PubTitle', how='left')

    # Change data format
    df['Newspaper'] = df['Newspaper'].astype('category')

    return df

# %%
# Function to refine dataset to index start date through end date
def specify_timeframe(df):
    start_date = datetime.datetime(1985, 1, 1)
    end_date = datetime.datetime(2021, 12, 31)

    df['StartDate'] = df['StartDate'].astype('datetime64[ns]')
    df = df[(df['StartDate'] >= start_date) & (df['StartDate'] <= end_date)].sort_values('StartDate').reset_index(
        drop=True)

    # Year and month
    df['Year'] = df['StartDate'].dt.year
    df['Month'] = df['StartDate'].dt.month

    return df

# %% [markdown]
# ## Import datasets

# %%
# Import saved uncertainty scores
df=pd.read_csv(f'{directory}/../data/all_uncertainty_scores_baseline.csv')
print(df.info())

# Process data
df=merge_newspapers(df)
df=specify_timeframe(df)

#-----------------------------------------------------------------------------------------------------------------------
#---------------------------------------Baseline oil regulatory uncertainty index---------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

print('This code will reproduce the oil regulatory uncertainty index '
      '(pre-saved in /data/oil_regulatory_uncertainty_index_baseline.csv).\n'
      'Note: This may take a few minutes.')

# %%
# Refine to articles with regulatory sections
df_reg=df[df['RegUncertaintyScore'].notnull()].reset_index(drop=True)

# %% [markdown]
# ## Construct monthly regulatory uncertainty index

# %%
# Function to create a DF with all unique years and months
def create_ym(df):
    df_ym=df[['Year','Month']].drop_duplicates().reset_index(drop=True).reset_index()
    df_ym['YM']=df_ym['index']+1
    df_ym=df_ym.drop('index',axis=1)

    df=df.merge(df_ym[['Year','Month','YM']],on=['Year','Month'],how='left').sort_values(['Year','Month']).reset_index(drop=True)

    return df,df_ym

# %% [markdown]
# ### Baseline index

# %%
# Function to estimate index (suppressing constant)
def estimate_index(df,var_name,category='Newspaper'):
    # Identify unique years and months
    df_data,df_ym=create_ym(df)

    # Estimate
    FE_OLS=sm.ols(formula=f'{var_name} ~ 0+C(YM)+C({category})',
        data=df_data).fit()

    FE_estimates=pd.DataFrame()
    FE_estimates[var_name+'Index']=FE_OLS.params[0:max(df_ym['YM'])]
    FE_estimates=FE_estimates.reset_index().rename(columns={'index':'FE'})
    FE_estimates['YM']=FE_estimates['FE'].str.split("[",expand=True)[1].str.split("]",expand=True)[0].astype('int64')

    # Clean data
    FE_estimates=df_ym.merge(FE_estimates, on='YM', how='left').drop('FE', axis=1)

    return FE_estimates

# %%
# Estimate uncertainty index
RegUncertaintyIndex=estimate_index(df_reg,'RegUncertaintyScore')

# Rename columns
RegUncertaintyIndex.rename(columns={'RegUncertaintyScoreIndex':'RegUncertaintyIndex'},
                           inplace=True)
print(RegUncertaintyIndex.head())

# %%
# Save estimated index
RegUncertaintyIndex[['Year','Month','YM','RegUncertaintyIndex']].\
    to_csv(f'{directory}/../data/oil_regulatory_uncertainty_index_baseline.csv',index=False)

#-----------------------------------------------------------------------------------------------------------------------
#---------------------------------------Alternative oil regulatory uncertainty index------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

print('This code will reproduce the oil regulatory uncertainty index '
      '(pre-saved in /data/oil_regulatory_uncertainty_index_robust.csv).\n'
      'Note: This may take a few minutes.')

# %% [markdown]
# ### Controlling for econ uncertainty

# %%
# Function to estimate index (controlling for econ uncertainty)
def estimate_index_econ(df,var_name,category='Newspaper'):
    # Identify unique years and months
    df_data, df_ym = create_ym(df)

    # Estimate
    FE_OLS=sm.ols(formula= f'{var_name} ~ 0+C(YM)+C({category})+EconUncertaintyScore',
        data=df_data).fit()

    FE_estimates=pd.DataFrame()
    FE_estimates[var_name+'Index_Econ']=FE_OLS.params[0:max(df_ym['YM'])]
    FE_estimates=FE_estimates.reset_index().rename(columns={'index':'FE'})
    FE_estimates['YM']=FE_estimates['FE'].str.split("[",expand=True)[1].str.split("]",expand=True)[0].astype('int64')

    # Clean data
    FE_estimates=df_ym.merge(FE_estimates, on='YM', how='left').drop('FE', axis=1)

    return FE_estimates

# %%
# Estimate uncertainty index
RegUncertaintyIndex_Econ=estimate_index_econ(df_reg,'RegUncertaintyScore')

# Rename columns
RegUncertaintyIndex_Econ.rename(columns={'RegUncertaintyScoreIndex_Econ':'RegUncertaintyIndex_Econ'},
                           inplace=True)


# %% [markdown]
# ### Using news articles based on a broader set of energy terms
# Import saved uncertainty scores
df_broad=pd.read_csv(f'{directory}/../data/all_uncertainty_scores_broadterm.csv')

# Process data
df_broad=merge_newspapers(df_broad)
df_broad=specify_timeframe(df_broad)

# Estimate uncertainty index
RegUncertaintyIndex_BroadTerm=estimate_index(df_broad,'RegUncertaintyScore')

# Rename columns
RegUncertaintyIndex_BroadTerm.rename(columns={'RegUncertaintyScoreIndex':'RegUncertaintyIndex_Broad'},
                           inplace=True)

# %% [markdown]
# ### Using trade journal & magazine articles
# Import saved uncertainty scores
df_journal=pd.read_csv(f'{directory}/../data/all_uncertainty_scores_journal.csv')

# Process data
df_journal=specify_timeframe(df_journal)

# Estimate uncertainty index
RegUncertaintyIndex_Journal=estimate_index(df_journal,'RegUncertaintyScore',category='PubTitle')

# Rename columns
RegUncertaintyIndex_Journal.rename(columns={'RegUncertaintyScoreIndex':'RegUncertaintyIndex_Journal'},
                           inplace=True)

# %% [markdown]
# ### Merge alternative indexes
RegUncertaintyIndex_Robust=RegUncertaintyIndex_Econ.\
    merge(RegUncertaintyIndex_BroadTerm.drop(['YM'],axis=1),on=['Year','Month'],how='left').\
    merge(RegUncertaintyIndex_Journal.drop(['YM'],axis=1),on=['Year','Month'],how='left')

print(RegUncertaintyIndex_Robust.head())

# Save estimated index
RegUncertaintyIndex[['Year','Month','YM','RegUncertaintyIndex_Econ','RegUncertaintyIndex_Broad','RegUncertaintyIndex_Journal']].\
        to_csv(f'{directory}/../data/oil_regulatory_uncertainty_index_robust.csv',index=False)


#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------General oil supply uncertainty index------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

print('This code will reproduce the general oil supply uncertainty index '
      '(pre-saved in /data/oil_supply_uncertainty_index.csv).\n'
      'Note: This may take a few minutes.')

# %% [markdown]
# ## Construct uncertainty index
# Estimate uncertainty index
UncertaintyIndex = estimate_index(df,'UncertaintyScore')

# Rename columns
UncertaintyIndex.rename(columns={'UncertaintyScoreIndex': 'UncertaintyIndex'}, inplace=True)

# %%
# Save estimated index
UncertaintyIndex.to_csv(f'{directory}/../data/oil_supply_uncertainty_index.csv')

