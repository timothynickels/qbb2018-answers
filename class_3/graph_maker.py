#!/usr/bin/env python

"""
Usage:
./graph_maker.py <vcf> <summary.txt>
"""

import sys
import matplotlib.pyplot as plt
import numpy as np

file1 = open(sys.argv[1])
file2 = open(sys.argv[2])

freq = []
depth = []
qual = []

i=1
for line in file1:
    if line.startswith('#'):
        pass
    else:
        seg = line.rstrip('\r\n').split('\t')
        freqs = seg[7].split(';')[3].lstrip('AF=').split(',')
        depths = seg[7].split(';')[7].lstrip('DP=').split(',')
        quals = seg[9].split(':')
        try:
            gq = quals[1].split(',')
        except IndexError:
            i += 1
        for q in freqs:
            freq.append(float(q))
        for r in depths:
            depth.append(float(r))
        for s in gq:
            qual.append(float(s))
            i += 1

name = []
pred = []

for line in file2:
    seg1 = line.rstrip('\r\n').split('\t')
    name.append(seg1[0])
    pred.append(int(seg1[1]))
    

fig, axes = plt.subplots(nrows=2,ncols=2)
axes = axes.flatten()

fig.set_size_inches(20,12)

axes[0].hist(freq, bins = 200, color = "black")
axes[0].set_xlabel('Frequency')
axes[0].set_ylabel('Position')
axes[0].set_title('Allele frequency')

axes[1].hist(np.log10(depth), bins = 200, color = "black")
axes[1].set_xlabel('position')
axes[1].set_ylabel('read depth')
axes[1].set_title('Read Depth')

axes[2].hist(qual, bins = 200, color = "black")
axes[2].set_xlabel('Quality')
axes[2].set_ylabel('Position')
axes[2].set_title('Genotype Quality')

axes[3].bar(name,pred, color = "black")
axes[3].set_xlabel('Predicted values')
axes[3].set_ylabel('Position')
axes[3].set_title('Predicted effect of each variant')
axes[3].set_xticklabels(name, rotation=45)

plt.savefig('graphs.png')
plt.close(fig)