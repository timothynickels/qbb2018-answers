#!/usr/bin/env python3

#<dna sequence> , <aligned amino acid sequence>

import sys

class FASTAReader(object):
    
    def __init__(self,file):
        self.last_ident = None
        self.file = file
        self.eof = False
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.eof:
            raise StopIteration
        if self.last_ident is not None:
            #Not first line
            ident = self.last_ident
            
        else:
            #First line
            line = self.file.readline()
            if line == "":
                return None, None
            
            assert line.startswith(">"), "Not a FASTA file"
            ident = line[1:].rstrip("\r\n") 

        sequences = []
        while True:
            line = self.file.readline()
            if line == "":
                self.eof = True
                break
            elif not line.startswith(">"):
                sequences.append(line.strip())
            else:
                self.last_ident = line[1:].rstrip("\r\n")
                break
        sequence = "".join(sequences)
        return ident, sequence

dna_reader = FASTAReader(open(sys.argv[1]))
aa_reader = FASTAReader(open(sys.argv[2]))


for (dna_id,dna),(aa_id,aa) in zip(dna_reader,aa_reader):
    new = ""
    j=0
    for i in range (0,len(aa)):
        amino=aa[i]
        nucleotide = dna[i*3:(i+1)*3]
        if amino == "-":
            n = "---"
        else:
            n = dna[j*3:(j+1)*3]
            j+=1
        new += n
    print(">"+dna_id+"\n" + new +"\n")




