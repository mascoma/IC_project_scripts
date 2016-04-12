#!/usr/bin/env python3
# this script is for check the duplicate sequences in fasta file
from Bio import SeqIO
from collections import Counter
import pandas as pd

def check_dup(handle):
	seq_id = []
	dup = []
	sequences = SeqIO.parse(handle, "fasta")
	for record in sequences:
		seq_id.append (record.id)
	seq_id_count = Counter(seq_id)
	df = pd.DataFrame.from_dict(seq_id_count, orient = 'index').reset_index()
	df = df.rename(columns={'index':'seq_id', 0:'count'})
	for i in range(len(df.iloc[:, 0])):
		print(i)
		if df.iloc[i, 1] > 1:
			dup.append(df.iloc[i, 0]) 
	handle.close()
	return len(dup)
	


def main():
	inputdir = "/isi/olga/xin/Halophile_project/output/20160406/halophile_cut.fa"
	f = open(inputdir, 'rU')
	print("open successfully!")
	cd = check_dup(f)
	print("There are " + str(cd) + " duplications")

if __name__ == "__main__": main() 