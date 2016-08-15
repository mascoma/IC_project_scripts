#!/bin/bash
 
inputdir=$1
echo $inputdir
fullfilename=$2
filename=`echo "$fullfilename" | cut -d'.' -f1`
echo $filename
