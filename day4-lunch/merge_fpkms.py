#!/usr/bin/env python3

"""
usage: ./merge_fpkms.py <threshold> <ctab file 1> <ctab file 2> ... <ctab file n> 

"""

import sys
import os
import pandas as pd

threshold = float(sys.argv[1])
fpkms = {}

for i in range (2,len(sys.argv)):
    

    name = sys.argv[i].split(os.sep)[-2]
    fpkm = pd.read_csv(sys.argv[i],sep="\t", index_col="t_name").loc[:,"FPKM"]
    if i == 2: 
        fpkms = {name : fpkm}
    else:
        fpkms[name] = fpkm

fpkms_df = pd.DataFrame(fpkms)

sum_roi = fpkms_df.sum(axis = 1) > threshold


fpkms_df.loc[sum_roi,:].to_csv(sys.stdout,sep="\t")


#sum_roi.to_csv(sys.stdout)