import re
import pandas as pd
import csv
## modified from "remove_reps.py" by Geogia
def main():

        input1 = "/isi/olga/xin/Halophile_project/output/20160505/ICC_reads_cog_all.csv"

 
        output2 = '/isi/olga/xin/Halophile_project/output/20160519/ICC_reads_cog_long.csv'
        output3 = '/isi/olga/xin/Halophile_project/output/20160519/ICC_reads_cog_short.txt'
        reps = pd.read_csv(input1, sep = ',')
        grouped = reps.sort(['reads','COG_id','e'])
        grouped_dedup = grouped.drop_duplicates(['reads','COG_id'])

        grouped_abr = grouped_dedup[['reads','COG_id','fun_class','COG_annotate','e']]
 
        grouped_dedup.to_csv(output2, sep = '\t')
        grouped_abr.to_csv(output3,index=False, sep = '\t')





if __name__=="__main__":main()