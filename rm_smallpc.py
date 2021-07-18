import os, sys
import numpy as np 


SEQ = sys.argv[1]
NUM = sys.argv[2]

BIN_DIR = 'dataset/sequences/'+SEQ+'/velodyne/'+NUM+'.bin'
LABEL_DIR = 'dataset/sequences/'+SEQ+'/labels/'+NUM+'.label'

os.remove(BIN_DIR)
os.remove(LABEL_DIR)