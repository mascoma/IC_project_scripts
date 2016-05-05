import sys, getopt
from pymysql import connect, err, sys, cursors
import pandas as pd
def main():	
	outputfile = open("/isi/olga/xin/Halophile_project/output/20160413/ICC_DS2_2_unmapped_unassigned_taxa.fa", 'w')
	conn = connect(host = 'localhost', user = 'xchen', passwd = 'f0029mc');
	cursor = conn.cursor( cursors.DictCursor );
	sql = 'USE xchen_projects;'
	cursor.execute(sql)
	sql = 'SELECT t1.reads_name, sequence FROM ICC_umapped_to_DS2_2_fa t1 WHERE SUBSTRING(t1.reads_name, 2) NOT IN (SELECT t2.reads_name FROM ICC_reads_taxapath_megan t2);'
	cursor.execute(sql)
	data = cursor.fetchall()
	cursor.close()
	conn.close()
	df = pd.DataFrame(data)
	for i in range(len(df['reads_name'])):	 
		print >> outputfile, df['reads_name'][i]+ '\n' + df['sequence'][i]
if __name__ == "__main__": main() 





