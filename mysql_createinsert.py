import sys, getopt
from pymysql import connect, err, sys, cursors
import pandas as pd
from sqlfun_class import SQLfunc
def main(argv):
    inputdir = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print ("test.py -i <inputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ("test.py -i <inputfile>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputdir = arg
 
    #outputfile = open(outputdir, 'w')
    
   # df = pd.read_table(inputdir, header = None, names=['reads','seq'], delimiter = ' ')
    
#     sql = 'CREATE DATABASE IF NOT EXISTS rpoB_reads_assignment'
#     cursor.execute(sql))
    #sql = 'SELECT reads_name, sequence FROM reads_trimmed_merged.DS2_1_trimmed_merged_fa WHERE id < 100 AND SUBSTRING(reads_name, 2) NOT IN (SELECT reads_name from reads_assignment.DS2_1_assignment);'
    sqlfun = SQLfunc()
    sqlfun.create_seqdb("xchen_projects","ICW_trimmed_merged_fa",inputdir)
if __name__ == "__main__": main(sys.argv[1:]) 
