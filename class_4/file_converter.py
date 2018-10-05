#!/usr/bin/env python

"""
Usage:
./file_converter.py <phenotypes.txt>
"""

import sys

file1 = open(sys.argv[1])

for line in file1:
    if line.startswith("C"):
        print ("\t" + line)
    else:
        print (line.replace("_", "\t"))