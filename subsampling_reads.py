import re 
import csv

def main():
    output = open("/Users/Xin/Desktop/IC_project/output/Nov242015/DS2_1_unassigned_blastn.fasta", 'w')
    try:
        all_reads = open("/Users/Xin/Desktop/IC_project/input/merged_reads_CLC/ICW_CLC.fasta", 'r')
    except IOError:
        print ("no such file!") 
    readslist = []
    readslist1 = []
    flag = False
    with open('/Users/Xin/Desktop/IC_project/output/Nov242015/ICW_CLC_reads_genus.csv', 'r') as inputfile:
        input = csv.DictReader(inputfile, delimiter =",", fieldnames=['reads','genus'])
        for row in input:
            readslist.append(row['reads']) # all the reads
        print("total reads:", len(readslist)) 
        
        for line in all_reads: 
            if flag:
                if not line.startswith('>'):
                    print(line, file = output, end = '')  
                if line.startswith('>'):
                    flag = False      
            tmp = re.search(">(M00704:49:000000000-AFW6D[\d\:\w\/\_\-]+)\s",line)      
            if tmp:
                index = tmp.group(1) 
                if index not in readslist:
                    readslist1.append(index)# unassigned reads after blastn
                    flag = True
                    print(line, file = output, end = '')
                    continue
                     
        print("unassigned reads:", len(readslist1))    
                
if __name__ == "__main__": main() 