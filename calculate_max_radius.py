import sys
import os
import numpy as np

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../tmp/pmeal/OpenPNM/'))
sys.path.append(os.path.join(current_path, '../tmp/pmeal/porespy/'))

import porespy as ps
import matplotlib.pyplot as plt

from scipy import ndimage

from max_radius import bool_shooting_method
from max_radius import Max_radius


def calculate_max_radius(segmented_im, voxel_size, input_output_im, file_name='out/im'):
    # calculate distance map
    distance_map_im = ndimage.distance_transform_edt(segmented_im)
    distance_map_im *= voxel_size
    # np.save(file_name + '_distance_map', distance_map_im)
    # ps.io.to_vtk(distance_map_im, path=file_name + '_distance_map', divide=False,
    #              downsample=False, voxel_size=voxel_size, vox=False)
    plt.imshow(distance_map_im[:, :, 0])
    plt.axis('off')
    plt.show()

    # calculate max radius
    input_im = np.where(input_output_im == 1, 1, 0)
    output_im = np.where(input_output_im == 2, 1, 0)
    max_radius = Max_radius(distance_map_im, input_im, output_im, voxel_size=voxel_size)
    result = bool_shooting_method(max_radius.is_propagated, init_x=1.e-6,
                                  init_dx=1.e-6, min_dx=1.e-9)

    print('threshold, accuracy', result)

    np.savetxt(file_name + '_max__radius.txt', [result[0]])

    return result


if __name__ == '__main__':
    result = calculate_max_radius(segmented_im=np.load('out/segmented_im.npy'),
                                  voxel_size=float(np.loadtxt('out/voxel_size.txt')),
                                  input_output_im=np.load('out/input_output_im.npy'),
                                  distance_map_name='out/distance_map_im')
