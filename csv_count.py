import pandas as pd
def main():  

    df1 = pd.read_csv('DS2_1_reads_taxon.csv')
    df2 = pd.read_csv('DS2_2_reads_taxon.csv')
    df3 = pd.read_csv('ICC_reads_taxon.csv')
    taxa_count1 = df1['taxa'].value_counts()
    taxa_count2 = df2['taxa'].value_counts()
    taxa_count3 = df3['taxa'].value_counts()
    taxa_count1.to_csv("DS2_1_taxa_count.csv")
    taxa_count2.to_csv("DS2_2_taxa_count.csv")
    taxa_count3.to_csv("ICC_taxa_count.csv")
if __name__ == "__main__": main() 