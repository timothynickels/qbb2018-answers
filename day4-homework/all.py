#!/usr/bin/env python3

"""
usage: ./all.py <samples.csv> <ctab_dir>

create a single file containing all of the data from the stringtie folder with the proper header from samples.csv
"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1])

d = {}

for index, sample, sex, stage in df.itertuples():
    filename = os.path.join(sys.argv[2],sample,"t_data.ctab")
    ctab_df = pd.read_table(filename,index_col="t_name").loc[:,"FPKM"]
    d[("_".join([sex,stage]))] = ctab_df
    
df_fpkms = pd.DataFrame(d)
df_fpkms.to_csv(sys.stdout,sep=",")


    
    