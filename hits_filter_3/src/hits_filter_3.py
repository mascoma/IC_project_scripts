#!/usr/bin/python3
import re 
import pandas as pd
def main():
    input1dir ="/Users/Xin/Desktop/IC_project/output/01112016/DS2_1_pb_reads_taxa.csv"
    input2dir ="/Users/Xin/Desktop/IC_project/output/01132016/DS2_1_pb_taxa.csv"
    outputdir = "/Users/Xin/Desktop/IC_project/output/01132016/DS2_1_pb_taxa_diff.csv"        
    df1 = pd.read_csv(input1dir)
    df2 = pd.read_csv(input2dir)
    df3 = pd.merge(df1, df2, on = 'read' ,how = 'inner')
    df3.to_csv('/Users/Xin/Desktop/IC_project/output/01132016/DS2_1_pb_taxa_overlap.csv')
    output = open(outputdir, 'w')
    try:
        f = open('/Users/Xin/Desktop/IC_project/output/01132016/DS2_1_pb_taxa_overlap.csv','r')
    except IOError:
        print ("no such file!") 
    for line in f:
        tmp = re.search('M00704:49:000000000-AFW6D:[\w\d\:\_\/]+\,\d+\,([\w\<\> ?]+)\,([\w\<\> ?]+)$', line)
        if tmp:
            taxa1 = tmp.group(1)
            taxa2 = tmp.group(2)
            if taxa1 != taxa2:
                print(line, file = output, end = '')
    
if __name__ == "__main__": main() 