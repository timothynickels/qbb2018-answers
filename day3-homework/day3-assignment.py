#!/usr/bin/env python3

import sys
import fasta

target = open (sys.argv[1])
query = open(sys.argv[2])
k = int(sys.argv[3])

reader = fasta.FASTAReader(target)

target_d = {}

for ident, sequence in reader:
    for pos in range(0,len(sequence)-k):
        kmer = sequence[pos:pos+k]
        if kmer not in target_d:
            target_d[kmer] = [(ident,pos)]
        else:
            target_d[kmer].append( (ident,pos) )

reader2 = fasta.FASTAReader(query)

for ident, sequence in reader2:
    for pos2 in range(0,len(sequence)-k):
        kmer2 = sequence[pos2:pos2+k]
        if kmer2 in target_d.keys():
            for hit in target_d[kmer2]:
                for match in target_d[kmer2]:
                    print("MATCH ; Gene name: ", match[0], "; Target start position: ",match[1], " ; Query start position: ",pos2, " ; K-mer: ",kmer2)
            

