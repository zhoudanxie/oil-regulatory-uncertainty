# %%
import pandas as pd
import os
import re
import time
import spacy
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

# %%
# Get directory
directory=os.path.dirname(os.path.realpath(__file__))

# %%
# Import parsed articles
df=pd.read_pickle(f'{directory}/../data/nlp_demo/parsed_xml.pkl')
# print(df.info())
print(df['Type'].value_counts())

# %%
# Keep only "News" articles
df=df[df['Type']=='News'].reset_index(drop=True)
# print(df.info())

# %%
# Convert dates
df['StartDate']=df['StartDate'].astype('datetime64[ns]')
df['Year']=df['StartDate'].astype('datetime64[ns]').dt.year
df['Month']=df['StartDate'].astype('datetime64[ns]').dt.month

# %%
print("# of publication titles:",df['PubTitle'].nunique())

# %%
# Check start and end dates for each pub title
for title in df.sort_values('PubTitle')['PubTitle'].unique():
    print(title,
         min(df[df['PubTitle']==title].sort_values('StartDate')['StartDate'].dt.date),
         max(df[df['PubTitle']==title].sort_values('StartDate')['StartDate'].dt.date),
         len(df[df['PubTitle']==title]))

# %%
# Sort
df=df.sort_values(['PubTitle','StartDate','Title']).reset_index(drop=True)

# %%
# Identify and Remove Duplicated Articles
# Full text for certain articles is not available due to copyright restrictions
print("Number of full texts:",df[df['Text']!=""]['ID'].nunique())
print("Number of empty full texts:",df[df['Text']==""]['ID'].nunique())

# %%
# Define a text preprocessor (lemmatizer)
def my_preprocessor(text):
    doc=nlp(text.lower())
    lemmas=[token.lemma_ for token in doc if not token.is_punct | token.is_space]
    text_out=" ".join(lemmas)
    return text_out

# %%
# Convert ID and text to list
text_list=df['Text'].tolist()

# %%
# Preprocess all text
start_time = time.time()
text_lemmatized=[]
for text in text_list:
    text_out=my_preprocessor(text)
    text_lemmatized.append(text_out)
print("--- %s seconds ---" % (time.time() - start_time))

# %%
# Add processed data to dataframe
df['TextLemmatized']=text_lemmatized

# %%
# Remove unavailable full text and sort
df=df[df['TextLemmatized']!=""].sort_values(['TextLemmatized','StartDate']).reset_index(drop=True)
print("Total number of articles:",len(df))

# %%
# Check duplicates by pub title and lemmatized text
df['GroupNo']=df.groupby(['PubTitle','TextLemmatized']).cumcount()+1
print("Number of duplicated articles:",df[df['GroupNo']>1]['ID'].nunique())

# %%
# Remove duplicates and keep the earliest article
df_nodup=df.groupby(['PubTitle','TextLemmatized']).nth(0).reset_index(drop=True)

# %%
df_nodup['GroupNo']=df_nodup.groupby(['PubTitle','TextLemmatized']).cumcount()+1
print("Number of duplicated articles:", df_nodup[df_nodup['GroupNo']>1]['ID'].nunique())
print("Number of unavailable articles:",df_nodup[df_nodup['TextLemmatized']==""]['ID'].nunique())
print("Number of articles in the clean dataset:", len(df_nodup))

# %%
# Export clean data
df_nodup.drop(['GroupNo'],axis=1).to_pickle(f'{directory}/../data/nlp_demo/parsed_xml_clean.pkl')

