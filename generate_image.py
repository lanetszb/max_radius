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
image = ps.generators.blobs(shape=dims, porosity=poro, blobiness=blob)

np.save('image', image) 

plt.imshow(image[:,:,0])
plt.axis('off')
plt.show()

# exporing generated image to VTK format
ps.io.to_vtk(image, path=f'image', divide=False, downsample=False, voxel_size=1E-6, vox=False)