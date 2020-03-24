import sys
import os
import numpy as np

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../tmp/pmeal/OpenPNM/'))
sys.path.append(os.path.join(current_path, '../tmp/pmeal/porespy/'))

import porespy as ps
import matplotlib.pyplot as plt
import scipy as sp


voxel_size = 1.e-6
np.savetxt('voxel_size.txt', [voxel_size])
        
poro = 0.6
blob = 0.5
dims = [50, 50, 50]
segmented_im = ps.generators.blobs(shape=dims, porosity=poro, blobiness=blob)
np.save('segmented_im', segmented_im) 
# ps.io.to_vtk(segmented_im, path=f'segmented_im', divide=False, downsample=False, voxel_size=voxel_size, vox=False)

input_output_im = np.zeros_like(segmented_im, dtype=int)
input_output_im[0, :, :] = segmented_im[0, :, :]
input_output_im[dims[0] - 1, :, :] = segmented_im[dims[0] - 1, :, :] * 2
np.save('input_output_im', input_output_im) 
# ps.io.to_vtk(input_output_im, path=f'input_output_im', divide=False, downsample=False, voxel_size=voxel_size, vox=False)

# plt.imshow(segmented_im[:,:,0])
# plt.axis('off')
# plt.show()
