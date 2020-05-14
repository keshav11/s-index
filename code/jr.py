
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import difflib
import fuzzymatcher


# In[2]:

j_df = pd.read_csv('jr.csv', sep=';')

# In[5]:

sjr_null_count = j_df['SJR'].isnull().sum()
pub_null_count = j_df['Publisher'].isnull().sum()
sjr_null_count, pub_null_count

# In[6]:

# Replace nulls in SJR with zeroes, this is what the Scimagojr website suggests.
# Eg: https://www.scimagojr.com/journalsearch.php?q=21100817106&tip=sid&clean=0
j_df.loc[j_df['SJR'].isnull(), 'SJR'] = 0

# In[7]:

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

# In[11]:

# # Without a fuzzy join we only matched 622702 out of 3079007 rows. Now we consider a fuzzy join.

t = fuzzymatcher.fuzzy_left_join(dblp_df[3000000:], j_df, ['venue'], ['Title'])
print('done')
PICKLE_PATH = 'dblp_jr11.pickle'
t.to_pickle(PICKLE_PATH)

# In[ ]:
