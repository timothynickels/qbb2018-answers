#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin
    
dist = 0
find_pos = 21378950
closest_name = ""
closest_name2 = ""
closest_distance = 30000000
closest_distance2 = 30000000

for line in f:
    fields = line.strip().split()
    if line.startswith("#"):
        continue
    for column in range (0,len(fields)):
        if fields[2] != "gene":
            continue
        if fields[0] != "3R":
            continue
        if fields[column] == "gene_biotype":
            gene_type = fields[column + 1]
        
            
            if gene_type == '"protein_coding";':
                gene_start = int(fields[3])
                gene_end = int(fields[4])
                if find_pos < gene_start:
                    dist = gene_start - find_pos
                elif find_pos > gene_end:
                    dist = find_pos - gene_end
                if dist < closest_distance:
                    closest_distance = dist
                    closest_name = fields[13]
            
            
        
            elif gene_type != '"protein_coding";':
                gene_start = int(fields[3])
                gene_end = int(fields[4])
                if find_pos < gene_start:
                    dist = gene_start - find_pos
                elif find_pos > gene_end:
                    dist = find_pos - gene_end
                if dist < closest_distance2:
                    closest_distance2 = dist
                    closest_name2 = fields[13]
                    
print("The closest protein coding gene is ", closest_name)
print("The closest  non protein coding gene is ", closest_name2)