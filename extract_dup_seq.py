from Bio import SeqIO
from collections import Counter
import pandas as pd
inputdir = "/isi/olga/xin/Halophile_project/db_source/nr_halo.faa"
inputdir1 = "/isi/olga/xin/Halophile_project/output/20160406/nr_dup_seqlist_new.txt"
outputdir2 = "/isi/olga/xin/Halophile_project/output/20160406/nr_dup_seq_test.fasta"
dup_seq = []
seq_id_dup = []
f = open(inputdir1, 'r')
for seq in f:
	seq_id_dup.append(seq.rstrip('\n'))
handle = open(inputdir, "rU")
f2 = open(outputdir2, 'w')
handle = open(inputdir, "rU")
fasta_sequences = SeqIO.parse(handle, "fasta")
#print("opened")
i = 0
for record1 in fasta_sequences:
	print(i)
	i = i + 1
	if record1.id in seq_id_dup:
		dup_seq.append(record1)
print("alomost there!")
SeqIO.write(dup_seq, f2, "fasta")
handle.close()
f2.close()