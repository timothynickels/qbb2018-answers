#!/usr/bin/env python3

"""
usage: ./timecourse_v2.py <gene_name> <samples.csv> <replicates.csv> <ctab_dir> 

create a timecourse of a specified gene name
"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

def graphFPKMs (sex):
    df = pd.read_csv(sys.argv[2])
    soi =df.loc[:,"sex"] == sex
    df = df.loc[soi,:]
    fpkms =[]
    # if (CSVfilename == sys.argv[2]):
#         fpkms = []
#     elif (CSVfilename == sys.argv[3]):
#         fpkms =[None,None,None,None]
        
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join(sys.argv[3],sample,"t_data.ctab")
        ctab_df = pd.read_table(filename,index_col="t_name")
    
        #fpkms.append (ctab_df.loc[sys.argv[1],"FPKM"])
        
        roi = ctab_df.loc[:,"gene_name"]==sys.argv[1]
        fpkms.append (np.mean(ctab_df.loc[roi,"FPKM"]))
        
    return fpkms
        


fig, ax = plt.subplots()
ax.plot(graphFPKMs("female"),'r', label="Female")
ax.plot(graphFPKMs("male"),'b',label="Male")
#ax.plot(graphFPKMs("female",sys.argv[3]),'r')
#x.plot(graphFPKMs("male",sys.argv[3]),'b')

ax.legend(bbox_to_anchor=(1.5, 0.5))
fig.suptitle("%s" %(sys.argv[1]))
ax.set_ylabel("mRNA abundance (RPKM)")
ax.set_xlabel("Developmental Stage")
ax.set_xticks(range(9))
ax.set_xticklabels(["10","11","12","13","14A","14B","14C","14D"])
plt.xticks(rotation=90)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
fig.savefig("timecourse_v2.png")
plt.close(fig)