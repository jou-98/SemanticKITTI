#!/bin/bash

for file in dataset/sequences/*/labels/*.label
do 
    seq=$(echo $file | grep -o '/[0-9]*/' | cut -d'/' -f2)
    num=$(echo $file | grep -o '[0-9]*\.label' | cut -d'.' -f1)
    #echo "$seq $num"
    python3 check_valid.py $seq $num
done