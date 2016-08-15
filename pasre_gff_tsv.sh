#!/bin/bash

for f in *.gff; do
	
	echo $f
	f1="${f%.*}"
 	sed -i.bak '/#/d' $f
 	sed -i.bak2 '/gbkey=CDS/d' $f
 	grep 'pseudo=true' $f > $f1"_pseudo.gff" 
	sed -i.bak3 '/pseudo=true/d' $f
	awk -F $'\t' '{print $4, $5, $9}' $f |  awk -F ';' '{print $1, ( $(NF) )}' > $f1"_short1.gff"
 	awk -F $'\t' '{print $4, $5, $9}' $f1"_pseudo.gff" |  awk -F ';' '{print $1, ( $(NF-1) ) }' > $f1"_short2.gff"
 	awk -F $'\t' '{print $9}' $f1"_pseudo.gff" |  awk -F ';' '{print $1, ( $(NF-1) ), ( $(NF) )  }' > $f1"_pseudo1.gff"
 	cat $f1_short1.gff $f1"_short2.gff" >  $f1"_short.gff"
 	sed -E 's/ID=//g' $f1"_short.gff" | sed -E 's/locus_tag=//g' | sed '/id0/d' |sed -E $'s/\s/\t/g' > $f1"_short.tvs"

 done