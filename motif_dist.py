#this script is to match the motif locations with the gene locus_tag. 
import pandas as pd
import re
import csv
def main():  
    input1 = "/isi/olga/xin/Halophile_project/output/20160518/NC_013968_short.tvs"
    input2 = "/isi/olga/xin/Halophile_project/output/20160518/motif_phv1.csv"
    input3 = "/isi/olga/xin/Halophile_project/output/20160518/NC_013968_short.ptt"
    input4 = "/isi/olga/xin/Halophile_project/output/20160518/NC_013968_pseudo1.gff"
    output = "/isi/olga/xin/Halophile_project/output/20160519/motif_phv1_map.csv"
    genome = pd.read_csv(input1, header = None, names = ["start","end","id","locus_tag"], sep = '\t')   
    motif = pd.read_csv(input2) 
    ptt = pd.read_csv(input3, sep = '\t')
    pseudo = pd.read_csv(input4, header = None, names = ["id", "locus_tag", "region"], sep = '\t')
    motif_count = []
    gene_list = []
    motif_status = []
    genome_sorted = genome.sort(['start'])
    for i in range(len(motif['start'])):
        for j in range(len(genome_sorted['start'])):
            if motif['start'][i] >= genome_sorted['start'][j] and motif['end'][i] <= genome_sorted['end'][j]:
                motif_count.append(motif['start'][i])
                gene_list.append(genome_sorted['locus_tag'][j])
                motif_status.append("gene")
    df = pd.DataFrame({'start':motif_count, 'locus_tag':gene_list, 'region':motif_status})

    df2 = pd.DataFrame({'locus_tag':ptt['Synonym'], 'COG':ptt['COG'], 'Product':ptt['Product']})

    tmp = pd.merge(motif, df, on = "start", how = 'outer')
    motif_region_status = pd.merge(tmp, df2, on = "locus_tag", how = 'left')
    motif_region_status['locus_tag'] = motif_region_status['locus_tag'].fillna("none")
    motif_region_status['COG'] = motif_region_status['COG'].fillna("none")
    motif_region_status['Product'] = motif_region_status['Product'].fillna("none")
    motif_region_status['region'] = motif_region_status['region'].fillna("intergene")
    for k in range(len(motif_region_status['locus_tag'])):
        if (motif_region_status['locus_tag'][k] in list(pseudo['locus_tag'])):
            motif_region_status['region'][k] = "pseudo"
     
    motif_region_status.to_csv(output, sep = '\t')
    
if __name__ == "__main__": main() 