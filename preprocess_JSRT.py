import os
import numpy as np
from skimage import io, exposure
"""
def make_lungs():
    path = 'All247images/'
    for i, filename in enumerate(os.listdir(path)):
        k = np.fromfile('All247images/' + filename, dtype='>u2')
        img = 1.0 - k.reshape((2048, -1)) * 1. / 4096
        img = exposure.equalize_hist(img)
        io.imsave('All247images/LungMake' + filename[:] + '.png', img)
        print ('Lung', i, filename)
"""
def make_masks():
    path = 'scratch/folder/masks/'
    for i, filename in enumerate(os.listdir('scratch/folder/masks/left lung')):
        left = io.imread('scratch/folder/masks/left lung/' + filename[:-4] + '.gif')
        right = io.imread('scratch/folder/masks/right lung/' + filename[:-4] + '.gif')
        io.imsave('scratch/folder/masks/new' + filename[:-4] + 'msk.png', np.clip(left + right, 0, 255))
        print ('Mask', i, filename)

#make_lungs()
make_masks()
