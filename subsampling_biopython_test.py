#!/usr/bin/python3
# this script is show an example of using class to filter out certain reads
# cluster version - input the arguments in the order as the directory of 
# the reads collection file, the reads filter file and the directory of the output file
import sys, getopt
import csv
import re
import time
from subsampling_class_biopython import Subsampling  # import the class subsampling_class

def main(argv):
    start_time = time.clock()
    if len(argv[1:]) == 3:
        inputdir1 = argv[1]
        inputdir2 = argv[2]
        outputdir = argv[3]
    else:
        print("Three arguements are needed!!")
    readslist = []
    with open(inputdir2, 'r') as inputfile:
        f = csv.DictReader(inputfile, delimiter =",", fieldnames=['id','reads','taxa'])
        for row in f:
            readslist.append(row['reads']) # all the reads
        print("total reads in filter list:", len(readslist)) 
        subset = Subsampling()  
        subset.exclude_seq(inputdir1, "fasta", readslist, outputdir)
    print time.clock() - start_time, "seconds"
if __name__ == "__main__": main(sys.argv)