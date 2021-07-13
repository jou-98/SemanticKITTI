import numpy as np 
import glob 


for i in range(11):
    arg = 'dataset/sequences/'+str(i).zfill(2)+'/labels/*.label'
    files = glob.glob(arg)
    for fname in files:
        arr = np.fromfile(fname,dtype=uint16)
        classes, counts = np.unique(arr,return_counts=True)
        for j in range(len(classes)):
            print(f'Class {classes[j]} occurrence: {counts[j]} times')


