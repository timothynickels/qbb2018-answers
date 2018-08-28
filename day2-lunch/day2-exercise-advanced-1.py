#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin
    
count = 0
total = 0

for line in f:
    if line.startswith("SRR") and "2L" in line:
        cut = line.strip().split("\t")
        if int(cut[3]) >= 10000 and int(cut[3]) <= 20000:
            count += 1
        
        
        
        
print ("number of genes aligned to 2L between 10k and 20k = " + str(count))