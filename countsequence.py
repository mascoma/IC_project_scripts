#this script is to count the total number of sequences in fasta files

import re
def main():
    count1 = 0
    try:
        f = open('nr_all.faa', 'r')
        print("successful open!")
        for line in f:  
            indexN = (re.search('>',line,re.IGNORECASE))
            if indexN:
                count1 = count1 + 1
        print(count1)        
    except IOError:
        print ("no such file!")      
    
if __name__ == "__main__": main()      
