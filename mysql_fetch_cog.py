import sys, getopt
from pymysql import connect, err, sys, cursors
import pandas as pd
import re		
def main():
	conn = connect(host = 'localhost', 
        user = 'xchen',
        passwd = 'f0029mc');
	cursor = conn.cursor( cursors.DictCursor );
	inputdir = "/isi/olga/xin/Halophile_project/output/20160503/cog_hits_gilist.txt"
	outputdir = "/isi/olga/xin/Halophile_project/output/20160503/cog_hits_parse.txt"
	df = pd.read_table(inputdir, header = None, names=['gi'], delimiter = ',')
	sql = 'USE xchen_general;'
	cursor.execute(sql)
	df3 = pd.DataFrame(columns = ["COG_annotate", "COG_id", "domain_end" ,"domain_start", "fun_class", "genome", "membership_class", "prot_id", "prot_len"])
	for a in range(len(df['gi'])):
		
		gi = df.iloc[a, 0]
		sql = "SELECT t1.prot_id,t1.genome, t1.prot_len, t1.domain_start, t1.domain_end, t1.membership_class, t2.COG_id, t2.fun_class, t2.COG_annotate FROM coglist AS t1 CROSS JOIN cognames AS t2 ON t1.COG_id = t2.COG_id WHERE t1.prot_id ='" + str(gi) + "';"
		cursor.execute(sql)
		data = cursor.fetchall()
		if data:
			df4 = pd.DataFrame(data)
			#print(df['reads'][a] + data, file = outputfile)
		else:
			sql = "SELECT t1.prot_id, t1.genome, t1.prot_len, t1.domain_start, t1.domain_end, t1.membership_class, COG_id FROM coglist AS t1 WHERE t1.prot_id ='" + str(gi) + "';"
			cursor.execute(sql)
			data = cursor.fetchall()
			df4 = pd.DataFrame(data)
		print a
		df3 = df3.append(df4)
	df3.to_csv(outputdir, sep = '\t')
	cursor.close()
	conn.close()
if __name__ == "__main__": main(sys.argv[1:]) 