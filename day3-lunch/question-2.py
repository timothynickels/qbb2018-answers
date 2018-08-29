#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin
    
count = 0
index = {}
   
for line in f:
    fields = line.strip().split()
    if line.startswith("#"):
        continue
    for column in range (7,len(fields)):
        if fields[2] != "gene":
            continue
        if fields[column] == "gene_biotype":
            gene_type = fields[column + 1]
            if gene_type in index:
                index [gene_type] += 1
            else:
                index[gene_type] = 1
        
for name, value in index.items():
    print(name, " ", value)
