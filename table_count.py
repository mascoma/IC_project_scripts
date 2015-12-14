import pandas as pd
def main():  

    df1 = pd.read_table('DS2_1_rpoB.txt', header = 0)
    df2 = pd.read_table('DS2_2_rpoB.txt', header = 0)
    df3 = pd.read_table('ICC_rpoB.txt', header = 0)
    df4 = pd.read_table('ICW_rpoB.txt', header = 0)
    reads_count1 = df1['reads'].value_counts()
    reads_count2 = df2['reads'].value_counts()
    reads_count3 = df3['reads'].value_counts()
    reads_count4 = df4['reads'].value_counts()
    taxa_count1.to_csv("DS2_1_rpoB_reads.csv")
    taxa_count2.to_csv("DS2_2_rpoB_reads.csv")
    taxa_count3.to_csv("ICC_rpoB_reads.csv")
    taxa_count4.to_csv("ICW_rpoB_reads.csv")
if __name__ == "__main__": main() 