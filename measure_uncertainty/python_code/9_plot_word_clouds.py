# %%
import pandas as pd
import os
import numpy as np
import calendar

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image

import matplotlib
matplotlib.use('TkAgg')

# %%
# Get directory
directory=os.path.dirname(os.path.realpath(__file__))

# %%
# Import fonts
from matplotlib import font_manager
times = font_manager.FontProperties(fname=f'{directory}/../data/supplementary_data/palatinolinotype_roman.ttf')

font_path=f'{directory}/../data/supplementary_data/coolvetica_rg.otf'

# Word cloud mask
mask = np.array(Image.open(f'{directory}/../data/supplementary_data/wordcloud_mask.png'))

# %%
# Create output folder if not existing
output_path=f'{directory}/../output'
if not os.path.exists(output_path):
        os.makedirs(output_path)
else:
        pass

# %% [markdown]
# ## 1. Import data
# Top noun chunks from all articles were pre-saved in the /data folder.

# %% [markdown]
# ## 2. Wordcloud
# ### 2.1 Oil Regulatory Uncertainty
# #### 2.1.1 Noun Chunks Word Cloud (Figure 2)

# %%
# Import saved noun chunks
df=pd.read_csv(f'{directory}/../data/noun_chunks_by_month_reg.csv')

# %%
# Function to create word cloud for a specific year-month
def creat_wordcloud(year, month):

    # Refine data
    temp = df[(df['Year'] == year) & (df['Month'] == month)]
    # Convert saved noun chunks to dictionary
    all_nc_counts = dict(zip(temp['NounChunk'], temp['Count']))

    # Create a WordCloud object
    wordcloud = WordCloud(background_color="white", max_words=50, random_state=42,
                         width=500, height=300, font_path=font_path, mask=mask)
    # Generate a word cloud
    wordcloud.fit_words(all_nc_counts)

    return wordcloud

# %%
# Specify years & months
# Year-months used in the paper
yearmonth=[(1991,1),(1995,10),(2001,9),(2004,9),(2009,5),(2016,7)]

# %%
# Plot word clouds
fig, axes = plt.subplots(2, 3, figsize=(25,15), sharex=False, sharey=False)

for i, ax in enumerate(axes.flatten()):
    year=yearmonth[i][0]
    month=yearmonth[i][1]
    ax.imshow(creat_wordcloud(year,month), interpolation="bilinear")
    title=calendar.month_name[month]+' '+str(year)
    ax.set_title(title,fontproperties=times,fontsize=32,fontweight='bold')
    ax.axis('off')

plt.tight_layout()
plt.savefig(f'{directory}/../output/figure2.jpg', bbox_inches='tight')
plt.close()
print(f'Figure 2 saved in /measure_uncertainty/output.')

# %% [markdown]
# ### 2.2 General Oil & Gas Uncertainty
# #### 2.2.1 Noun Chunks Word Cloud (Figure 4)

# %%
# Import saved noun chunks
df=pd.read_csv(f'{directory}/../data/noun_chunks_by_month_general.csv')

# %%
# # Customize stop phrases
# stop_phrases=['united_states','new_york','et_al','natural_gas','crude_oil']

# %%
# Function to create word cloud
def creat_wordcloud2(year, month):

    # Refine data
    temp = df[(df['Year'] == year) & (df['Month'] == month)]
    # Convert saved noun chunks to dictionary
    all_nc_counts = dict(zip(temp['NounChunk'], temp['Count']))

    # Create a WordCloud object
    wordcloud = WordCloud(background_color="white", max_words=50, random_state=42,
                         width=500, height=300, font_path=font_path, mask=mask)
    # Generate a word cloud
    wordcloud.fit_words(all_nc_counts)

    return wordcloud

# %%
# Specify years & months
# Year-months used in the paper
yearmonth=[(1989,4),(1990,8),(2003,3),(2005,9),(2010,5),(2020,4)]

# %%
# Plot word clouds
fig, axes = plt.subplots(2, 3, figsize=(25,15), sharex=False, sharey=False)

for i, ax in enumerate(axes.flatten()):
    year=yearmonth[i][0]
    month=yearmonth[i][1]
    ax.imshow(creat_wordcloud2(year,month), interpolation="bilinear")
    title=calendar.month_name[month]+' '+str(year)
    ax.set_title(title,fontproperties=times,fontsize=32,fontweight='bold')
    ax.axis('off')

plt.tight_layout()
plt.savefig(f'{directory}/../output/figure4.jpg', bbox_inches='tight')
plt.close()
print(f'Figure 4 saved in /measure_uncertainty/output.')