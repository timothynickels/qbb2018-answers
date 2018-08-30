#!/usr/bin/env python3

#parse all FASTA records from stdin and print id and sequence

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
