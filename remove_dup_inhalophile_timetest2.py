#!/usr/bin/env python3
# pipeline to clean the duplicates in halophile genome
from Bio import SeqIO
from collections import Counter
import pandas as pd
import re 
import csv
import time

## this funtion is to extract all the gi number from sequence files nr or halophile genome
def extract_seqid(inputdir):
	handle = open(inputdir, 'rU')
	seq_id = []
	sequences = SeqIO.parse(handle, "fasta")
	for record in sequences:
		record.gi = re.search("^\w+\|([\d\w\.]+)", record.id)
		seq_id.append (record.gi.group(1))
	handle.close()
	return(seq_id)

## this function is to find the overlapped sequences between nr and halophile genome and return the list of seqid
def overlap_seqid(df1, df2):
	overlap = pd.merge(df1, df2, how = 'inner', on = 'seq_id')
	return(overlap)


## this function is to filter out the sequences in halophile genome, which are also exist in nr. 

def remove_overlap(inputdir, overlap, outputdir):
	handle = open(inputdir, 'rU')
 	seq = []
	f = open(outputdir, 'w')
	fasta_sequences = SeqIO.parse(handle, "fasta")
	for record in fasta_sequences:
		record.gi = re.search("^\w+\|([\d\w\.]+)", record.id)
		if record.gi.group(1) not in overlap:
			seq.append(record) 
	SeqIO.write(seq, f, "fasta")
	handle.close()
	f.close()


# this function is for check the duplicate sequences in fasta file

def check_dup(inputdir):
	handle = open(inputdir, 'rU')
	seq_id = []
	dup = []
	sequences = SeqIO.parse(handle, "fasta")
	for record in sequences:
		seq_id.append (record.id)
	seq_id_count = Counter(seq_id)
	df = pd.DataFrame.from_dict(seq_id_count, orient = 'index').reset_index()
	df = df.rename(columns={'index':'seq_id', 0:'count'})
	for i in range(len(df.iloc[:, 0])):
		if df.iloc[i, 1] > 1:
			dup.append(df.iloc[i, 0])
	handle.close()
	return(len(dup))


## this function is to remove the duplicate sequences in fasta file:
def remove_dup(inputdir, outputdir):
	handle = open(inputdir, 'rU')
	seq_id = []
	seq = []
	f = open(outputdir, 'w')
	sequences = SeqIO.parse(handle, "fasta")
	for record in sequences:
		if record.id not in seq_id:
			seq_id.append (record.id)
			seq.append(record)
	SeqIO.write(seq, f, "fasta")
	handle.close()
	f.close()


def main(): 
	inputdir1 = "/isi/olga/xin/Halophile_project/db_source/aa/nr.faa"  # load nr.fa
	inputdir2 = "/isi/olga/xin/Halophile_project/output/20160406/halophiles.fa"  # load halophile_genome.fa
	outputdir1 = "/isi/olga/xin/Halophile_project/output/20160729/halophiles_noneoverlap.fa"
 	## output after removing the overlapped sequences
	outputdir2 =  "/isi/olga/xin/Halophile_project/output/20160729/halophiles_clean.fa" 
	## output after removing the duplicates sequences if exist
	start_time = time.clock()
	nr_seqid = extract_seqid(inputdir1)
	print time.clock() - start_time, "seconds"

	start_time = time.clock()
	halo_seqid = extract_seqid(inputdir2)
	print time.clock() - start_time, "seconds"

	start_time = time.clock()
	nr_seqid_df1 = pd.DataFrame(nr_seqid, columns = ['seq_id'])
	halo_seqid_df2 = pd.DataFrame(halo_seqid, columns = ['seq_id'])
	halo_nr_seqid = overlap_seqid(nr_seqid_df1, halo_seqid_df2)
	halonr_seqid_list = halo_nr_seqid['seq_id'].tolist()
	print time.clock() - start_time, "seconds"

	start_time = time.clock()
	remove_overlap(inputdir2, halonr_seqid_list, outputdir1)
	print time.clock() - start_time, "seconds"

	start_time = time.clock()
	num_dup = check_dup(outputdir1)
	print time.clock() - start_time, "seconds"
	
	start_time = time.clock()
	if num_dup > 0:
		remove_dup(outputdir1, outputdir2)
	else:
		print("halophile genome dataset has already been cleaned!!")
	print time.clock() - start_time, "seconds"
if __name__ == "__main__": main() 