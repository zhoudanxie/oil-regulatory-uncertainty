import pandas as pd
import os
import gc
from collections import Counter

import spacy
nlp = spacy.load('en_core_web_sm')

# %%
# Get directory
directory=os.path.dirname(os.path.realpath(__file__))

#%%
print("This code extracts top noun chunks from demo text data only. "
      "Top noun chunks from all articles were pre-saved in the /data folder.")

# %%
# Import all data
df_all=pd.read_pickle(f'{directory}/../data/nlp_demo/parsed_xml_clean.pkl')

# Oil and gas related articles
df=df_all[(df_all['KeyWordCount1']>0) & (df_all['KeyWordCount2']>0)].reset_index(drop=True)

# Free memory
del df_all
gc.collect()

# %%
# Customize stop phrases
stop_phrases=['federal_regulator','state_regulator','natural_gas']

# Function to identify noun chunks
def get_nounchunks(text_list):
    all_nc=[]
    for text in text_list:
        doc=nlp(text)
        for nc in doc.noun_chunks:
            doc_nc=nlp(str(nc).lower())
            lemmas=[token.lemma_ for token in doc_nc if not token.is_punct | token.is_space | token.is_stop]   # Lemmatize noun chunks
            if (len(lemmas)>=2) & (len(lemmas)<=3):      # Keep only bigrams and trigrams
                noun_out="_".join(lemmas)
                if noun_out not in stop_phrases:
                    all_nc.append(noun_out)
    return all_nc

#%% Extract noun chunks and counts from regulatory sections
# Refine data to the year & month
year=2011
month=11
temp=df[(df['Year']==year) & (df['Month']==month) & (df['RegUncertaintyCount']>0)].reset_index(drop=True)

# Generate noun chunk frequencies
all_nc_counts=Counter(get_nounchunks(temp['RegSection']))
print(all_nc_counts)
