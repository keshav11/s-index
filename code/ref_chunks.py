
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os


# In[2]:

PICKLE_PATH = 'dblp.pickle'
try:
    dblp_df = pd.read_pickle(PICKLE_PATH)
except:
    dblp_df0 = pd.read_json('../input/dblp-ref-0.json', lines=True)
    dblp_df1 = pd.read_json('../input/dblp-ref-1.json', lines=True)
    dblp_df2 = pd.read_json('../input/dblp-ref-2.json', lines=True)
    dblp_df3 = pd.read_json('../input/dblp-ref-3.json', lines=True)
    dblp_df = pd.concat([dblp_df0, dblp_df1, dblp_df2, dblp_df3])
    dblp_df.to_pickle(PICKLE_PATH)





# In[4]:


dblp_df = dblp_df.dropna(subset=['authors'])
dblp_df['references'].fillna('[]', inplace=True)
dblp_df['abstract'].fillna('', inplace=True)

keep_cols = ['references', 'id']
cols = ['id']
papers = dblp_df[keep_cols].set_index(cols)

chunk_sz = 300000
papers_chunks = [papers[i : i + chunk_sz] for i in range(0, papers.shape[0], chunk_sz)]

for chunk in enumerate(papers_chunks):
    chunk_flattened_ref_df = chunk[1].references.apply(pd.Series).stack().reset_index(level=1, drop=True).to_frame('references').reset_index()
    chunk_flattened_ref_df.to_pickle('flattened_chunks_ref/references'+ str(chunk[0]) + '.pickle')
    del chunk_flattened_ref_df



