grep "SRR072893" SRR072893.sam >grep.sam
cut -f 3 grep.sam | grep -v "^211" | sort | uniq -c <chromosome_alignments.sam
