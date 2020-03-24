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


image_distance_map = ndimage.distance_transform_edt(np.load('image_segmented.npy'))

np.save('image_distance_map', image_distance_map) 

plt.imshow(image_distance_map[:,:,0])
plt.axis('off')
plt.show()

# exporing generated image to VTK format
ps.io.to_vtk(image_distance_map, path=f'image_distance_map', divide=False, downsample=False, voxel_size=1E-6, vox=False)