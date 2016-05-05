import re 
from Bio import SeqIO
import pandas as pd
import csv
inputdir = "/isi/olga/xin/Halophile_project/output/20160429/halophiles_nodup.fa"
inputdir2 = "/isi/olga/xin/Halophile_project/output/20160429/dup_seqid.txt"
outputdir2 = "/isi/olga/xin/Halophile_project/output/20160429/halophiles_sgl.fa"
seqid = []
seq = []
seq_id = pd.read_csv(inputdir2, sep = ',')
handle = open(inputdir, "rU")
f2 = open(outputdir2, 'w')
fasta_sequences = SeqIO.parse(handle, "fasta")
seq_id.iloc[:, 1]
for i in range(len(seq_id.iloc[:, 1])):
	seqid.append(seq_id.iloc[i, 1])
for record1 in fasta_sequences:
	tmp = re.search('[A-Za-z]+\|([A-Za-z0-9\.]+)', record1.id)
	rec = tmp.group(1)
	if 'peg' not in rec:
		rec = int(rec)
	if rec not in seqid:
		seq.append(record1) 
SeqIO.write(seq, f2, "fasta")
handle.close()
f2.close()