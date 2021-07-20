#!/bin/bash

seqNum="$1"

while read line
do
    seq=$(echo $line | grep -o '/[0-9]*/' | cut -d'/' -f2)
    if [ $seqNum -eq $seq ]
    then 
        num=$(echo $line | grep -o '[0-9]*\.bin' | cut -d'.' -f1)
        #echo "seq is $seq and num is $num"
        unzip -q -j /content/SemanticKITTI/data_odometry_velodyne.zip dataset/sequences/$seq/velodyne/$num.bin -d dataset/sequences/$seq/velodyne/
        unzip -q -j /content/SemanticKITTI/data_odometry_labels.zip dataset/sequences/$seq/labels/$num.label -d dataset/sequences/$seq/labels/
        python3 preprocess.py $seq $num
    fi
done < binList.txt