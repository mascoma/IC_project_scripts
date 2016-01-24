# this script is to select the hits with given the 
#read list and filter out the problematic hits
# arg1 is all the hits file
# arg2 is the problematic hits file
# arg3 is the output file
#!/usr/bin/python3
import sys, getopt

import re 
def main(argv):
    if len(argv[1:]) == 3:
        input1dir = argv[1]
        input2dir = argv[2]
        outputdir = argv[3]
    else:
        print("Three arguements are needed!!")
    output = open(outputdir, 'w')
    try:
        all_hits = open(input1dir, 'r')
    except IOError:
        print ("no hits file!") 
    try:
        reads = open(input2dir, 'r')
    except IOError:
        print ("no reads file!") 
    readslist = []
    for line1 in reads:
        tmp = re.search("(M00704:49:000000000-AFW6D[\w\d\_\:\/\-]+)\s", line1)
        if tmp:
            readname1=tmp.group(1)
            readslist.append(readname1)
    print("total readslist:", len(readslist)) 
     
    for line2 in all_hits: 
        tmp1 = re.search("(M00704:49:000000000-AFW6D[\w\d\_\:\/\-]+)\s", line2)
        tmp2 = re.search("gi\|344319636",line2)
        if tmp1 and not tmp2:
            readname2=tmp1.group(1)
            if readname2 in readslist:
                print(line2, file = output, end = '')  
 
if __name__ == "__main__": main(sys.argv) 
