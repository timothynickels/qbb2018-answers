#!/usr/bin/env python3

"""
usage: ./ma_plot.py <ctab file1> <ctab file2>

create an MA plot for two samples
"""

import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math 

name1 = sys.argv[1].split(os.sep)[-2]
fpkm1 = pd.read_csv(sys.argv[1],sep="\t", index_col="t_name").loc[:,"FPKM"]

name2 = sys.argv[2].split(os.sep)[-2]
fpkm2 = pd.read_csv(sys.argv[2],sep="\t", index_col="t_name").loc[:,"FPKM"]

m = np.log2((fpkm1 +0.1)/(fpkm2 +0.1))
a = 1/2 * (np.log2((fpkm1 +0.1) * (fpkm2 +0.1)))

df = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")



fig, ax = plt.subplots()

ax.scatter(a,m,alpha=0.1)
ax.set_title("M A plot for "+name1+" vs "+name2)
ax.set_xlabel("A")
ax.set_ylabel("M")
# ax.set_yscale('log')
# ax.set_xscale('log')
#ax.set_ylim([-1,10])
#ax.set_xlim([-1,10])
fig.savefig("ma_plot.png")
plt.close(fig)
