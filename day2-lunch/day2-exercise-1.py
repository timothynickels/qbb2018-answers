#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin
    
count = 0

for line in f:
    if line.startswith("SRR"):
        count += 1
print ("Number of alignments = " + str(count))


        
    #fields = line.rstrip("\r\n").split("\t")
    #tx_len = int (fields[4]) - int (fields[3])
    
    
    #print (fields[5], tx_len)