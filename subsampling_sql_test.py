import sys, getopt
from pymysql import connect, err, sys, cursors
import pandas as pd
import time
from subsampling_class_sql import Subsampling
def main(argv):
    start_time = time.clock()
    if len(argv[1:]) == 3:
        input1dir = argv[1]
        input2dir = argv[2]
        outputdir = argv[3]
    else:
        print("Three arguements are needed!!")
    subset = Subsampling()
    start_time = time.clock()
    subset.create_seqdb("xchen_general", "ICC_seq_test", input1dir)
    #subset.create_table("xchen_general", "ICC_reads_test", "id INT, reads_name VARCHAR(255) NOT NULL, taxa VARCHAR(255), PRIMARY KEY (reads_name)", 
    #    input2dir, ",") ## load not supported by pymysql
    #subset.fetch_seq_exclude("xchen_general", "ICC_seq_test", "ICC_reads_test", outputdir)
    print time.clock() - start_time, "seconds"
if __name__ == "__main__": main(sys.argv) 
