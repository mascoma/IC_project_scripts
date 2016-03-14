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
		inputfile = open(inputdir, 'r')
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
		outputfile = open(outputdir, 'w')
		df = pd.read_table(inputdir, header = None, names=['reads','ref'], delimiter = ' ')
		sql = 'USE ' + database + ';'
		cursor.execute(sql)
		for a in range(len(df['ref'])):
			
			df2 = (re.search("([A-Za-z_]+[0-9]+)",df['ref'][a])).group(1)
			sql = "SELECT cn.fun_class FROM cognames cn INNER JOIN coglist cl ON cn.COG_id = cl.COG_id INNER JOIN prot_refseq p ON cl.prot_id = p.prot_id WHERE p.refseq_acc = '" + df2 + "';"
			cursor.execute(sql)
			data = cursor.fetchall()
			if data: 
				cogclass = data[0]["fun_class"]
			#print(df['reads'][a] + data, file = outputfile)
				print >>  outputfile, df['reads'][a] + '\t' + cogclass
			else: 
				print >>  outputfile, df['reads'][a] + '\t' + "NULL"
		cursor.close()
		conn.close()


