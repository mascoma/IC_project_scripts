import pandas as pd
def main():  
    input1 = "/Users/Xin/Desktop/IC_project/output/ICC_DS2_CLC_mapping_output/ICC_DS2_1_bl_dd_reads_genus.csv"
    output1 = "/Users/Xin/Desktop/IC_project/output/ICC_DS2_CLC_mapping_output/ICC_DS2_1_bl_dd_genus_count.csv"
    input2 = "/Users/Xin/Desktop/IC_project/output/ICC_DS2_CLC_mapping_output/ICC_DS2_2_bl_dd_reads_genus.csv"
    output2 = "/Users/Xin/Desktop/IC_project/output/ICC_DS2_CLC_mapping_output/ICC_DS2_2_bl_dd_genus_count.csv"
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
   
    taxa_count1 = df1['taxa'].value_counts()
    taxa_count2 = df2['taxa'].value_counts()
     
    taxa_count1.to_csv(output1)
    taxa_count2.to_csv(output2)

if __name__ == "__main__": main() 