#!/usr/bin/env python3

"""
usage: ./timecourse_v2.py <samples.csv> <ctab_dir> <gene name 1> <gene name 2> ... <gene name n>

create a timecourse of a specified gene name
"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

def graphFPKMs (sex,i):
    df = pd.read_csv(sys.argv[1])
    soi =df.loc[:,"sex"] == sex
    df = df.loc[soi,:]
    fpkms =[]
    # if (CSVfilename == sys.argv[2]):
#         fpkms = []
#     elif (CSVfilename == sys.argv[3]):
#         fpkms =[None,None,None,None]
        
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join(sys.argv[2],sample,"t_data.ctab")
        ctab_df = pd.read_table(filename,index_col="t_name")
    
        #fpkms.append (ctab_df.loc[sys.argv[1],"FPKM"])
        
        roi = ctab_df.loc[:,"gene_name"]==sys.argv[i]
        
        fpkms.append (np.mean(ctab_df.loc[roi,"FPKM"]))
        
    return fpkms
        
def graph (i):
    fig, ax = plt.subplots()
    plot1=graphFPKMs("female",i)
    plot2=graphFPKMs("male",i)
    
    ax.plot(plot1,'r', label="Female")
    ax.plot(plot2,'b',label="Male")
    #ax.plot(graphFPKMs("female",sys.argv[3]),'r')
    #x.plot(graphFPKMs("male",sys.argv[3]),'b')

    ax.legend(bbox_to_anchor=(1.5, 0.5))
    fig.suptitle("%s" %(sys.argv[i]))
    ax.set_ylabel("mRNA abundance (RPKM)")
    ax.set_xlabel("Developmental Stage")
    ax.set_xticks(range(9))
    ax.set_xticklabels(["10","11","12","13","14A","14B","14C","14D"])
    plt.xticks(rotation=90)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    fig.savefig(sys.argv[i] + ".png")
    plt.close(fig)
for i in range (3,len(sys.argv)):
    graph(i)
   
    