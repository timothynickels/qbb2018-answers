#!/usr/bin/env python

"""
Usage:
./dot_plot_generator.py <lastz sorted out file> <selected output name>
"""

import sys
import matplotlib.pyplot as plt

count_1 = 0
count_2 = 0
plt.figure()
for line in open( sys.argv[1] ):
    count_1 += 1
    if count_1 == 1:
        continue
    else:
        line = line.rstrip('\r\n').split('\t')
        start, stop = int(line[0]), int(line[1])
        plt.plot( [start, stop], [count_2, count_2 + abs(stop - start)] )
        count_2 += abs(stop - start)

plt.xlim( 0, 100000 )
plt.ylim( 0, 80000 )
plt.xlabel( 'reference' )
plt.ylabel( 'contig' )
plt.title( sys.argv[2] )
plt.savefig( str(sys.argv[2]) + ".png")
plt.close()