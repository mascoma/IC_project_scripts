#!/bin/bash
inputdir=$1
fullfilename=$2
filename=`echo "$fullfilename" | cut -d'.' -f1`
outputdir=$3
suffix1='_blx_k5'
suffix2='_blx_5k_hits_gilist'
suffix3='_blx_5k_hits_seq'

echo $inputdir$fullfilename
echo $inputdir$filename$suffix1
echo $outputdir$filename$suffix2
echo $outputdir$filename$suffix3

diamond blastx -d /isi/olga/xin/Halophile_project/db/nr_halo_diamond.dmnd -q $inputdir$fullfilename -e 0.000001 -k 5 -a $outputdir$filename$suffix1.daa

diamond view -a $outputdir$filename$suffix1.daa -f tab -o $outputdir$filename$suffix1.m8 

awk -F $'\t' '{print $2}' $outputdir$filename$suffix1.m8 | awk -F '|' '{print $2}' > $outputdir$filename$suffix2.txt
 
blastdbcmd -db /isi/olga/xin/Halophile_project/db/nr_halo -dbtype prot -entry_batch $outputdir$filename$suffix2.txt -out $outputdir$filename$suffix3.fa

perl /isi/olga/xin/Halophile_project/bin/split_multifasta.pl --input_file=$outputdir$filename$suffix3.fa --output_dir=$outputdir --f=$filename$suffix3 --seqs_per_file=4000

