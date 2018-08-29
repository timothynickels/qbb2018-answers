#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin
    
count = 0
   
for line in f:
    fields = line.strip().split()
    if line.startswith("#"):
        continue
    if fields[2] == "gene" and "protein_coding" in line:
        count += 1

print("Number of protein coding genes = " + str(count))
    