#this script is to count the number of the reads and extract the number (name) of each read from reads collection (fasta file)
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
    output = open(outputfile, 'w')
#     try:
    f = open(inputfile, 'r')
    print("successful open!")
    for line in f:      
        if line.startswith('>'):        
            index = (re.search(">(M00704[\d\w\-\:]+)",line))  
            count1 = count1 + 1  
            name = index.group(1)
            print(name, file = output, end = "\n") 
    print(count1)                
#      except IOError:
#         print ("no such file!")                   
if __name__ == "__main__": main(sys.argv[1:]) 