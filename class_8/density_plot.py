#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt


"""
Usage: ./density_plot.py bedtools_out
"""

file1 = open(sys.argv[1])

position = []
for line in file1:
    fields = line.rstrip("\r\n").split("\t")
    start = int(fields[1])
    end = int(fields[2])
    motif = int(fields[13])
    length = end-start
    motif_position = motif-start
    relative = motif_position/length
    position.append(relative)

fig, axes = plt.subplots()
fig.suptitle("Relative Location of Motif Match in Sequence")
axes.hist(position, bins = 30)
axes.set_xlabel("(Motif Start - Sequence Start)/Length")
axes.set_ylabel("Number")    
fig.savefig("density_plot.png")
plt.close(fig)
