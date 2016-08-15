#!/usr/bin/python3
import sys, getopt
from pymysql import connect, err, sys, cursors
import pandas as pd
import re
class Subsampling:
	global conn, cursor;
	conn = connect(host = 'localhost', 
               user = 'xchen',
               passwd = 'f0029mc');
	cursor = conn.cursor( cursors.DictCursor );

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

	def create_table(self, database, tablename,columns ,filedir, delimiter):
		sql = 'USE ' + database + ';'
		cursor.execute(sql)
		sql = 'CREATE TABLE IF NOT EXISTS '+ tablename+' ('+columns +')CHARSET=utf8;'
		cursor.execute(sql)
		sql = 'LOAD DATA LOCAL INFILE ' + "'" + filedir + "'" + ' INTO TABLE ' + tablename + ' COLUMNS TERMINATED BY' + "'" + delimiter+ "'" + ';'  # seems LOAD command is not allowed for this version of pymysql package? 
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

