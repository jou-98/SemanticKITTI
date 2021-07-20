#!/bin/bash

for dir in dataset/sequences/*
do 
    mkdir $dir/velodyne
    mkdir $dir/labels
done