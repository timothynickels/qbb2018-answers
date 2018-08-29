#!/usr/bin/env python3

#enter reference out file from mapping.py followed by the sample file to be compared to the reference.  If a third argument is included, it will be printed prior to a line of a sample that has no match in the reference

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
        
    else:   
        if len(sys.argv) > 3:
            print (sys.argv[3] + " " + line.strip("\n\r"))
        
        
    
    
    
    


   