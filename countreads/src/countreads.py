#this script is to count the number of reads in a fastq file
import sys, getopt
def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print ("test.py -i <inputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ("test.py -i <inputfile>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
    count1 = 0
#     try:
    f = open(inputfile, 'r')
    print("successful open!")
    for line in f:      
        if line.startswith('@M00704'):       
            count1 = count1 + 1  
    print("Total number of reads is : ", count1)                
#      except IOError:
#         print ("no such file!")                   
if __name__ == "__main__": main(sys.argv[1:]) 