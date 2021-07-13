import numpy as np 
import glob 

counts = {0:"unlabeled", 1 : "outlier", 11: "bicycle", 15: "motorcycle",\
        30: 0, 31: 0, 32: 0, 40: 0,\
        44: 0, 48: 0, 49: 0, 80: 0, 81: 0}

for i in range(11):
    arg = 'dataset/sequences/'+str(i).zfill(2)+'/labels/*.label'
    files = glob.glob(arg)
    
    for fname in files:
        arr = np.fromfile(fname,dtype=np.uint16)
        classes, counts = np.unique(arr,return_counts=True)
        for j in range(len(classes)):
            print(f'Class {classes[j]} occurrence: {counts[j]} times')


