#!/usr/bin/env python3

"""
Usage: compute the number of contigs, min/max/average contig length, and N50

./contigs.py <contigs.fa> <contigs.fasta>
#contigs.fa from velvetg output #contigs.fasta from SPAdes output
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import fasta
from itertools import groupby


lengths = []

fasta_file = fasta.FASTAReader(open(sys.argv[1]))

for name, seq in fasta_file:
    lengths.append(len(seq))

# sort contigs longest>shortest
tot_length=sorted(lengths, reverse=True)
csum=np.cumsum(tot_length)

print ("Max length = " + str(tot_length[0]))
print ("Min length = " + str(tot_length[-1]))

n2=int(sum(lengths)/2)

print ("median =" + str(n2))

# get index for cumsum >= N/2
csumn2=min(csum[csum >= n2])
ind=np.where(csum == csumn2)

n50 = tot_length[ind[0][0]]
print ("N50= " + str(n50))