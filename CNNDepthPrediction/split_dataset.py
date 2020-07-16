import os
import shutil
import numpy as np

validation_size=0.2
datasetmap="Dataset/"
source = datasetmap+"train"
dest = datasetmap+"validation"
directory = os.listdir(source)

for dir in directory:
    files = os.listdir(source+'/'+dir)
    if not os.path.exists(dest+'/'+dir):
        os.makedirs(dest+'/'+dir)
    for file in files:
        if np.random.rand(1) < validation_size:
            print ("moving file: "+source+'/'+dir+'/'+file+" to folder: "+dest +'/'+ dir+'/'+file)
            shutil.move(source+'/'+dir+'/'+file, dest+'/'+dir+'/'+file)