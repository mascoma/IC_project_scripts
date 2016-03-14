#!/usr/bin/python2.7
import re 
import pandas as pd
def main():
    inputdir1 = '/isi/olga/xin/Halophile_project/output/Jan132016/DS2_1_assigned_old.csv'
    inputdir2 = '/isi/olga/xin/Halophile_project/output/Jan132016/DS2_1_pb_taxa_replace.csv'
    outputdir = '/isi/olga/xin/Halophile_project/output/Jan132016/DS2_1_fixed_assigned.csv'
    df1 = pd.read_csv(inputdir1)
    df2 = pd.read_csv(inputdir2)
    for i in range(0, len(df1['read'])):
        for j in range(0, len(df2['read'])):
            if df1['read'][i] == df2['read'][j]:
                df1['taxa'][i] = df2['taxa1'][j]                
    df1.to_csv(outputdir)        
if __name__ == "__main__": main() 
