makeblastdb -in /isi/olga/xin/Halophile_project/db_source/nt_halo_.fna -dbtype nucl  -out /isi/olga/xin/Halophile_project/db/nt_halo

## for blastn query, to increase the computational speed, split the query file ## into multiple files and run parellal pbs jobs 

perl /isi/olga/xin/Halophile_project/bin/split_multifasta.pl --in /isi/olga/xin/Halophile_project/input/merged_reads_CLC_fa/DS2_1_CLC.fasta --output_dir=/isi/olga/xin/Halophile_project/output/blastn_split_query_results --f=DS2_1_CLC --seqs_per_file=300000 

perl /isi/olga/xin/Halophile_project/bin/split_multifasta.pl --in /isi/olga/xin/Halophile_project/input/merged_reads_CLC_fa/DS2_2_CLC.fasta --output_dir=/isi/olga/xin/Halophile_project/output/blastn_split_query_results --f=DS2_2_CLC --seqs_per_file=300000 

perl /isi/olga/xin/Halophile_project/bin/split_multifasta.pl --in /isi/olga/xin/Halophile_project/input/merged_reads_CLC_fa/ICC_CLC.fasta --output_dir=/isi/olga/xin/Halophile_project/output/blastn_split_query_results --f=ICC_CLC --seqs_per_file=300000 

perl /isi/olga/xin/Halophile_project/bin/split_multifasta.pl --in /isi/olga/xin/Halophile_project/input/merged_reads_CLC_fa/ICW_CLC.fasta --output_dir=/isi/olga/xin/Halophile_project/output/blastn_split_query_results --f=ICW_CLC --seqs_per_file=300000 

blastn -db /isi/olga/xin/Halophile_project/db/nt_halo -query /isi/olga/xin/Halophile_project/input/merged_reads_CLC_fa/DS2_1_CLC1.fasta -outfmt 6  -evalue 0.000001 -out /isi/olga/xin/Halophile_project/output/Jan192016/HdrB_ICC.txt

diamond makedb --in /isi/olga/xin/Halophile_project/db_source/nr_halo_.faa -d /isi/olga/xin/Halophile_project/db/nr_halo_diamond