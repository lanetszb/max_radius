import sys
import os
import numpy as np

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../tmp/pmeal/OpenPNM/'))
sys.path.append(os.path.join(current_path, '../tmp/pmeal/porespy/'))

import porespy as ps
import matplotlib.pyplot as plt
import scipy as sp

from scipy import ndimage


voxel_size = float(np.loadtxt('voxel_size.txt'))
image_distance_map = np.load('image_distance_map.npy')
image_input_output = np.load('image_input_output.npy')

threshold = 1.e-6
image_threshold = np.where(image_distance_map > threshold, 1, 0)
np.save('image_threshold', image_threshold) 
ps.io.to_vtk(image_threshold, path=f'image_threshold', divide=False, downsample=False, voxel_size=voxel_size, vox=False)

image_input = np.where(image_input_output == 1, 1, 0)
image_output = np.where(image_input_output == 2, 1, 0)

image_propagation = ndimage.binary_propagation(image_input, mask=image_threshold).astype(np.int)
np.save('image_propagation', image_propagation) 
ps.io.to_vtk(image_propagation, path=f'image_propagation', divide=False, downsample=False, voxel_size=voxel_size, vox=False)
