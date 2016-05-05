import re 
import pandas as pd
import csv
def main(): 

	input1 = "/isi/olga/xin/Halophile_project/output/20160429/halo_allheader1.txt"
	input2 = "/isi/olga/xin/Halophile_project/output/20160429/nr_header1.txt"
	output1 = "/isi/olga/xin/Halophile_project/output/20160429/dup_seqid.txt"
 
	halo_id = pd.read_csv(input1, header = None, names = ['seq_id'], sep = ';')
	nr_id = pd.read_csv(input2, header = None, names = ['seq_id'], sep = ';')
	overlap = pd.merge(halo_id, nr_id, how = 'inner', on = 'seq_id')
	overlap.to_csv(output1)
 
    
if __name__ == "__main__": main() 