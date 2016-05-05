import re 
import pandas as pd
import csv
def main(): 

	input1 = "/isi/olga/xin/Halophile_project/output/20160428/ICC_blx_gi_short.txt"	 
	output2 = "/isi/olga/xin/Halophile_project/output/20160428/ICC_blx_gi_single.txt"
	reads = pd.read_csv(input1, header = None, names = ['read']) 
	counts = reads['read'].value_counts()
	
	counts.to_csv(output2)
    
if __name__ == "__main__": main() 