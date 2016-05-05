import re 
import pandas as pd
import csv
def main(): 

	input1 = "/isi/olga/xin/Halophile_project/output/20160428/ICC_reads_taxa.txt"
	 
	output1 = "/isi/olga/xin/Halophile_project/output/20160429/ICC_taxa_count.txt"
	 
	reads = pd.read_csv(input1, header = None, names = ['id', 'read', 'taxa'], sep = '\t')
 
	taxacounts = reads['taxa'].value_counts()
	taxacounts.to_csv(output1)
    
if __name__ == "__main__": main() 