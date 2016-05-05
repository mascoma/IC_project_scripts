from Bio import SeqIO
inputdir = "/isi/olga/xin/Halophile_project/output/20160429/halophiles.fa"
outputdir2 = "/isi/olga/xin/Halophile_project/output/20160429/test.fa"
seq_id = []
seq = []
handle = open(inputdir, "rU")
f2 = open(outputdir2, 'w')
fasta_sequences = SeqIO.parse(handle, "fasta")
i = 0
for record1 in fasta_sequences:
	print i
	i = i + 1
	if record1.id not in seq_id:
		seq_id.append(record1.id)
		seq.append(record1) 
SeqIO.write(seq, f2, "fasta")
handle.close()
f2.close()