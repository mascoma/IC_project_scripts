#!/usr/bin/python3
# searchSeq.py by Xin Chen
# 09/9/2015
# search for a short fragments in sequences files and return the counts and positions
import re
def main():
    count1 = 0
    count2 = 0
    countreads = 0
    outfile1 = open('ICW_R2_N_output.txt', 'w')
    outfile2 = open('ICW_R2_S_output.txt', 'w')
    print('Start\tend\n', file = outfile1, end = '\n')
    print('Start\tend\n', file = outfile2, end = '\n')
    try:
        f = open('ICW_S5_L001_R2_001.fastq', 'r')
        print("successful open!")
        for line in f:  
            indexN = (re.search('TAGGCATG',line,re.IGNORECASE))
            indexS = (re.search('AGAGTAGA', line, re.IGNORECASE))
            tmp = (re.search('@M00704:',line,re.IGNORECASE))
            if indexN:
                startPosition = str(indexN.start())
                endPosition = str(indexN.end())
                count1 = count1 + 1
                print(startPosition, '\t', endPosition,  file = outfile1, end = '\n')
            if indexS:
                startPosition = str(indexS.start())
                endPosition = str(indexS.end())
                count2 = count2 + 1
                print(startPosition, '\t', endPosition,  file = outfile2, end = '\n')
            if tmp:
                countreads = countreads +1    
        freq1 = count1 / countreads    
        freq2 = count2 / countreads    
        print("The total count of index N is " + str(count1))
        print("The total count of index S is " + str(count2))
        print("The frequency of index N " + str(freq1))   
        print("The frequency of index S " + str(freq2))    
    except IOError:
            print ("no such file!")      
    
if __name__ == "__main__": main()      