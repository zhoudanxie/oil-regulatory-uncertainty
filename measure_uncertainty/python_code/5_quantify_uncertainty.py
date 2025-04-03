# %%
import pandas as pd
import os
import re
import gc
import spacy
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

# %%
# Get directory
directory=os.path.dirname(os.path.realpath(__file__))

# %% [markdown]
# Import data

# %%
# All articles
df=pd.read_pickle(f'{directory}/../data/nlp_demo/parsed_xml_clean.pkl')
# print(df.info())

# %%
# Define relevant articles
df_match=df[(df['KeyWordCount1']>0) & (df['KeyWordCount2']>0)].reset_index(drop=True)
print('Number of articles related to oil & gas production:',len(df_match))

# %%
# Free memory
del df
gc.collect()

# %% [markdown]
# ### LM uncertainty

# %%
# LM dictionary
LMlist=pd.read_csv(f'{directory}/../data/supplementary_data/lm_sentiment.csv')

# %%
# LM uncertainty dictionary
LMuncertain=LMlist[LMlist['Uncertainty'].notnull()]['Uncertainty']
print('Number of uncertainty words in LM dictionary:',len(LMuncertain))

# %%
# Define a text preprocessor (lemmatizer)
# It has to be the same preprocessor used for preprocessing news articles
def my_preprocessor(text):
    doc=nlp(text.lower())
    lemmas=[token.lemma_ for token in doc if not token.is_punct | token.is_space]
    text_out=" ".join(lemmas)
    return text_out

# %%
# Lemmatize keywords
uncertainlist_lemmatized=list(set([my_preprocessor(w) for w in LMuncertain]))    #Convert to set to remove duplicates

# %%
# Compile a new re pattern with all keywords
pattern=re.compile(r"\b"+r"\b|\b".join(map(re.escape, uncertainlist_lemmatized))+r"\b")

# %%
# Function to count uncertainty terms
def uncertainty_count(text):
    match_new=[]
    count_new=0
    find=pattern.findall(text)
    if len(find)>0:
        match_new=find
        count_new=len(find)

    return count_new, match_new

# %%
# Count uncertainty words in full text
text_list=df_match['TextLemmatized'].tolist()
results=[]
for text in text_list:
    results.append(uncertainty_count(text))

# Add processed data to dataframe
df_match[['UncertaintyCount','UncertaintyWords']] = pd.DataFrame(results)
print('Number of articles with uncertainty words:',df_match[df_match['UncertaintyCount']!=0]['ID'].nunique())

# %%
# Count uncertainty words in regulatory sections
text_list=df_match['RegSection'].tolist()
results=[]
for text in text_list:
    results.append(uncertainty_count(text))

# Add processed data to dataframe
df_match[['RegUncertaintyCount','RegUncertaintyWords']] = pd.DataFrame(results)
print('Number of regulatory sections with uncertainty words:',df_match[df_match['RegUncertaintyCount']!=0]['ID'].nunique())

# %%
# Count uncertainty words in economic sections
text_list=df_match['EconSection'].tolist()
results=[]
for text in text_list:
    results.append(uncertainty_count(text))

# Add processed data to dataframe
df_match[['EconUncertaintyCount','EconUncertaintyWords']] = pd.DataFrame(results)
print('Number of economic sections with uncertainty words:',df_match[df_match['EconUncertaintyCount']!=0]['ID'].nunique())

# %% [markdown]
# ## Calculate uncertainty scores

# %%
# Define a word counter
def word_counter(text):
    doc=nlp(text.lower())
    tokens=[token for token in doc if not token.is_punct | token.is_space]
    count=len(tokens)
    return count

# %%
# Total word count
lemmatized_texts = df_match['TextLemmatized'].tolist()
df_match['TotalWordCount']= [word_counter(text) for text in lemmatized_texts]

# print(df['UncertaintyCount'].describe())
# print(df['TotalWordCount'].describe())

# %%
# Calculate scores
df_match['UncertaintyScore'] = df_match['UncertaintyCount'] / df_match['TotalWordCount'] * 100
print(df_match['UncertaintyScore'].describe())

# %%
# Regulatory uncertainty scores
# Reg section word count
texts=df_match[df_match['RegSection']!='']['RegSection'].tolist()
reg_counts=[word_counter(text) for text in texts]
df_match.loc[df_match['RegSection']!='','RegSectionWordCount']=reg_counts

# %%
# Calculate scores
df_match['RegUncertaintyScore']=df_match['RegUncertaintyCount']/df_match['RegSectionWordCount']*100
print(df_match['RegUncertaintyScore'].describe())
print("Articles with positive reg uncertainty scores:",len(df_match[df_match['RegUncertaintyScore']>0]))

# %% [markdown]
# ### Economic uncertainty scores

# %%
# Econ section word count
texts=df_match['EconSection'].tolist()
df_match['EconSectionWordCount']=[word_counter(text) for text in texts]

# %%
# Calculate scores
df_match['EconUncertaintyScore']=df_match['EconUncertaintyCount']/df_match['EconSectionWordCount']*100
# Set EconUncertaintyScore=0 if there is no econ section
df_match.loc[df_match['EconSection']=='', 'EconUncertaintyScore']=0

print(df_match['EconUncertaintyScore'].describe())
print("Articles with positive econ uncertainty scores:",len(df_match[df_match['EconUncertaintyScore']>0]))

# %%
# Save data
df_match.to_pickle(f'{directory}/../data/nlp_demo/parsed_xml_clean.pkl')




