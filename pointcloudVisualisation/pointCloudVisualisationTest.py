import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#actual code to load,slice and display the point cloud
file_data_path="PointClouds/sample.xyz"
point_cloud= np.loadtxt(file_data_path,skiprows=1)
mean_Z=np.mean(point_cloud,axis=0)[2]
spatial_query=point_cloud[abs( point_cloud[:,2]-mean_Z)<1]
xyz=spatial_query[:2000,:3]
rgb=spatial_query[:2000,3:]
ax = plt.axes(projection='3d')
#ax.scatter(xyz[:,0], xyz[:,1], xyz[:,2], c = rgb/255, s=0.01)

ax = plt.axes(projection='3d')
ax.plot_trisurf(xyz[:,0], xyz[:,1], xyz[:,2],
                cmap='viridis', edgecolor='none')
plt.show()