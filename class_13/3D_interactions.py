#!/usr/bin/env python

"""
Usage: ./3D_interactions.py GSM2418860_WT_CTCF_peaks.txt
"""

import hifive
import numpy as np
import sys

peaks=[]
for line in open(sys.argv[1]):
    fields = line.strip("\r\n").split("\t")
    if fields[0] == "chr17":
        if int(fields[1]) >= 15000000 and int(fields[2]) <= 17500000:
            peaks.append((int(fields[1])+int(fields[2]))/2)
        
            
hic = hifive.HiC('hifive_output.hcp')
data = hic.cis_heatmap(chrom="chr17", start=15000000, stop=17500000, binsize=10000, datatype='fend', arraytype='full')
data[:, :, 1] *= np.sum(data[:, :, 0]) / np.sum(data[:, :, 1])
where = np.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
data = data[:, :, 0]

bins =[]
for value in peaks:
    i=(value - 15000000)/10000
    bins.append(i)

bins=np.unique(bins)
bins1l = []
bins2l = []
enrichedl = []

for i in range(len(bins)):
    for j in range(i,len(bins)):
        enrichment = float(data[bins[i],bins[j]])
        if enrichment >= 1:
            enrichedl.append(
            ((bins[i]*10000)+15000000, 
            (bins[j]*10000)+15000000, 
            enrichment))

enriched=np.array(enrichedl, dtype=np.dtype([('bin1', int), ('bin2', int), ('score', float)]))
sort = np.argsort(enriched, order=('score', 'bin1'))[::-1]
enriched = enriched[sort]
print "Chr17 Start\tChr17 End\tEnrichment"
for start,end,score in enriched:
    print start, "\t", end, "\t", score
