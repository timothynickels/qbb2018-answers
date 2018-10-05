#!/usr/bin/env python

"""
Usage:
./graphing.py <plink.eigenvec> <vcf> <plink.*.qassoc>
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import statistics

file1 = open(sys.argv[1])
file2 = open(sys.argv[2])
file3 = open(sys.argv[3])

component1 =[]
component2 =[]

for line in file1:
        fields = line.rstrip('\r\n').split()
        component1.append(float(fields[2]))
        component2.append(float(fields[3]))

plt.figure()
plt.scatter(component1, component2)       
plt.xlabel( 'component 1' )
plt.ylabel( 'component 2' )
plt.title( "Principle Component Analysis" )
plt.savefig( "pca.png")
plt.close()
 
frequencies = []
i=1
for line in file2:
    if line.startswith('#'):
        pass
    else:
        fields2 = line.rstrip('\r\n').split('\t')
        freqs = fields2[7].lstrip('AF=')
        if "," in freqs:
            r = freqs.split(",")
            frequencies.append(float(r[0]))
            frequencies.append(float(r[1]))
        else:
            frequencies.append(float(freqs))
        
plt.figure()
plt.hist(frequencies, bins = 200)       
plt.xlabel( 'Frequency' )
plt.ylabel( 'Position' )
plt.title( "Allele Frequency" )
plt.savefig( "allele_frequency.png")
plt.close()

for name in sys.argv[3:]:
    
    condition = name.split(".")[1]
    
    fig, axes = plt.subplots(figsize=(15,10))
    fig.suptitle('{}'.format(condition))
    axes.set_xlabel("Chromosome")
    axes.set_ylabel("-log_10(P)")    
    
    with open(name) as name:
        dictionary = {}
        for i, line in enumerate(name):
            if i == 0:
                continue
            else:
                fields=line.rstrip("\r\n").split()
                if fields[-1] != "NA":
                    chromo = fields[0]
                    bp = int(fields[2])
                    pValue = float(fields[-1])
                    if chromo not in dictionary:
                        dictionary[chromo]=[(pValue,bp)]
                    else:
                        dictionary[chromo].append((pValue,bp))
                        
        lastX=0
        xTicks = []
        xTicksLoc = []
        
        for i, chromo in enumerate(dictionary):
            y,x = zip(*dictionary[chromo])
            x = np.array([val + lastX for val in x])
            y = np.array(-np.log10(y))
            if chromo == '26':
                chromo = "chrX"
            elif chromo == '23':
                chromo = "chrM"
            xTicks.append(chromo)
            lastX = max(x)
            significance = y>5
            xTicksLoc.append(statistics.median(x))
            colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'gray', 'black', 'turquoise', 'indigo']
            plt.scatter(x[significance], y[significance], c=colors[i%10], alpha = 0.25)
            plt.scatter(x[~significance], y[~significance], c=colors[i%10])
            
        axes.set_xticklabels(xTicks, rotation=90)    
        axes.axhline(-np.log10(10**-5), linestyle='--')
        plt.xticks(xTicksLoc)       
        fig.savefig("manhattan_plot_{}.png".format(condition))
        plt.close(fig)