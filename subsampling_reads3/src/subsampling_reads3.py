import csv
import re 
import pandas as pd
from subsampling_class import Subsampling
def main():
    genuslist = []
    readlist = []
    inputfiledir1 = "/Users/Xin/Desktop/IC_project/output/Jan222016/resource_tables/ICC_DS2_2_unmapped_genus_count.csv"
    inputfiledir2 = "/Users/Xin/Desktop/IC_project/output/Jan222016/resource_tables/ICC_DS2_2_unmapped_taxa.csv"
    inputfiledir3 = "/Users/Xin/Desktop/IC_project/output/ICC_DS2_CLC_mapping_output/ICC_DS2_2_CLC_unmapped.fa"
    outputfiledir = "/Users/Xin/Desktop/IC_project/output/Feb032016/ICC_DS2_2_unmapped_genus.fa"
    outputfile = open(outputfiledir, 'w')
    seq = open(inputfiledir3, 'r')
    genus = pd.read_csv(inputfiledir1, names=["taxa", "count"], header=None)
    read_taxa = pd.read_csv(inputfiledir2, names=["num", "read","id","taxa"], header=None)
    for row in genus["taxa"]:
        genuslist.append(row)
    for i in range(0,len(read_taxa["taxa"])):
        tmp = read_taxa["taxa"][i]
        if tmp in genuslist:
              readlist.append(read_taxa["read"][i])
    subset = Subsampling()  
    subset.include(seq, readlist, outputfile)          
if __name__ == "__main__": main() 