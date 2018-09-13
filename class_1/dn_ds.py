#!/usr/bin/env python3


import sys
import numpy as np
import matplotlib.pyplot as plt

#fasta reader
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
        
#code starts here

"""
./dn_ds.py alignment.out blast_translated_aligned.fa 
"""

dna_reader = FASTAReader(open(sys.argv[1]))
prot_reader = FASTAReader(open(sys.argv[2]))
codons = {} 
codons_ratio = {} 
no_change = 0
syn = 0
non_syn = 0
alignments = 0

for (dna_id, dna), (aa_id, aa) in zip(dna_reader, prot_reader): 
    
    if dna_id == "gi|11497619|gb|M12294.2|WNFCG": 
        ref_dna = dna
        ref_prot = aa
    else:
        alignments += 1 
        j = 0 
        acd = 0 
        for i in range(len(ref_prot)): 
            if ref_dna[j:(j+3)] == "---": 
                j += 3
            else: 
                if dna[j:(j+3)] == ref_dna[j:(j+3)]: 
                    if acd in codons: 
                        no_change, syn, non_syn = codons[acd] 
                        no_change += 1 
                        codons[acd] = (no_change, syn, non_syn) 
                    else: 
                        codons[acd] = (1,0,0) 
                   
                    j += 3
                    acd += 1
                else: 
                    if aa[i] == ref_prot[i]: 
                        if acd in codons:
                            no_change, syn, non_syn = codons[acd]
                            syn += 1
                            codons[acd] = (no_change, syn, non_syn)
                        else:
                            codons[acd] = (0,1,0)
                        
                        j += 3
                        acd += 1

                    else: 
                        if acd in codons:
                            no_change, syn, non_syn = codons[acd]
                            non_syn += 1
                            codons[acd] = (no_change, syn, non_syn)

                        else:
                            codons[acd] = (0,0,1)
                        j += 3
                        acd += 1



X = []
y = []
difference = []
totalCounts = []
SigX = []
Sigy = []
InsigX = []
Insigy = []

for i in range(1,len(codons)):
    no_change, syn, non_syn = codons[i]
    if syn != 0:
        codons_ratio[i] = float(non_syn)/float(syn)
    else:
        codons_ratio[i] = non_syn/(0.5)
    difference.append(float(non_syn)-float(syn))
    totalCounts.append(float(non_syn)+float(syn))
    X.append(i)
    y.append(codons_ratio[i])


for i, value in enumerate(difference):
    stdev = np.std(difference)
    stderr = stdev/totalCounts[i]**.5
    t = (value -0)/stderr
    if t > 2.58:
        SigX.append(X[i])
        Sigy.append(y[i])
    else:
        InsigX.append(X[i])
        Insigy.append(y[i])
        


fig, ax = plt.subplots(figsize=(25,10))
ax.scatter(SigX, np.log2(Sigy), color='b', alpha = 0.5, s=9)
ax.scatter(InsigX, np.log2(Insigy), alpha = 0.5, s=9)
x = np.linspace(0, len(codons)+1)
y = alignments
y50=[]
for i in range(len(x)):
    y50.append(y)
plt.plot(x, np.log2(y50), color = 'r', linestyle='dashed')
fig.suptitle("dN/dS")
ax.set_xlabel("Codon")
ax.set_ylabel("log2(dN/dS)")
fig.savefig("dn_ds.png")
plt.close(fig)

        




    