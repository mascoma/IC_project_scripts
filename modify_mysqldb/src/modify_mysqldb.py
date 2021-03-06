#!/usr/bin/env python3

from pymysql import connect, err, sys, cursors
import pandas as pd

def main():
    inputdir2 = '/Users/Xin/Desktop/IC_project/output/01132016/ICC_pb_taxa_replace.csv'
    df2 = pd.read_csv(inputdir2)
    conn = connect(host = 'localhost', 
 
               user = 'xchen',
               passwd = 'f0029mc');
    
    cursor = conn.cursor( cursors.DictCursor );
    sql = 'USE xchen_projects'
    cursor.execute(sql)
    
    for j in range(0, len(df2['read'])):
        sql = 'UPDATE DS2_1_reads_taxapath_megan SET taxapath = ' + "'" + df2['taxapath'][j]+ "' " + 'WHERE reads_name = ' + "'" + df2['read'][j]+ "';"
        cursor.execute(sql)
        conn.commit()
        #print(j)
    #sql = 'RENAME TABLE DS2_1_assignment TO ICC_assignment'
    #cursor.execute(sql)
#     sql = '''SELECT * 
#             FROM ICC_assignment 
#             INTO OUTFILE "/tmp/ICC_assignment_new.csv"
#             FIELDS TERMINATED BY ','
#             ENCLOSED BY '"'
#             LINES TERMINATED BY '\n'''
#     
#     cursor.execute(sql)
    cursor.close()
    conn.close()
    
if __name__ == "__main__": main() 