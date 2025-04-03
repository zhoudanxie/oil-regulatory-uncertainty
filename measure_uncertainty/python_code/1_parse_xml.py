# %%
import xml.etree.cElementTree as et
import pandas as pd
import os
import re
import pickle
import time

# %%
# Get directory
directory=os.path.dirname(os.path.realpath(__file__))

# %%
# Function to remove html tags from a string
def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# Function to remove multiple spaces
def remove_spaces(text):
    text=re.sub(' +',' ',text).strip()
    return text

# %%
# All files
filePath=f'{directory}/../data/nlp_demo/xml_examples'
files=[]
for file in os.listdir(filePath):
    files.append(file)
print('Number of XML files:',len(files))

# %%
# Function to parse XML
def import_xml(filename):
    ID=filename.split('.xml')[0]
    xmlp = et.XMLParser(encoding="UTF-8")
    parsed_xml = et.parse(f'{filePath}/{filename}',parser=xmlp)
    root = parsed_xml.getroot()
    
    try:
        for child in root.findall('Obj'):
            for grandchild in child.findall('Language'):
                if grandchild.find('RawLang')!=None:
                    lang=grandchild.find('RawLang').text
        if lang=='English':
            for child in root.findall('Obj'):
                type=child.find('ObjectTypes').find('mstar').text
                title=child.find('TitleAtt').find('Title').text
                try:
                    startdate=child.find('StartDate').text
                    enddate=child.find('EndDate').text
                except:
                    startdate=child.find('NumericDate').text
                    enddate=child.find('NumericDate').text
                
                try:
                    section=child.find('PrintLocation').find('DocSection').text
                except:
                    section=""
                       
                try:                
                    subjects=[]
                    for grandchild in child.find('Terms').findall('GenSubjTerm'):
                        new=grandchild.find('GenSubjValue').text
                        subjects.append(new)
                except:
                    subjects=[]

            if root.find('TextInfo')!=None:
                for node in root.iter('Text'):
                    text=node.text
                    text=remove_spaces(remove_html_tags(text))
                    wordcount=node.get('WordCount')
            else:
                text=''
                wordcount=0

            for child in root.findall('DFS'):
                pubtitle=child.find('PubFrosting').find('Title').text
                sourcetype=child.find('PubFrosting').find('SourceType').text

            return ID,title,type,startdate,enddate,text,wordcount,pubtitle,sourcetype,section,subjects
        
        else:
            print(filename, ": non-English article")
    
    except:
        print('Could not parse:',filename)

# %%
# Parse all XMLs
processed_lists=[import_xml(file) for file in files]

# %%
# # Using multiprocessing if a large number of files
# # Multiprocessing Module
# import multiprocessing as mp
# from multiprocessing import Pool
# # Check core count
# print(mp.cpu_count())
#
# start_time = time.time()
# with Pool(8) as p:
#     processed_lists=p.map(import_xml, files)
# print("--- %s seconds ---" % (time.time() - start_time))

# %%
# Transform processed data into a dataframe
df = pd.DataFrame(processed_lists, columns=['ID','Title','Type','StartDate','EndDate','Text',
            'TextWordCount','PubTitle', 'SourceType','Section','Subjects'])
# print(df.info())

# %%
# Save dataframe
df.to_pickle(f'{directory}/../data/nlp_demo/parsed_xml.pkl')


