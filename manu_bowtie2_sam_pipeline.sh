#!/bin/bash

for f in *.sam; do
	
	echo $f
	f1="${f%.*}"
	f2="_mapped.txt"
	ff=$f1$f2
	grep 'M00704:49:000000000-AFW6D' $f | grep 'gi' | awk -F '\t' '{print $1, $2, $3}' | sed  's/|/ /g'  | awk -F ' ' '{print $1, $4, $6}'  > $ff 	
done
	
