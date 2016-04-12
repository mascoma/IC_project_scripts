from Bio import SeqIO
from collections import Counter
import pandas as pd
inputdir = "/isi/olga/xin/Halophile_project/db_source/nr_halo.faa"
inputdir1 = "/isi/olga/xin/Halophile_project/output/20160406/nr_dup_seqlist_new.txt"
outputdir1 = "/isi/olga/xin/Halophile_project/output/20160406/nr_sgl_seq.fasta"
sgl_seq = []
seq_id_dup = []
f = open(inputdir1, 'r')
for seq in f:
	seq_id_dup.append(seq.rstrip('\n'))
handle = open(inputdir, "rU")
f1 = open(outputdir1, 'w')
print("open file successfully!")
fasta_sequences = SeqIO.parse(handle, "fasta")
#print("opened")
#i = 0
for record1 in fasta_sequences:
	#print(i)
	#i = i + 1
	if record1.id not in seq_id_dup:
		sgl_seq.append(record1)
print("alomost there!")
SeqIO.write(sgl_seq, f1, "fasta")
handle.close()
f1.close()