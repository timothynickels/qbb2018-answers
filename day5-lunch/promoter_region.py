#!/usr/bin/env python3

"""
usage: ./promoter_region.py <ctab_file>

makes a file containing chromosome \t start \t  end \t t_name where start \t end is +/- 500bp from start site
"""

import sys
import pandas as pd

# df = pd.read_csv(sys.argv[1],sep="\t")
#
# new_start = df.loc[:,"start"]-500
# new_end = df.loc[:,"start"]+500
#
# df2 = df.assign(start=new_start, end=new_end)
#
# coi = ["chr","start","end","t_name"]
#
# df2.loc[:,coi].to_csv(sys.stdout, sep="\t",index=False)

ctab_file = open(sys.argv[1])

for i, line in enumerate (ctab_file):
    if i == 0:
        continue
    fields = line.rstrip("\r\n").split("\t")
    if int(fields[3])<500:
        fields[3]="500"
    order = [fields[1], str(int(fields[3])-500), str(int(fields[3])+500), fields[5]]
    if fields[2]=="-":
        order = [fields[1], str(int(fields[3])+500), str(int(fields[3])-500), fields[5]]
        
    print("\t".join(order))

