import sys
import os
import numpy as np
from scipy import ndimage

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../tmp/pmeal/OpenPNM/'))
sys.path.append(os.path.join(current_path, '../tmp/pmeal/porespy/'))
import porespy as ps


def bool_shooting_method(bool_function, init_x, init_dx, min_dx):
    ind = 0
    y_curr = bool_function(init_x, ind)
    
    y_prev = y_curr
    x = init_x
    if y_curr:
        dx = abs(init_dx)
    else:
        dx = -abs(init_dx)
        
    while True:
        x += dx
        y_prev = y_curr
        ind += 1
        y_curr = bool_function(x, ind)
        if y_curr != y_prev:
            dx /= -2.
        if abs(dx) < abs(min_dx):
            break
    
    return x, abs(dx)
    
class Max_radius:
    def __init__(s, distance_map_im, input_im, output_im, save_paraview=False, voxel_size=1.e-6):
        s.distance_map_im = distance_map_im
        s.input_im = input_im
        s.output_im = output_im
        s.save_paraview = save_paraview
        s.voxel_size = voxel_size
        
    def is_propagated(s, threshold, ind=0):
        mask = np.where(s.distance_map_im > threshold, 1, 0)
        propagation = ndimage.binary_propagation(input=s.input_im, mask=mask).astype(np.int)
        
        if s.save_paraview:            
            ps.io.to_vtk(mask, path=f'mask_{ind}', divide=False, downsample=False, voxel_size=s.voxel_size, vox=False)            
            ps.io.to_vtk(propagation, path=f'propagation_{ind}', divide=False, downsample=False, voxel_size=s.voxel_size, vox=False)
            
        return bool(np.count_nonzero(propagation[np.nonzero(s.output_im)]))
        