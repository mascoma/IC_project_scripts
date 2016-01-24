import re 
import pandas as pd
import csv
def main():   
    reads = pd.read_csv('/Users/Xin/Desktop/IC_project/output/rpoB_output/ICC_rpoB_reads.csv')
    taxa = pd.read_csv('/Users/Xin/Desktop/IC_project/output/01142016/ICC_assignment_new.csv')
    overlap = pd.merge(reads, taxa, how = 'inner', on = 'read')
    sum = overlap['taxa'].value_counts()
    overlap.to_csv('/Users/Xin/Desktop/IC_project/output/01142016/ICC_rpoB_reads_taxa.csv')
    sum.to_csv('/Users/Xin/Desktop/IC_project/output/01142016/ICC_rpoB_taxa_count.csv')
    
if __name__ == "__main__": main() 