import re 
import pandas as pd
import csv
def main(): 

	input1 = "/isi/olga/xin/Halophile_project/output/20160428/ICC_DS2_2_unmapped_reads.txt"
	input2 = "/isi/olga/xin/Halophile_project/output/20160428/ICC_reads_taxa.txt"
	output1 = "/isi/olga/xin/Halophile_project/output/20160428/ICC_DS2_2_unmapped_reads_taxa.csv"
	output2 = "/isi/olga/xin/Halophile_project/output/20160428/ICC_DS2_2_unmapped_taxa_count.csv"
	reads = pd.read_csv(input1, header = None, names = ['read'])
	taxa = pd.read_csv(input2, header = None, names = ['id', 'read', 'taxa'], sep = '\t')
	overlap = pd.merge(reads, taxa, how = 'inner', on = 'read')
	taxacounts = overlap['taxa'].value_counts()
	overlap.to_csv(output1)
	taxacounts.to_csv(output2)
    
if __name__ == "__main__": main() 