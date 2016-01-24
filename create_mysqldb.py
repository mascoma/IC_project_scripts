#!/usr/bin/env python3

from pymysql import connect, err, sys, cursors
import pandas as pd
def main():
    inputdir1 = '/Users/Xin/Desktop/IC_project/output/Jan202016/ICC_read_species.csv'
    df1 = pd.read_csv(inputdir1)
    conn = connect(host = '', 
               port = 3306,
               user = 'xchen',
               passwd = '008');
    
    cursor = conn.cursor( cursors.DictCursor );
    #sql = 'CREATE DATABASE IF NOT EXISTS reads_assignment'
    #cursor.execute(sql)
    sql = 'USE reads_assignment'
    cursor.execute(sql)
    sql = """CREATE TABLE IF NOT EXISTS ICC_species_assignment
    (
        id INT AUTO_INCREMENT NOT NULL,
        reads_name VARCHAR(255) NOT NULL,
        taxa VARCHAR(255),
        PRIMARY KEY (id)
    )CHARSET=utf8""" 
    cursor.execute(sql)
    for i in range(0, len(df1['read'])):
        r = df1['read'][i]
        t = df1['taxa'][i]
        sql = 'INSERT INTO ICC_species_assignment (reads_name, taxa) VALUES('+"'"+r+"'"+','+"'"+t+"'"+');'
        #print(sql)
        cursor.execute(sql)
        conn.commit()
    cursor.close()
    conn.close()
if __name__ == "__main__": main() 