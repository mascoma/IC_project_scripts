import re 
import pandas as pd
import csv
def main():   
    rpob = pd.read_csv('/Users/Xin/Desktop/IC_project/output/reads_assigned_bl_dd/DS2_2_rpoB_reads.csv')
    taxon = pd.read_csv('/Users/Xin/Desktop/IC_project/output/reads_assigned_bl_dd/DS2_2_CLC_bl_dd_genus.csv')
    overlap = pd.merge(rpob, taxon, how = 'inner', on = 'read')
    sum = overlap['taxon'].value_counts() 
    overlap.to_csv('/Users/Xin/Desktop/IC_project/output/reads_assigned_bl_dd/DS2_2_rpoB_taxon.csv')
    sum.to_csv('/Users/Xin/Desktop/IC_project/output/reads_assigned_bl_dd/DS2_2_rpoB_taxon_count.csv')
    
if __name__ == "__main__": main() 