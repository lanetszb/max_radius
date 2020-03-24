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

from bool_shooting_method import implement_bool_shooting_method

class Max_radius:
    def __init__(s, distance_map_im, input_im, output_im, save_paraview=False, voxel_size=1.e-6):
        s.distance_map_im = distance_map_im
        s.input_im = input_im
        s.output_im = output_im
        s.save_paraview = save_paraview
        s.voxel_size = voxel_size
        
    def is_propagated(s, threshold):
        mask = np.where(s.distance_map_im > threshold, 1, 0)
        propagation = ndimage.binary_propagation(input=s.input_im, mask=mask).astype(np.int)
        if s.save_paraview:
            ps.io.to_vtk(mask, path=f'mask', divide=False, downsample=False, voxel_size=s.voxel_size, vox=False)
            ps.io.to_vtk(propagation, path=f'propagation', divide=False, downsample=False, voxel_size=s.voxel_size, vox=False)
        return bool(np.count_nonzero(propagation[np.nonzero(s.output_im)]))
    

voxel_size = float(np.loadtxt('voxel_size.txt'))
distance_map_im = np.load('image_distance_map.npy')
input_output_im = np.load('image_input_output.npy')
input_im = np.where(input_output_im == 1, 1, 0)
output_im = np.where(input_output_im == 2, 1, 0)

max_radius = Max_radius(distance_map_im, input_im, output_im, True, voxel_size)

print('threshold, accuracy', implement_bool_shooting_method(max_radius.is_propagated, init_x=1.e-6, init_dx=1.e-6, min_dx=1.e-8))