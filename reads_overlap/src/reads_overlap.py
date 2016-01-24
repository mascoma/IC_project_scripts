import re 
import pandas as pd
import csv
def main():   
    reads = pd.read_csv('/Users/Xin/Desktop/IC_project/output/Jan202016/DS2_2_ICC_CLC_unmapped.csv')
    taxa = pd.read_csv('/Users/Xin/Desktop/IC_project/output/01142016/reads_assignment_new/DS2_2_read_species.csv')
    overlap = pd.merge(reads, taxa, how = 'inner', on = 'read')
    sum = overlap['taxa'].value_counts() 
    overlap.to_csv('/Users/Xin/Desktop/IC_project/output/Jan202016/DS2_2_ICC_unmapped_species.csv')
    sum.to_csv('/Users/Xin/Desktop/IC_project/output/Jan202016/DS2_2_ICC_unmapped_species_count.csv')
    
if __name__ == "__main__": main() 