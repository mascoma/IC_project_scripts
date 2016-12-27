#!/usr/bin/env python3
# this script is for estimating the isoelectric point of ICC and SS37
# input files generate using program FGS+ 
# FGS+ -s /isi/olga/xin/Halophile_project/input/merged_reads_CLC_fa/ICC_CLC.fasta -o /isi/olga/xin/Halophile_project/output/20160420/ICC_aa -w 0 -t illumina_10 -e 1 -d 1 
# FGS+ -s /isi/olga/georgia/SS37/fasta/trimmed_SS37.fasta -o /isi/olga/xin/Halophile_project/output/20160421/SS37_aa -w 0 -t 454_10 -e 1 -d 1 
# input files /isi/olga/xin/Halophile_project/output/20160420/ICC_aa.faa
# input files /isi/olga/xin/Halophile_project/output/20160421/SS37_aa.faa

from Bio import SeqIO
from Bio.SeqUtils import IsoelectricPoint 
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import numpy as np
import pandas as pd
def main():
	ieps = []
	seqid = []
	inputfile = "/isi/olga/xin/Halophile_project/output/20160421/SS37_aa.faa"
	outputfile = "/isi/olga/xin/Halophile_project/output/20160421/SS37_reads_isp.txt"
	f = open(inputfile, 'rU')
	sequences = SeqIO.parse(f, "fasta")
	for record in sequences:
		seqid.append(record.id)
		seq = str(record.seq)
		seq_pa = ProteinAnalysis(seq)
		ie = seq_pa.isoelectric_point() 
		ieps.append(ie)
	read_ieps = np.column_stack((seqid, ieps))
	df = pd.DataFrame(read_ieps)
	df.to_csv(outputfile, sep = '\t', header = False)

if __name__ == "__main__": main() 