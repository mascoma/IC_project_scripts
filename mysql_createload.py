import sys, getopt
from pymysql import connect, err, sys, cursors
import pandas as pd
from sqlfun_class import SQLfunc
def main():
 
#     sql = 'CREATE DATABASE IF NOT EXISTS rpoB_reads_assignment'
#     cursor.execute(sql)
    #sql = 'SELECT reads_name, sequence FROM reads_trimmed_merged.DS2_1_trimmed_merged_fa WHERE id < 100 AND SUBSTRING(reads_name, 2) NOT IN (SELECT reads_name from reads_assignment.DS2_1_assignment);'
    sqlfun = SQLfunc()
    sqlfun.create_table('xchen_general', 'prot_refseq', 'prot_id INT, refseq_acc VARCHAR(100), PRIMARY KEY (refseq_acc)', '/isi/olga/xin/Halophile_project/db_source/prot2003-2014.tab', '\\t')
 
if __name__ == "__main__": main() 