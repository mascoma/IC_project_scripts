#!/usr/bin/python3

from Bio import SeqIO
class Subsampling:
    def include_seq(self, inputdir, format, readlist, outputdir):        
		seq = []
		try:
		    handle = open(inputdir, "rU")
		except IOError:
			print ("no such file!")
		f = open(outputdir, 'w')
		fasta_sequences = SeqIO.parse(handle, format)
		for record in fasta_sequences:
 			if record.id in readlist:
				seq.append(record) 
		SeqIO.write(seq, f, format)
		handle.close()
		f.close()
    
    def exclude_seq(self, inputdir, format, readlist, outputdir):        
		seq = []
		try:
		    handle = open(inputdir, "rU")
		except IOError:
			print ("no such file!")
		f = open(outputdir, 'w')
		fasta_sequences = SeqIO.parse(handle, format)
		for record in fasta_sequences:
 			if record.id not in readlist:
				seq.append(record) 
		SeqIO.write(seq, f, format)
		handle.close()
		f.close()

 