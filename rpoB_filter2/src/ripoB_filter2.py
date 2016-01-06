#this script is for filtering out the reverse reads of paired Reads
import re
import csv
import pandas as pd

def subsampling(inputhandle, readlist, outputhandle):
    flag = False
    for line in inputhandle: 
            if flag:
                if not line.startswith('>'):
                    print(line, file = outputhandle, end = '')  
                if line.startswith('>'):
                    flag = False      
            tmp = re.search(">(M00704:49:000000000-AFW6D[\d\:\w\/\_\-]+)\s",line)      
            if tmp:
                index = tmp.group(1) 
                if index not in readlist:
                    flag = True
                    print(line, file = outputhandle, end = '')
                    continue

def main():
    readslist = []
    readslist2 = []
    input = "/Users/Xin/Desktop/IC_project/output/rpoB_output/ICW_rpoB.fasta"
    output0 = "/Users/Xin/Desktop/IC_project/output/rpoB_output/read_counts.csv"
    output = open("/Users/Xin/Desktop/IC_project/output/rpoB_output/ICW_rpoB_nopaired.fasta", 'w')
    reads_tag ='_2:N:0:5'
    try:
        f0 = open(input, 'r')
        print("Open success!")
    except IOError:
        print ("no such file!")
    for line in f0:
        tmp0 = re.search("^\>(M00704:49:000000000-AFW6D[\d\:]+)",line)
        if tmp0:
            read = tmp0.group(1)
            readslist.append(read)
    print("Number of the reads in the list is ", len(readslist))
    f0.close()
    df_reads = pd.DataFrame(readslist, columns = ['read'])
    read_counts = df_reads['read'].value_counts()
    read_counts.to_csv(output0)
    f= open(input, 'r') 
        
    with open("/Users/Xin/Desktop/IC_project/output/rpoB_output/read_counts.csv", 'r') as csvfile:
        f1 = csv.DictReader(csvfile, delimiter = ",", fieldnames = ['read','count'])
        for row in f1:
            if int(row['count']) == 2:
                readslist2.append(row['read']+reads_tag)
        subsampling(f, readslist2, output)
            
    
if __name__ == "__main__": main()    


#  