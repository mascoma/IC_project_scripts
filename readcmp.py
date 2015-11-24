#!/usr/bin/python3
# readscmp.py by Xin Chen
# 09/29/2015
# this is for comparing the diamond and blastn RESULTS

import re
def main():
    output1 = open("test_diamond_nohits.txt", 'w')
    output2 = open("test_blastn_nohits.txt", 'w')
    output3 = open("test_fighits.txt", 'w')
    output4 = open("test_diffhits.txt", 'w')
    readslist = []
    count = 0
    try:
        f = open("testreads.txt", 'r')      
        print("Open success!")
        for line in f:
            readslist.append(line.rstrip('\n'))
        while (count < len(readslist)): 
            flag = True
            flag2 = True
            f1 = open("test_matches.m8", 'r')
            f2 = open("test_small.m8", 'r')   
            diamondgi = []
            blastgi = []
            reads = readslist[count]
            for line1 in f1:
                index1 = re.search(reads, line1)
                if index1:
                    tmp1 = re.search('(gi\|[\d]+)\|', line1)
                    tmp3 = re.search('fig\|[\d]+', line1)
                    if tmp1:
                        giNum1 = tmp1.group(1)
                        diamondgi.append(giNum1)
                        flag  = False   
                    if tmp3: 
                        print(line1, file = output3, end= '\n')
                        flag  = False          
            if flag : 
                print(readslist[count], file = output1, end = '\n')
                    
            for line2 in f2:
                index2 = re.search(readslist[count], line2)
                if index2:
                    tmp2 = re.search('(gi\|[\d]+)\|', line2)
                    if tmp2:
                        giNum2 = tmp2.group(1)
                        blastgi.append(giNum2)
                        flag2  = False                                
            if flag2 : 
                print(readslist[count], file = output2, end = '\n')
            f1.close()
            f2.close()
            if diamondgi and blastgi:
                index = set(diamondgi).intersection(blastgi)
                if not index:
                    print(readslist[count], file = output4, end = '\n')
            count = count + 1 
    except IOError:
        print ("no such file!") 
if __name__ == "__main__": main() 