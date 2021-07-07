import numpy as np
import open3d as o3d
import sys

SEQ = sys.argv[1]
NUM = sys.argv[2]


LABEL_DIR = './dataset/sequences/'+SEQ+'/labels/'+NUM+'.label'
BIN_DIR = './dataset/sequences/'+SEQ+'/velodyne/'+NUM+'.bin'

def labelFromFile(fname):
    labels = np.fromfile(fname, dtype=np.uint16)
    labels = labels.reshape((-1,2))
    unique, counts = np.unique(labels[:,0], return_counts=True)
    dic = dict(zip(unique, counts))
    return labels


def pointsFromFile(fname):
    scan = np.fromfile(fname, dtype=np.float32)
    scan = scan.reshape((-1, 4))
    return scan[:,:3]

bin_path = BIN_DIR # + num + '.bin'
pts = pointsFromFile(bin_path)
label_path = LABEL_DIR # + num + '.label'
label = labelFromFile(label_path)

"""
pcd1 = o3d.geometry.PointCloud()
pcd1.points = o3d.utility.Vector3dVector(pts)
o3d.io.write_point_cloud(NUM+"normal.ply", pcd1)
"""
background = list(range(50,75))
blacklist = [10,13,16,18,20,\
            *background,\
            252,253,254,255,256,257,258,259]
# Keep the classes person, bicycle, motorcycle, bicyclist, motorcyclist, pole, traffic sign
# Use unlabeled, outlier, road, parking, sidewalk, other-ground as background
# Previous: Keeping 30 as the positive class, and 0, 1, 40-49 as negative class



others = np.isin(label[:,0],blacklist)
#print(others.shape)
pts = np.delete(pts,others,axis=0)
#print(pts.shape)

new_labels = np.delete(label,others,axis=0)
# new_labels = new_labels[:,0] # Takes the category number but not the instance number


new_labels.tofile(LABEL_DIR)
new_labels = new_labels.reshape((-1,1))
rgb = np.concatenate((new_labels,new_labels,new_labels),axis=1)

pts.tofile(BIN_DIR)
"""
pcd2 = o3d.geometry.PointCloud()
pcd2.points = o3d.utility.Vector3dVector(pts)

pcd2.colors = o3d.utility.Vector3dVector(rgb)

o3d.io.write_point_cloud(NUM+".ply", pcd2)

"""
