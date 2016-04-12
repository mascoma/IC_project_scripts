from Bio import SeqIO
from collections import Counter
import pandas as pd
inputdir = "/isi/olga/xin/Halophile_project/db_source/nr_halo.faa"
outputdir1 = "/isi/olga/xin/Halophile_project/output/20160401/nr_sgl_seq.fasta"
outputdir2 = "/isi/olga/xin/Halophile_project/output/20160401/nr_dup_seq.fasta"
seq_id = []
seq_id_sgl = []
seq_id_dup = []
sgl_seq = []
dup_seq = []
handle = open(inputdir, "rU")
f1 = open(outputdir1, 'w')
f2 = open(outputdir2, 'w')
print("open file successfully!")
fasta_sequences = SeqIO.parse(handle, "fasta")
for record in  fasta_sequences:
	seq_id.append (record.id)
seq_id_count = Counter(seq_id)
df = pd.DataFrame.from_dict(seq_id_count, orient = 'index').reset_index()
df = df.rename(columns={'index':'seq_id', 0:'count'})
handle.close()
print("seq id list done!")
for i in range(len(df.iloc[:, 0])):
	if df.iloc[i, 1] > 1:
		seq_id_dup.append(df.iloc[i, 0])
	if df.iloc[i, 1] == 1:
		seq_id_sgl.append(df.iloc[i, 0])
print("divided seq id to two groups (sigle copy and dupliates)")
handle = open(inputdir, "rU")
fasta_sequences = SeqIO.parse(handle, "fasta")
#print("opened")
#i = 0
for record1 in fasta_sequences:
	#print(i)
	#i = i + 1
	if record1.id in seq_id_dup:
		dup_seq.append(record1)
	else:
		sgl_seq.append(record1)
print("alomost there!")
SeqIO.write(dup_seq, f2, "fasta")
SeqIO.write(sgl_seq, f1, "fasta")
handle.close()
f1.close()
f2.close()