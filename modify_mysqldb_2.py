#!/usr/bin/env python3

from pymysql import connect, err, sys, cursors
import pandas as pd

def main():
    inputdir2 = '/Users/Xin/Desktop/IC_project/output/01132016/DS2_1_pb_taxa_replace.csv'
    df2 = pd.read_csv(inputdir2)
    conn = connect(host = '', 
               port = 3306,
               user = 'xchen',
               passwd = '008');
    
    cursor = conn.cursor( cursors.DictCursor );
    sql = 'USE reads_assignment'
    cursor.execute(sql)
    
    for j in range(0, len(df2['read'])):
        sql = 'UPDATE DS2_1_assignment SET taxa = ' + "'" + df2['taxa1'][j]+ "' " + 'WHERE reads_name = ' + "'" + df2['read'][j]+ "';"
        cursor.execute(sql)
        conn.commit()
    #print(j)
    #sql = 'RENAME TABLE DS2_1_assignment TO DS2_1_assignment'
    #cursor.execute(sql)
    sql = '''SELECT * 
            FROM DS2_1_assignment 
            INTO OUTFILE "/tmp/DS2_1_assignment_new.csv"
            FIELDS TERMINATED BY ','
            ENCLOSED BY '"'
            LINES TERMINATED BY '\n'''
    
    cursor.execute(sql)
    cursor.close()
    conn.close()
    
if __name__ == "__main__": main() 