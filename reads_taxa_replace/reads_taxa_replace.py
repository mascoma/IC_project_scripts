#!/usr/bin/python3
import re 
import pandas as pd
def main():
    inputdir1 = '/Users/Xin/Desktop/IC_project/output/01082016/reads_assigned/ICC_assigned_old.csv'
    inputdir2 = '/Users/Xin/Desktop/IC_project/output/01132016/ICC_pb_taxa_replace.csv'
    outputdir = '/Users/Xin/Desktop/IC_project/output/01132016/ICC_fixed_assigned.csv'
    df1 = pd.read_csv(inputdir1)
    df2 = pd.read_csv(inputdir2)
    for i in range(0, len(df1['read'])):
        for j in range(0, len(df2['read'])):
            if df1['read'][i] == df2['read'][j]:
                df1['taxa'][i] = df2['taxa1'][j]
        print(i)
                
    df1.to_csv(outputdir)        
if __name__ == "__main__": main() 