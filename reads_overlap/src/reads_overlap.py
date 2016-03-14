import re 
import pandas as pd
import csv
def main():   
    file1 = pd.read_csv('/Users/Xin/Desktop/IC_project/output/01132016/ICC_pb_taxa_replace.csv', )
    file2 = pd.read_csv('/Users/Xin/Desktop/IC_project/output/01132016/ICC_pb_taxapath.csv', names = ["read", "taxapath"], header = None)
    overlap = pd.merge(file1, file2, how = 'inner', on = 'read')
    #sum = overlap['taxa'].value_counts() 
    overlap.to_csv('/Users/Xin/Desktop/IC_project/output/01132016/ICC_replace_path.csv')
    #sum.to_csv('/Users/Xin/Desktop/IC_project/output/Jan202016/DS2_2_ICC_unmapped_species_count.csv')
    
if __name__ == "__main__": main() 