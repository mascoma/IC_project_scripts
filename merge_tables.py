import re 
import pandas as pd
import csv
def main(): 

	input1 = "/isi/olga/xin/Halophile_project/output/20160503/cog_hits_parse_cut.txt"
	input2 = "/isi/olga/xin/Halophile_project/output/20160503/ICC_qgi_coggi.txt"
	input3 = "/isi/olga/xin/Halophile_project/output/20160504/ICC_blx_k5.m8"
	output = "/isi/olga/xin/Halophile_project/output/20160505/ICC_reads_cog_all.csv"
	cog = pd.read_csv(input1, sep = '\t')
	gi = pd.read_csv(input2, header = None, names = ['qid', 'prot_id'], sep = '\t')
	reads = pd.read_csv(input3, header = None, names = ['reads', 'qid', 'percent', 'align_len', 
		'mismatches', 'gap', 'qstart', 'qend', 'sstart', 'send', 'e', 'bit_score'], sep = '\t')
	reads_filter = reads[reads['e'] < 0.000001]
	jointable1 = pd.merge(cog, gi, how = 'outer', on = 'prot_id')
	jointable2 = pd.merge(jointable1, reads_filter, how = 'inner', on = 'qid')
	jointable2.to_csv(output)
    
if __name__ == "__main__": main() 