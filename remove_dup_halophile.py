from Bio import SeqIO
from collections import Counter
import pandas as pd
inputdir1 = "/isi/olga/xin/Halophile_project/output/20160406/halophiles.fa"
inputdir2 = "/isi/olga/xin/Halophile_project/output/20160406/nr_dup_seqlist_new.txt"
outputdir = "/isi/olga/xin/Halophile_project/output/20160406/halophile_sgl.faa"
outputdir1 = "/isi/olga/xin/Halophile_project/output/20160406/halophile_dup.faa"
outputdir2 = "/isi/olga/xin/Halophile_project/output/20160406/halophile_dup_list.txt"
seq_id_halo = []
seq_id_dup = []
halo_dup = []
halo_sgl = []
sgl_seq = []
dup_seq = []
dup_id = []
handle1 = open(inputdir1, "rU")
f = open(inputdir2, "r")
f1 = open(outputdir, 'w')
f2 = open(outputdir1, 'w')
f3 = open(outputdir2, 'w')
print("open file successfully!")

halo_sequences = SeqIO.parse(handle1, "fasta")
for record in  halo_sequences:
	seq_id_halo.append (record.id)
seq_id_count = Counter(seq_id_halo)
df = pd.DataFrame.from_dict(seq_id_count, orient = 'index').reset_index()
df = df.rename(columns={'index':'seq_id', 0:'count'})
for i in range(len(df.iloc[:, 0])):
	if df.iloc[i, 1] > 1:
		halo_dup.append(df.iloc[i, 0]) 
	if df.iloc[i, 1] == 1:
		halo_sgl.append(df.iloc[i, 0])
print >> f3, halo_dup

for line in f:
	seq_id_dup.append(line[1:-2])

handle1.close()
handle1 = open(inputdir1, "rU")
halo_sequences = SeqIO.parse(handle1, "fasta")
j = 0
for record1 in halo_sequences:
	print(j)
	j = j + 1
	#if record1.id in seq_id_dup:
	#	print(record1.id)
	#	print("T")
	if record1.id not in seq_id_dup and record1.id not in halo_dup :
		sgl_seq.append(record1)
	elif record1.id not in seq_id_dup and record1.id in halo_dup :
		if record1.id not in dup_id:
			dup_id.append(record1.id)
			dup_seq.append(record1)

 
SeqIO.write(sgl_seq, f1, "fasta")
SeqIO.write(dup_seq, f2, "fasta")

 
handle1.close()
f1.close()
f2.close()
f3.close()