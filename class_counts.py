import numpy as np 
import glob 

count_dict = {0: 0, 1: 0, 11: 0, 15: 0,\
        30: 0, 31: 0, 32: 0, 40: 0,\
        44: 0, 48: 0, 49: 0, 80: 0, 81: 0, 99: 0}

for i in range(10):
    arg = 'dataset/sequences/'+str(i).zfill(2)+'/labels/*.label'
    files = glob.glob(arg)
    
    for fname in files:
        arr = np.fromfile(fname,dtype=np.uint16)
        classes, counts = np.unique(arr,return_counts=True)
        for j in range(len(classes)):
            if not classes[j] in count_dict:
                print(f'{fname}')
                count_dict[classes[j]] = 0
            count_dict[classes[j]] += counts[j]
            #print(f'Class {classes[j]} occurrence: {counts[j]} times')
print(count_dict)


