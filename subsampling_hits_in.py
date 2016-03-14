#!/usr/bin/python3
# this script is to filter out the reads in the csv reads list
# the arguments are in the order of arg1= hits file, arg2 =  reads filter, arg3 = output

import sys, getopt

import re 
import csv
def main(argv):
    if len(argv[1:]) == 3:
        input1dir = argv[1]
        input2dir = argv[2]
        outputdir = argv[3]
    else:
        print("Three arguements are needed!!")
    output = open(outputdir, 'w')
    try:
        all_hits = open(input1dir, 'r')
    except IOError:
        print ("no such file!") 
    readslist = []
    with open(input2dir, 'r') as inputfile:
        f = csv.DictReader(inputfile, delimiter =",", fieldnames=['reads','taxa'])
        for row in f:
            readslist.append(row['reads']) # all the reads
        print("total reads:", len(readslist))    
        for line in all_hits: 
            tmp = re.search("(M00704:49:000000000-AFW6D[\w\d\_\:\/\-]+)\s", line)
            if tmp:
                readname=tmp.group(1)
                if readname in readslist:
                    print >> output, line  
 
if __name__ == "__main__": main(sys.argv) 


    
