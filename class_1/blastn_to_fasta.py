#!/usr/bin/env python3

#converts the output of blastn -outfmt "6 seq_id sseq" to a fasta file

import sys

for line in sys.stdin:
    split = line.rstrip("\r\n").split("\t")
    print(">" + split[0] + "\n" +split[1] + "\n")