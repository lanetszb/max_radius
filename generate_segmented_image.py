import sys
import os
import numpy as np

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../tmp/pmeal/OpenPNM/'))
sys.path.append(os.path.join(current_path, '../tmp/pmeal/porespy/'))

import porespy as ps
import matplotlib.pyplot as plt
import scipy as sp

        
poro = 0.6
blob = 0.5

voxel_size = 1.e-6

dims = [50, 50, 1]
image_segmented = ps.generators.blobs(shape=dims, porosity=poro, blobiness=blob)

image_input_output = image_segmented * 0
image_input_output[0, :, :] = 1
image_input_output[dims[0] - 1, :, :] = 2

np.save('image_input_output', image_input_output) 
np.save('image_segmented', image_segmented) 
np.savetxt('voxel_size.txt', [voxel_size]) 

plt.imshow(image_segmented[:,:,0])
plt.axis('off')
plt.show()

# exporing generated image to VTK format
ps.io.to_vtk(image_segmented, path=f'image_segmented', divide=False, downsample=False, voxel_size=voxel_size, vox=False)