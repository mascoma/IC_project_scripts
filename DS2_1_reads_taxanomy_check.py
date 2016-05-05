import sys, getopt
from pymysql import connect, err, sys, cursors
import pandas as pd
def main():	
	conn = connect(host = 'localhost', user = 'xchen', passwd = 'f0029mc');
	cursor = conn.cursor( cursors.DictCursor );
	sql = 'USE xchen_projects;'
	cursor.execute(sql)
	sql = 'SELECT t1.reads_name, t1.taxapath FROM DS2_1_reads_taxapath_megan t1 WHERE t1.reads_name NOT IN (SELECT t2.reads_name FROM DS2_1_reads_taxa_megan t2);'
	cursor.execute(sql)
	data = cursor.fetchall()
	cursor.close()
	conn.close()
	df = pd.DataFrame(data)
 	df.to_csv("/isi/olga/xin/Halophile_project/output/20160413/extra_reads_DS2_1.csv")
if __name__ == "__main__": main() 