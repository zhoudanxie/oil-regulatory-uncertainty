# %%
import pandas as pd
import os
import re
import gc
import time
from transformers import pipeline

import spacy
from spacy.lang.en import English
nlp = English()  # just the language with no model
sentencizer = nlp.create_pipe("sentencizer")
nlp.add_pipe("sentencizer")

# %%
# Get directory
directory=os.path.dirname(os.path.realpath(__file__))

# %%
# Import all articles
df=pd.read_pickle(f'{directory}/../data/nlp_demo/parsed_xml_clean.pkl')
# print(df.info())

# %%
# Refine to articles with both KeyWordMatch1 and KeyWordMatch2
df_match=df[(df['KeyWordCount1']>0) & (df['KeyWordCount2']>0)].reset_index(drop=True)
# print(df_match.info())

# %%
# Free memory
del df
gc.collect()

# %%
# Check date range
print("Date range:",min(df_match['StartDate']), max(df_match['StartDate']))

# %%
# Function to remove multiple spaces
def remove_spaces(text):
    text=re.sub(' +',' ',text).strip()
    text=text.replace('\n',' ').replace('\r',' ')
    return text

# %% [markdown]
# ## Extract regulatory sections with zero-shot classification

# %%
# Zero-shot model
pipe = pipeline("zero-shot-classification",model="facebook/bart-large-mnli")

# %%
# Set labels
labels = ["government regulation", "not government regulation"]

# %%
# Function to determine if a sentence is related to regulation using zero-shot classification
def use_zero_shot(sentence, labels):
    result = pipe(sentence, labels,
                  # hypothesis_template="This text is about {}.",
                  multi_label=True)
    result_dict = dict(zip(result["labels"], result["scores"]))

    if result_dict[labels[0]] > result_dict[labels[1]]:
        return True
    else:
        # print(result_dict[labels[0]], result_dict[labels[1]])
        return False


# %%
# Function to identify the sentence with "*regulat*" and a sentence before and after (expanded regulatory sentences)
def extractSentenceZeroShot(text):
    regsent_set = set()
    regsent_index = []
    econsent_set = set()
    reg_section = econ_section = ''

    text = remove_spaces(text)
    doc = nlp(text)
    sentList = list(doc.sents)

    # Identify regulory sections
    # Iterate through all sentences
    for i in range(0, len(sentList)):
        sent = sentList[i].text.strip()
        if (len(re.findall('regulat', sent, re.IGNORECASE)) > 0) & (len(sent.split()) > 5):
            # Add the sentence before if the reg sent is not the first sent
            sent = sentList[i - 1].text.strip() + ' ' + sent if i > 0 else sent
            # Add the sentence after if the reg sent is not the last sent
            sent = sent + ' ' + sentList[i + 1].text.strip() if i < len(sentList) - 1 else sent

            # Determine reg relevance using zero-shot classification
            if use_zero_shot(sent, labels):
                # Add sentence by sentence to set in case same sentences appear in multiple reg sections
                # Add the sentence before if the reg sent is not the first sent
                if i > 0:
                    regsent_set.add(sentList[i - 1].text.strip())
                # Add the reg sent
                regsent_set.add(sentList[i].text.strip())
                # Add the sentence after if the reg sent is not the last sent
                if i < len(sentList) - 1:
                    regsent_set.add(sentList[i + 1].text.strip())

                # Save reg sent index
                regsent_index.append(i)
            else:
                pass
        else:
            pass

    # Join all reg sections in an article
    reg_section = ' '.join(regsent_set)

    # Identify economic sections (excluding regulatory sentences)
    if len(regsent_index) > 0:

        econ_words_match = re.compile(r'\b(economic|economy)\b', re.IGNORECASE)

        # Iterate through all sentences other than reg sentences
        for i in [i for i in range(0, len(sentList)) if i not in regsent_index]:
            sent = sentList[i].text.strip()
            if (len(econ_words_match.findall(sent)) > 0) & (len(sent.split()) > 5):
                # Add sentence by sentence to set in case same sentences appear in multiple reg sections
                # Add the sentence before if the econ sent is not the first sent
                if i > 0:
                    econsent_set.add(sentList[i - 1].text.strip())
                # Add the econ sent
                econsent_set.add(sentList[i].text.strip())
                # Add the sentence after if the econ sent is not the last sent
                if i < len(sentList) - 1:
                    econsent_set.add(sentList[i + 1].text.strip())
            else:
                pass

        # Join all econ sections in an article
        econ_section = ' '.join(econsent_set)
    else:
        pass

    return reg_section, econ_section

# %%
# Extract regulatory sections from all articles
texts=df_match['Text'].tolist()
reg_sections=[]
econ_sections=[]
for text in texts:
    result=extractSentenceZeroShot(text)
    reg_sections.append(result[0])
    econ_sections.append(result[1])

# %%
# Add results to dataframe
df_match['RegSection']=reg_sections
df_match['EconSection']=econ_sections

# %%
# Free memory
del reg_sections
del texts
gc.collect()

# %%
print('# of articles with "*regulat*" in full text:',df_match[df_match['RegSection']!=""]['ID'].nunique())
print('# of articles with no "*regulat*" in full text:',
      df_match[(df_match['RegSection']=="") | (df_match['RegSection']==" ")]['ID'].nunique())

# %%
print('# of articles with econ sections:',df_match[df_match['EconSection']!=""]['ID'].nunique())
print('# of articles with no econ sections',
      df_match[(df_match['EconSection']=="") | (df_match['EconSection']==" ")]['ID'].nunique())

# %%
# Sort dataframe
df_match=df_match.sort_values(['PubTitle','StartDate','Title']).reset_index(drop=True)

# %%
# Save data
df_match.to_pickle(f'{directory}/../data/nlp_demo/parsed_xml_clean.pkl')



