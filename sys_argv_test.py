#this script is to count the number of reads in a fastq file
import sys, getopt
import re
def main(argv):
    print(len(argv[1:]))
    print(argv[1])
    dir1 = argv[1]
    input1dir = dir1
    print(input1dir)
if __name__ == "__main__": main(sys.argv)


