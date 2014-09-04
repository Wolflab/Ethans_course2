#!/bin/bash
for file_name in data*.txt
do
	echo $file_name >> all.txt
	python species_counts.py $file_name >> all.txt
done
    