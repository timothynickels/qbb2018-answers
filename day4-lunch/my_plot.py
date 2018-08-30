#!/usr/bin/env python3

"""
usage: ./my_plot.py <ctab file> <ctab file>

"""

import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

name1 = sys.argv[1].split(os.sep)[-2]
fpkm1 = pd.read_csv(sys.argv[1],sep="\t", index_col="t_name").loc[:,"FPKM"]
log_fpkm1 = np.log(fpkm1 +1)

name2 = sys.argv[2].split(os.sep)[-2]
fpkm2 = pd.read_csv(sys.argv[2],sep="\t", index_col="t_name").loc[:,"FPKM"]
log_fpkm2 = np.log(fpkm2 +1)

df = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")



fig, ax = plt.subplots()
p = np.polyfit(log_fpkm1, log_fpkm2, 1)
x = np.linspace(0,8)
curve = np.poly1d(p)
ax.scatter(log_fpkm1,log_fpkm2,alpha=0.1)
ax.set_title("FPKM comparison")
ax.set_xlabel(name1+ " log FPKM")
ax.set_ylabel(name2+" log FPKM")
# ax.set_yscale('log')
# ax.set_xscale('log')
ax.set_ylim([-1,10])
ax.set_xlim([-1,10])
plt.plot(x, curve(x) ,'k')
fig.savefig("FPKM_plot.png")
plt.close(fig)
