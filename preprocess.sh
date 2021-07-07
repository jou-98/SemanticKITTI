#!/bin/bash

seqNum=00

while read line
do
    seq=$(echo $file | grep -o '/[0-9]*/' | cut -d'/' -f2)
    if [ $seqNum -eq $seq ]
    then 
        num=$(echo $file | grep -o '[0-9]*\.label' | cut -d'.' -f1)
        unzip -j /srv/scratch/z5211173/data_odometry_velodyne.zip dataset/sequences/$seq/velodyne/$num.bin -d dataset/sequences/$seq/velodyne/
        python3 preprocess.py $seq $num
    fi
done < binList.txt
