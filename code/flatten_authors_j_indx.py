import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import sys
import math

ranked_papers = pd.read_pickle('dblp_final_paper_rankings.pickle')

keep_cols = ['authors', 'year', 'normalized_citation_score_scaled','SJR_Normalized','reach_normalized','id', 'j-index', 'normalized_citation_score']
cols = ['year', 'normalized_citation_score_scaled','SJR_Normalized','reach_normalized','id', 'j-index', 'normalized_citation_score']
papers = ranked_papers[keep_cols].set_index(cols)

chunk_sz = 300000
papers_chunks = [papers[i : i + chunk_sz] for i in range(0, papers.shape[0], chunk_sz)]

for chunk in enumerate(papers_chunks):
        chunk_flattened_auths_df = chunk[1].authors.apply(pd.Series).stack().reset_index(level=2, drop=True).to_frame('authors').reset_index()
        chunk_flattened_auths_df.to_pickle('flattened_chunks_more_fields/ranked_authors'+ str(chunk[0]) + '.pickle')
        del chunk_flattened_auths_df

