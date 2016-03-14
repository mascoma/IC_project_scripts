#this script is to count the number of hits to the reference sequences without gi number. this customer database for diamond
#includes nr and halophile genomes. The faa file for a few species were generated from RAST, thus those genome reference sequences
#don't have regular gi number, instead have a ncbi taxon id with "fig" string in the front. 
#!/usr/bin/python
import re, sys, getopt

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
    count2 = 0
    countline = 0
    sp = []
    output = open(outputfile, 'w')
#     try:
    f = open(inputfile, 'r')
    print("successful open!")
    for line in f:
        countline = countline + 1             
        index = (re.search("gi|",line))  
        if not index :  
            count1 = count1 + 1  
            print >> output, line
        elif index : 
            count2 = count2 + 1

    print("The number of hits matching sequences with fig taxon id is ", count1)
    print("The number of hits matching sequences with gi number  is ",count2) 
    print("Total number of hits is ",countline)            
#      except IOError:
#         print ("no such file!")          
        
            
            
            
if __name__ == "__main__": main(sys.argv[1:]) 
