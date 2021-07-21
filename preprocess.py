import numpy as np
import open3d as o3d
import sys
from util import read_pc, read_label,render_color
import util
SEQ = sys.argv[1]
NUM = sys.argv[2]


LABEL_DIR = './dataset/sequences/'+SEQ+'/labels/'+NUM+'.label'
BIN_DIR = './dataset/sequences/'+SEQ+'/velodyne/'+NUM+'.bin'

bin_path = BIN_DIR # + num + '.bin'
pts = read_pc(bin_path,dim=4)
label_path = LABEL_DIR # + num + '.label'
label = read_label(label_path,dim=2)

# Keep the classes person, bicycle, motorcycle, bicyclist, motorcyclist, pole, traffic sign
# Use unlabeled, outlier, road, parking, sidewalk, other-ground as background
whitelist = [0,1,11,15,30,31,32,40,44,48,49,80,81,99]
target = [11,15,30,31,32,80,81]

# If there are no target points found in the point cloud, discard it
target_points = np.isin(label,target)
if np.unique(target_points).shape[0] == 1:
    os.remove(bin_path)
    os.remove(label_path)
    sys.exit()
"""
# Get the valid points
valid = np.isin(label,whitelist,invert=False)
# Keep only the valid points and save the files
pts = pts[valid]
new_labels = label[valid]
pts.tofile(BIN_DIR)
new_labels.tofile(LABEL_DIR)
"""