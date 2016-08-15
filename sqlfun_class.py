#!/usr/bin/python3
import sys, getopt
from pymysql import connect, err, sys, cursors
import pandas as pd
import re
class SQLfunc:
	global conn, cursor;
	conn = connect(host = 'localhost', 
               user = 'xchen',
               passwd = 'f0029mc');
	cursor = conn.cursor( cursors.DictCursor );
	def help(self, string):
		if (string is 'methods'):
			print("""def create_table(self, database, tablename,columns ,filedir, delimiter)
					def create_seqdb (self, database, tablename, inputhandle)
					def cell_replacment(self, database, tablename, column1, column2, replace, condition)
					def fetch_seq(self, database, table1, table2, string, outputfile)
					def fetch_table1(self, database, df, outputfile)
					def fetch_table2(self, database, outputfile) """)

		if (string is 'create_table'):
			print (""" example: 
				   sql = 'CREATE TABLE IF NOT EXISTS '+ tablename+' ('+tablestr +')CHARSET=utf8;'
				   CREATE TABLE IF NOT EXISTS coglist
					( 
						domain_id INT,
						genome VARCHAR(100),
						prot_id INT,
						prot_len INT,
						domain_start INT,
						domain_end INT,
						COG_id VARCHAR(30),
						membership_class INT,
						PRIMARY KEY (domain_id),
						FOREIGN KEY (prot_id)  REFERENCES prot_refseq(prot_id),	
						FOREIGN KEY (COG_id)  REFERENCES cognames(COG_id)
					)  CHARSET=utf8;
					sql = "LOAD DATA LOCAL INFILE '" + filedir + "' INTO TABLE " + tablename + " COLUMNS TERMINATED BY '"+ delimiter+"' ;" 
					LOAD DATA LOCAL INFILE '/isi/olga/xin/Halophile_project/db_source/names.dmp'
						INTO TABLE taxa_id_name
						COLUMNS TERMINATED BY '|'; """)

		if (string is 'createseqdb'):
			print ("""example:
					sql = 'CREATE TABLE IF NOT EXISTS '+tablename+' (id INT AUTO_INCREMENT NOT NULL,reads_name VARCHAR(255) NOT NULL,sequence VARCHAR(1200),PRIMARY KEY (id))CHARSET=utf8;'
					sql = 'INSERT INTO' + tablename + '(reads_name, sequence) VALUES('+"'"+reads_name+"'"+','+"'"+seq+"'"+')' # reads_name and seq are two columns in the inputfile """)

		if (string is 'cell_replacement'):
			print ("""example: 
					sql = 'UPDATE ' + tablename + ' SET ' + colunm1 + " = '" + replace + "' WHERE " + column2+ " = '" + condition + "';"
					sql = 'UPDATE DS2_1_reads_taxapath_megan SET taxapath = ' + "'" + df2['taxapath'][j]+ "' " + 'WHERE reads_name = ' + "'" + df2['read'][j]+ "';" """)

		if (string is 'fetch_seq'):
			print ("""example:
					sql = 'SELECT ' + + ' FROM ' + table1 + ' WHERE SUBSTRING (reads_name, 2) IN (SELECT reads_name FROM ' + table2 + ' WHERE ' + + " LIKE '%" + string + "%' );"  
					sql = 'SELECT reads_name, sequence FROM ICC_trimmed_merged_fa WHERE SUBSTRING(reads_name, 2) IN (SELECT reads_name FROM ICC_reads_taxapath_megan WHERE taxapath LIKE '+"'%" + 'Halorubrum;'+ "%'" +');' """)

		if (string is 'fetch_table1'):
			print("""example:
					sql = 'SELECT t.* FROM gi_taxaid g INNER JOIN taxa_id_name t ON g.taxaid = t.tax_id WHERE g.gi =' + str(a) + 'AND t.name_class LIKE '+ "'%"+ 'scientific name' + "%';"
					SELECT t.* FROM gi_taxaid g INNER JOIN taxa_id_name t ON g.taxaid = t.tax_id WHERE g.gi = 374428416 AND t.name_class LIKE '%  scientific name%'; """)

		if (string is 'fetch_table2'):
			print("""example:
					sql = 'SELECT cn.fun_class FROM cognames cn INNER JOIN coglist cl ON cn.COG_id = cl.COG_id INNER JOIN prot_refseq p ON cl.prot_id = p.prot_id WHERE p.refseq_acc = ' + df2 + ';' """)

	def create_table(self, database, tablename,columns ,filedir, delimiter):
		sql = 'USE ' + database + ';'
		cursor.execute(sql)
		sql = 'CREATE TABLE IF NOT EXISTS '+ tablename+' ('+columns +')CHARSET=utf8;'
		print(sql)
		cursor.execute(sql)
		sql = "LOAD DATA LOCAL INFILE '" + filedir + "' INTO TABLE " + tablename + " COLUMNS TERMINATED BY '"+ delimiter+"' ;"  # seems LOAD command is not allowned for this version of pymysql package? 
		print(sql)
		cursor.execute(sql)
		conn.commit()
		cursor.close()
		conn.close()

	def create_seqdb (self, database, tablename, inputdir):
    # this function is to create a table contain sequences (from fasta format)
		sql = 'USE ' + database + ';'
		cursor.execute(sql)
		sql = 'CREATE TABLE IF NOT EXISTS '+tablename+' (id INT AUTO_INCREMENT NOT NULL,reads_name VARCHAR(255) NOT NULL,sequence VARCHAR(1200),PRIMARY KEY (id))CHARSET=utf8;'
		cursor.execute(sql)
		tmp1=[]
		inputhandle = open(inputdir, 'r')
		for line in inputhandle:
			if line.startswith(">"):
				read = ''.join(tmp1)
				tmp2 = re.search('(>M00704:49:000000000-AFW6D[\w\d\_\:\/\-]+)\t([\w\-]+)', read)
				if tmp2:
					reads_name = tmp2.group(1)
					seq = tmp2.group(2)
					sql = 'INSERT INTO ' + tablename + '(reads_name, sequence) VALUES('+"'"+reads_name+"'"+','+"'"+seq+"'"+')'
					cursor.execute(sql)
					conn.commit()
				tmp1 = []
				tmp1.append("\n"+line.rstrip('\n')+"\t")
			else:
				tmp1.append(line.rstrip('\n'))
		read = ''.join(tmp1)
		tmp2 = re.search('(>M00704:49:000000000-AFW6D[\w\d\_\:\/\-]+)\t([\w\-]+)', read)
		if tmp2:
			reads_name = tmp2.group(1)
			seq = tmp2.group(2)
			sql = 'INSERT INTO ' + tablename + '(reads_name, sequence) VALUES('+"'"+reads_name+"'"+','+"'"+seq+"'"+')'
			cursor.execute(sql)
			conn.commit()
		cursor.close()
		conn.close()


	def create_seqdb2 (self, database, tablename, inputdir):
    # this function is to create a table contain sequences (from fasta format)
		sql = 'USE ' + database + ';'
		cursor.execute(sql)
		sql = 'CREATE TABLE IF NOT EXISTS '+tablename+' (id INT AUTO_INCREMENT NOT NULL,reads_name VARCHAR(255) NOT NULL,sequence VARCHAR(1200),PRIMARY KEY (id))CHARSET=utf8;'
		cursor.execute(sql)
		tmp1=[]
		inputhandle = open(inputdir, 'r')
		for line in inputhandle:
			if line.startswith(">"):
				read = ''.join(tmp1)
				tmp2 = re.search('(>FU0WOVM01[\w\d]+)\t([\w\-]+)', read)
				if tmp2:
					reads_name = tmp2.group(1)
					seq = tmp2.group(2)
					sql = 'INSERT INTO ' + tablename + '(reads_name, sequence) VALUES('+"'"+reads_name+"'"+','+"'"+seq+"'"+')'
					cursor.execute(sql)
					conn.commit()
				tmp1 = []
				tmp1.append("\n"+line.rstrip('\n')+"\t")
			else:
				tmp1.append(line.rstrip('\n'))
		read = ''.join(tmp1)
		tmp2 = re.search('(>FU0WOVM01[\w\d]+)\t([\w\-]+)', read)
		if tmp2:
			reads_name = tmp2.group(1)
			seq = tmp2.group(2)
			sql = 'INSERT INTO ' + tablename + '(reads_name, sequence) VALUES('+"'"+reads_name+"'"+','+"'"+seq+"'"+')'
			cursor.execute(sql)
			conn.commit()
		cursor.close()
		conn.close()	

	def cell_replacment(self, database, tablename, column1, column2, replace, condition): # this function is to replace the content of certain cells given the condition
		sql = 'USE ' + database + ';'
		cursor.execute(sql)
		sql = 'UPDATE ' + tablename + ' SET ' + colunm1 + " = '" + replace + "' WHERE " + column2+ " = '" + condition + "';"
		cursor.execute(sql)
		conn.commit()
		cursor.close()
		conn.close()

	def fetch_seq_include(self, database, table1, table2, string, outputfile):# this function is to fetch sequences using a query string, table1 contains sequences, 
		sql = 'USE ' + database + ';'
		cursor.execute(sql)
		sql = 'SELECT ' + + ' FROM ' + table1 + ' WHERE SUBSTRING (reads_name, 2) IN (SELECT reads_name FROM ' + table2 + ' WHERE ' + + " LIKE '%" + string + "%' );"
		cursor.execute(sql)
		data = cursor.fetchall()
		cursor.close()
		conn.close()
		print("almost done!")
		df = pd.DataFrame(data)
		for i in range(len(df['reads_name'])):
			#print(df['reads_name'][i]+ '\n'+ df['sequence'][i], file = outputfile, end = '\n')
			print >> outputfile, df['reads_name'][i]+ '\n' + df['sequence'][i]
 

	def fetch_seq_exclude(self, database, table1, table2, outputdir):
		sql = 'USE ' + database + ';'
		cursor.execute(sql)
		sql = 'SELECT *' + ' FROM ' + table1 + ' WHERE SUBSTRING(reads_name, 2) NOT IN (SELECT reads_name FROM ' + table2  +");"
		cursor.execute(sql)
		data = cursor.fetchall()
		cursor.close()
		conn.close()
		print("almost done!")
		outputfile = open(outputdir, 'w')
		df = pd.DataFrame(data)
		for i in range(len(df['reads_name'])):
			#print(df['reads_name'][i]+ '\n'+ df['sequence'][i], file = outputfile, end = '\n')
			print >> outputfile, df['reads_name'][i]+ '\n' + df['sequence'][i]
	 

	def fetch_table1(self, database, df, outputfile): # this function is to fetch taxa id from two tables given the gi number
		sql = 'USE ' + database + ';'
		cursor.execute(sql)
		for a in range(len(df['gi'])):
			sql = 'SELECT t.* FROM gi_taxaid g INNER JOIN taxa_id_name t ON g.taxaid = t.tax_id WHERE g.gi =' + str(a) + 'AND t.name_class LIKE '+ "'%"+ 'scientific name' + "%';"
			cursor.execute(sql)
			data = cursor.fetchall()
			#print(df['reads'][a] + df['gi'][a] + data, file = outputfile)
			print >> outputfile, df['reads'][a] + df['gi'][a] + data
		cursor.close()
		conn.close()

	def fetch_table2(self, database, inputdir, outputdir): # this function is to fetch COG class from three tables given the refseq 
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
			df3 = df3.append(df4)
		df3.to_csv(outputdir, sep = '\t')
		cursor.close()
		conn.close()


	def fetch_table3(self, database, table1, table2, outputdir): # this function is to fetch reads in ICC_DS2 dataset with KEGG or SEEDS assignment 
		# table1 ICC_DS2_1 query table;
		# table2 kegg/seed path/cog table;
		sql = 'USE ' + database + ';'
		cursor.execute(sql)
		sql =  "SELECT t2.reads_name, t2.cog FROM " + table1 + " AS t1 CROSS JOIN " + table2 + " AS t2 ON SUBSTRING(t1.reads_name, 2) = t2.reads_name;"  
		cursor.execute(sql)
		data = cursor.fetchall()
		df = pd.DataFrame(data)
		df.to_csv(outputdir, sep = '\t', header = False) 
		cursor.close()
		conn.close()

	def fetch_table4(self, database, table, outputdir): # this function is to fetch entire table
		# table ICC_reads_taxa;
		  
		sql = 'USE ' + database + ';'
		cursor.execute(sql)
		sql =  "SELECT * FROM " + table + ";"  
		cursor.execute(sql)
		data = cursor.fetchall()
		df = pd.DataFrame(data)
		df.to_csv(outputdir, sep = '\t', header = False) 
		cursor.close()
		conn.close()

	 