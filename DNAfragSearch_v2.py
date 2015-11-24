#!/usr/bin/python3
# DNAfragsearch.py by Xin Chen
# 09/9/2015
# search for a short fragments in sequences files, return the counts, and positions
# setup input and output files using -i and -o
# type in the string need to be checked
import re, io, sys, getopt
import matplotlib.pyplot as plt
# this script is to search and count certain DNA fragments in reads collections and plot the distribution of the fragments 
# in the reads
import numpy as np
def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ("test.py -i <inputfile> -o <outputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ("test.py -i <inputfile> -o <outputfile>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    count1 = 0
    sp = []
    output = open(outputfile, 'w')
    print('Start\tend\n', file = output, end = '\n')
    try:
        f = open(inputfile, 'r')
        print("successful open!")
        fragment = input("Enter the string you want to search: ")
        for line in f:             
            index = (re.finditer(fragment,line,re.IGNORECASE))                   
            for string in index:
                count1 = count1 + 1
                startPosition = str(string.start())
                sp.append(string.start())
                endPosition = string.end()
                print(startPosition,'\t',endPosition, file = output, end = '\n')
        print("The total count of " + fragment + " is " + str(count1))  
    
        plt.hist(sp, bins=range(min(sp), max(sp) + 2, 1))
        tital = input("Enter the tital of the graph: ")
        plt.title(tital + " (counts = " + str(count1) +")")
        plt.xlabel("Position")
        plt.ylabel("Frequency")
        plt.savefig("indexSeqPos_" + outputfile + ".png")
 
    except IOError:
            print ("no such file!")          
if __name__ == "__main__": main(sys.argv[1:])      