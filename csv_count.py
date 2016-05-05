import pandas as pd
import sys, getopt
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
    df1 = pd.read_csv(inputfile, header = None, names = ["col1"], sep = ' ')
    taxa_count1 = df1['col1'].value_counts()
    taxa_count1.to_csv(outputfile)
 

if __name__ == "__main__": main(sys.argv[1:]) 
