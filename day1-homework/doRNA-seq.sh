#!/bin/bash

GENOME=../genomes/BDGP6
ANNOTATION=../genomes/BDGP6.Ensembl.81.gtf

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
  echo "running pipeline on $SAMPLE"
  mkdir $SAMPLE
  echo "running fastq"
  fastqc ~/data/rawdata/${SAMPLE}.fastq 
  echo "running hisat2"
  hisat2 -p 4 -x $GENOME -U ~/data/rawdata/${SAMPLE}.fastq -S ${SAMPLE}/alignment.sam
  echo "running samtools sort"
  samtools sort -o ${SAMPLE}/alignment.bam ${SAMPLE}/alignment.sam
  echo "running samtools index" 
  samtools index ${SAMPLE}/alignment.bam
  echo "running stringtie"
  stringtie -p 4 -B -e -G $ANNOTATION -o ${SAMPLE}/alignment.gtf ${SAMPLE}/alignment.bam
done
