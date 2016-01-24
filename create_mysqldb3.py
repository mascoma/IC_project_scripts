#!/usr/bin/env python3
# this script is to create a database for sequencing reads
from pymysql import connect, err, sys, cursors
import re
import pandas as pd
def main():
    conn = connect(host = '', 
           port = 3306,
           user = 'xchen',
           passwd = '008')     
    cursor = conn.cursor( cursors.DictCursor )
    sql = 'CREATE DATABASE IF NOT EXISTS reads_trimmed_merged'
    cursor.execute(sql)
    sql = 'USE reads_trimmed_merged'
    cursor.execute(sql)
    sql = """CREATE TABLE IF NOT EXISTS DS2_2_trimmed_merged_fq
    (
        id INT AUTO_INCREMENT NOT NULL,
        reads_name VARCHAR(255) NOT NULL,
        sequence VARCHAR(1200),
        PRIMARY KEY (id)
    )CHARSET=utf8""" 
    cursor.execute(sql)
    inputdir1 = '/Users/Xin/Desktop/IC_project/input/merged_reads_CLC/DS2_2_CLC.fastq'
    f = open(inputdir1,'r')
    tmp1 = []
    for line in f:
        if line.startswith("@M00704"):
            read = ''.join(tmp1)
            #print(read)
            tmp2 = re.search('(@M00704:49:000000000-AFW6D[\w\d\_\:\/\-]+)\n(.+)', read, re.DOTALL)
            if tmp2:
                reads_name = tmp2.group(1)
                seq = tmp2.group(2)
                #print(reads_name)
                #print(seq)
                sql = 'INSERT INTO DS2_2_trimmed_merged_fq (reads_name, sequence) VALUES('+'"'+reads_name+'"'+','+'"'+seq+'"'+')'
                #print(sql)
                try:
                    cursor.execute(sql)
                    conn.commit()
                except pymysql.err.ProgrammingError:
                    print(sql)
                
                
            tmp1 = []
            tmp1.append(line)
        else:
            tmp1.append(line)
            
    cursor.close()
    conn.close()
if __name__ == "__main__": main() 