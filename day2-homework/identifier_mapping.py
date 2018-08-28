#!/usr/bin/env python3

import sys

dict = {}

for line in open(sys.argv[1]):
    fields = line.strip().split()
    dict [fields[0]] = fields[1]

for line in open(sys.argv[2]):
    if line.startswith("t_id"):
        continue
    fields_2 = line.strip().split()
    sample_flyID = (fields_2[8])
    if sample_flyID in dict.keys():
        print(dict[sample_flyID] + line.strip("\n\r") )
    if sample_flyID not in dict.keys():
        continue
        #print ("no match")
    


   