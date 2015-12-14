# this script is to extract reads name and gi numbers of reference sequences; and using gi number to fetch taxonomy name 
# of the reference sequences
import re 
import sys, getopt
from Bio import Entrez
Entrez.email = 'chenx1122@gmail.com'
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
    output = open(outputfile, 'w')
    input = open(inputfile, 'r')
    print("successful open!")
    for line in input:
        index1 = re.search("(M00704:49:000000000-AFW6D[\d\:\w\/\_\-]+)\t", line)
        index2 = re.search("gi\|(\d+)\|", line)
        reads = index1.group(1)
        gi = index2.group(1)
        print(gi)
        handle = Entrez.efetch(db ="nucleotide", id = gi, retmode="xml") # id number is the ncbi gi number
        record = Entrez.read(handle)
        handle.close()
        taxonomy = record[0]["GBSeq_organism"]
        if taxonomy:
            index =  re.search("^(\w+)\s(\w+)", taxonomy)
            if index:
                genus = index.group(1)
                species = index.group(2)
                print(reads,",",gi,",",genus,",",species,",", taxonomy,file = output, end = '\n')
                
            else:
                genus = "NA"
                species = "NA"
                print(reads,",",gi,",",genus,",",species,",", taxonomy,file = output, end = '\n')
        else:
            taxonomy = "NA"
            genus = "NA"
            species = "NA"
            print(reads,",",gi,",",genus,",",species,",", taxonomy,file = output, end = '\n')

if __name__ == "__main__": main(sys.argv[1:]) 
