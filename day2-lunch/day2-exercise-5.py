#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin
    
count = 0
total = 0

for line in f:
    if line.startswith("SRR"):
        count += 1
        cut = line.strip().split("\t")
        total += int(cut[4])
average = total / count
        
        
print ("MAPQ average = " + str(average))