#!/usr/bin/env python3
# this script is to create a database for the rpoB gene hits and taxa assignment
from pymysql import connect, err, sys, cursors
import pandas as pd
def main():
    inputdir1 = '/Users/Xin/Desktop/IC_project/output/Jan202016/ICC_DS2_1_CLC_unmapped.csv'
#     inputdir2 = '/Users/Xin/Desktop/IC_project/output/01142016/DS2_1_rpoB_reads_taxa.csv'
#     outputdir = '/Users/Xin/Desktop/IC_project/output/01142016/DS2_1_rpoB_hits_taxa.csv'
    df1 = pd.read_csv(inputdir1)
#     df2 = pd.read_csv(inputdir2)
#     df12 = pd.merge(df1, df2, on = 'read', how = 'outer')
#     df12.to_csv(outputdir)
    conn = connect(host = '', 
               port = 3306,
               user = 'xchen',
               passwd = '008');
      
    cursor = conn.cursor( cursors.DictCursor );
    sql = 'CREATE DATABASE IF NOT EXISTS DS2_ICC_mapping'
    cursor.execute(sql)
    sql = 'USE DS2_ICC_mapping'
    cursor.execute(sql)
    sql = """CREATE TABLE IF NOT EXISTS ICC_DS2_1_CLC_unmapped
    (
        id INT AUTO_INCREMENT NOT NULL,
        reads_name VARCHAR(255) NOT NULL,
        PRIMARY KEY (id)
    )CHARSET=utf8""" 
    cursor.execute(sql)
    for j in range(0, len(df1['read'])):
        r1 = df1['read'][j]
        #t1 = df1['taxa'][j]
        #print(r1)
        #print(t1)
        #sql = 'INSERT INTO DS2_1_rpoB_reads (reads_name, taxa) VALUES('+"'"+r1+"'"+','+"'"+t1+"'"+')'
        sql = 'INSERT INTO ICC_DS2_1_CLC_unmapped (reads_name) VALUES('+"'"+r1+"'"+')'
        
        #print(sql)
        cursor.execute(sql)
        conn.commit()        
    cursor.close()
    conn.close()
if __name__ == "__main__": main() 