#!/usr/bin/python3
# this script is show an example of using class to filter out certain reads
# cluster version - input the arguments in the order as the directory of 
# the reads collection file, the reads filter file and the directory of the output file
import sys, getopt
import csv
import re
from subsampling_class import Subsampling  # import the class subsampling_class
def main(argv):
    if len(argv[1:]) == 3:
        input1dir = argv[1]
        input2dir = argv[2]
        outputdir = argv[3]
    else:
        print("Three arguements are needed!!")
    output = open(outputdir, 'w')
    try:
        all_reads = open(input1dir, 'r')
    except IOError:
        print ("no such file!") 
    readslist = []
    with open(input2dir, 'r') as inputfile:
        f = csv.DictReader(inputfile)
        for row in f:
            readslist.append(row['read']) # all the reads
        print("total reads in filter list:", len(readslist)) 
        subset = Subsampling()  
        subset.include_fq(all_reads, readslist, output)
    
if __name__ == "__main__": main(sys.argv)
