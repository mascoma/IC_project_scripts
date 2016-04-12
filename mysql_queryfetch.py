import sys, getopt
from pymysql import connect, err, sys, cursors
import pandas as pd
from sqlfun_class import SQLfunc
def main(argv):
    inputfile = ''
    outputfile = ''
    # try:
    #     opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    # except getopt.GetoptError:
    #     print ("test.py -i <inputfile> -o <outputfile>")
    #     sys.exit(2)
    # for opt, arg in opts:
    #     if opt == '-h':
    #         print ("test.py -i <inputfile> -o <outputfile>")
    #         sys.exit()
    #     elif opt in ("-i", "--ifile"):
    #         inputfile = arg
    #     elif opt in ("-o", "--ofile"):
    #         outputfile = arg 

     
    try:
        opts, args = getopt.getopt(argv,"ho:",["ofile="])
    except getopt.GetoptError:
        print ("test.py -o <onputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ("test.py -o <onputfile>")
            sys.exit()
        elif opt in ("-o", "--ofile"):
            outputfile = arg

 
#     sql = 'CREATE DATABASE IF NOT EXISTS rpoB_reads_assignment'
#     cursor.execute(sql)
 
    #sql = 'SELECT reads_name, sequence FROM reads_trimmed_merged.DS2_1_trimmed_merged_fa WHERE id < 100 AND SUBSTRING(reads_name, 2) NOT IN (SELECT reads_name from reads_assignment.DS2_1_assignment);'
    sqlfun = SQLfunc()
    sqlfun.fetch_table3 ('xchen_projects', 'ICC_umapped_to_DS2_2', 'ICC_reads_COG_ncbidb', outputfile)
 
if __name__ == "__main__": main(sys.argv[1:]) 