#!/bin/bash


while read line
do 
    seq=$(echo $line | grep -o 'SEQ [0-9]*' | cut -d' ' -f2)
    num=$(echo $line | grep -o 'NUM [0-9]*' | cut -d' ' -f2)
    python3 rm_smallpc.py $seq $num
done < to_delete.txt