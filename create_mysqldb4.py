#!/usr/bin/env python3
# this script is to create a database for the rpoB gene hits and taxa assignment
from pymysql import connect, err, sys, cursors
import pandas as pd
def main():
    inputdir1 = '/isi/olga/xin/Halophile_project/db_source/gi_taxid_prot.dmp'
#     inputdir2 = '/Users/Xin/Desktop/IC_project/output/01142016/DS2_1_rpoB_reads_taxa.csv'
#     outputdir = '/Users/Xin/Desktop/IC_project/output/01142016/DS2_1_rpoB_hits_taxa.csv'
    df1 = pd.read_table(inputdir1, header = None, names = ['gi','taxaid'] )
#     df2 = pd.read_csv(inputdir2)
#     df12 = pd.merge(df1, df2, on = 'read', how = 'outer')
#     df12.to_csv(outputdir)
    conn = connect(host = 'localhost', 
               user = 'xchen',
               passwd = 'f0029mc');
      
    cursor = conn.cursor( cursors.DictCursor );
  #  sql = 'CREATE DATABASE IF NOT EXISTS DS2_ICC_mapping'
  #  cursor.execute(sql)
    sql = 'USE xchen_general'
    cursor.execute(sql)

    for j in range(0, len(df1['gi'])):
        r1 = str(df1['gi'][j])
        t1 = str(df1['taxaid'][j])
        #print(r1)
        #print(t1)
        sql = 'INSERT INTO gi_taxaid (gi, taxaid) VALUES('+ r1 + ',' + t1 + ')'
        #sql = 'INSERT INTO ICC_DS2_1_CLC_unmapped (reads_name) VALUES('+"'"+r1+"'"+')'
        
        #print(sql)
        cursor.execute(sql)
        conn.commit()        
    cursor.close()
    conn.close()
if __name__ == "__main__": main() 
