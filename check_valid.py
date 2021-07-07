import numpy as np
import open3d as o3d
import sys
import os
import util as utils

SEQ = sys.argv[1]
NUM = sys.argv[2]

BIN_DIR = './dataset/sequences/'+SEQ+'/velodyne/'+NUM+'.bin'
LABEL_DIR = './dataset/sequences/'+SEQ+'/labels/'+NUM+'.label'

label_path = LABEL_DIR # + num + '.label'
bin_path = BIN_DIR
label = utils.read_label(label_path)

#print(f'Preprocessing file {NUM} from sequence {SEQ}')

background = list(range(50,75))
blacklist = [10,13,16,18,20,\
            *background,99,\
            252,253,254,255,256,257,258,259]
# Keep the classes person, bicycle, motorcycle, bicyclist, motorcyclist, pole, traffic sign
# Use unlabeled, outlier, road, parking, sidewalk, other-ground as background
# Previous: Keeping 30 as the positive class, and 0, 1, 40-49 as negative class
target = [11,15,30,31,32,80,81]
classes,counts=np.unique(label,return_counts=True)
# Remove file and return if target classes are not found
if not set(target) & set(classes):
    #print(f'Deleting file {NUM} from sequence {SEQ} due to no points')
    os.remove(label_path)
    os.remove(bin_path)
else:
    print(f'Keeping SEQ {SEQ} NUM {NUM}')
"""
else:
    sum=0
    for i in range(len(classes)):
        if classes[i] in target:
            sum += counts[i]
    if sum <= 500:
        print(f'Deleting file {NUM} from sequence {SEQ} due to too few points ({sum})')
"""
