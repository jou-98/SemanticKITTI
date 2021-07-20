#!/bin/bash
echo "Processing SEQ $1......"
for file in dataset/sequences/$1/labels/*.label
do 
    cp $file ../drive/MyDrive/$file
done
echo "Done copying the label files"
for file in dataset/sequences/$1/velodyne/*.bin
do 
    cp $file ../drive/MyDrive/$file
done
echo "Done copying the velodyne files"