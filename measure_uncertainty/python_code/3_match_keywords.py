# %%
import pandas as pd
import os
import re

import spacy
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

# %%
# Get directory
directory=os.path.dirname(os.path.realpath(__file__))

# %%
# Define a text preprocessor (lemmatizer)
def my_preprocessor(text):
    doc=nlp(text.lower())
    lemmas=[token.lemma_ for token in doc if not token.is_punct | token.is_space]
    text_out=" ".join(lemmas)
    return text_out

# %%
# Import lemmatized articles
df=pd.read_pickle(f'{directory}/../data/nlp_demo/parsed_xml_clean.pkl')
# print(df.info())

# %% [markdown]
# ## 1. Match Keywords

# %% [markdown]
# ### 3.1 Match Group 1 keywords

# %%
# List of texts
texts_list=df['TextLemmatized'].tolist()
print('Number of articles:',len(texts_list))

# %%
# List of subject keywords (Group 1)
keywords=['Crude Oil', 'Natural Gas', 'Petroleum', 'Fossil Fuel', 
        'Energy Sector', 'Energy Market', 'Energy Industry', 'Energy Company']

# %%
# Lemmatize keywords
keywords=[my_preprocessor(w) for w in keywords]
print('Number of Group 1 keywords:',len(keywords))

# %%
# Compile a re pattern with all keywords
pattern=re.compile(r"\b"+r"\b|\b".join(map(re.escape, keywords))+r"\b")

# %%
# Match keywords in all articles
match_words=[]
match_count=[]
for text in texts_list:    
    match_new=[]
    count_new=0
    find_new=pattern.findall(text)
    if len(find_new)>0:
        match_new=find_new
        count_new=len(find_new)
    match_words.append(match_new)
    match_count.append(count_new)

# %%
df['KeyWordMatch1']=match_words
df['KeyWordCount1']=match_count

# %%
print('Articles that do not contain any Group 1 keywords:',\
     df[df['KeyWordCount1']==0]['ID'].nunique())
print('Articles that contain Group 1 keywords:',\
     df[df['KeyWordCount1']>0]['ID'].nunique())

# %% [markdown]
# ### 3.2 Match Group 2 keywords

# %%
# List of subject keywords (Group 2)
df_keywords_new=pd.read_excel(f'{directory}/../data/supplementary_data/eia_energy_glossary.xlsx')
# print(df_keywords_new.info())

# %%
keywords_new=df_keywords_new['Term'].tolist()
print('Number of Group 2 keywords:',len(keywords_new))

# %%
# Lemmatize keywords
keywords_new=[my_preprocessor(w) for w in keywords_new]

# %%
# Compile a new re pattern with all noun chunks
pattern_new=re.compile(r"\b"+r"\b|\b".join(map(re.escape, keywords_new))+r"\b")

# %%
# Match noun chunks in all articles
match_words_new=[]
match_count_new=[]
for text in texts_list:  
    match_new=[]
    count_new=0
    find_new=pattern_new.findall(text)
    if len(find_new)>0:
        match_new=find_new
        count_new=len(find_new)
    match_words_new.append(match_new)
    match_count_new.append(count_new)

# %%
df['KeyWordMatch2']=match_words_new
df['KeyWordCount2']=match_count_new

# %%
print('Articles that do not contain any Group 2 keywords:',\
     df[df['KeyWordCount2']==0]['ID'].nunique())
print('Articles that contain Group 2 keywords:',\
     df[df['KeyWordCount2']>0]['ID'].nunique())
print('Articles that contain both Group 1&2 keywords:',\
     df[(df['KeyWordCount1']>0) & (df['KeyWordCount2']>0)]['ID'].nunique())

# %%
# Export data
df.to_pickle(f'{directory}/../data/nlp_demo/parsed_xml_clean.pkl')


