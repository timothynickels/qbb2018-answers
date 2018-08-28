#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin
    
count = 0

for line in f:
    cut = line.strip().split("\t")
    if "NM:i:0" in line:
        count += 1
        print ("Chromosome of alignment " + str(count) + "= " + str(cut[2]))
    if count >9:
        break
        