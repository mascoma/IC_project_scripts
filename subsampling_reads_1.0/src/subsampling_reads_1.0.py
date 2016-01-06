#!/usr/bin/python3
# this script is show an example of using class to filter out certain reads
# PC version
import csv
from subsampling_class import Subsampling  # import the class subsampling_class
def main():
    input1dir = input('Reads collections: ')
    input2dir = input('Reads filter: ')
    outputdir = input('Output file: ')
    output = open(outputdir, 'w')
    try:
        all_reads = open(input1dir, 'r')
    except IOError:
        print ("no such file!") 
    readslist = []
    with open(input2dir, 'r') as inputfile:
        f = csv.DictReader(inputfile, delimiter =",", fieldnames=['reads','genus'])
        for row in f:
            readslist.append(row['reads']) # all the reads
        print("total reads in filter list:", len(readslist)) 
        subset = Subsampling()  
        subset.exclude(all_reads, readslist, output)
    
if __name__ == "__main__": main()