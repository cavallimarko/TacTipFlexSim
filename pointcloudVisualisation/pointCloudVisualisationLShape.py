import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#actual code to load,slice and display the point cloud

data_path="PointClouds/"
filename="MeasurementLRot10.0.txt"
point_cloud= np.loadtxt(data_path+filename)
mean_Z=np.mean(point_cloud,axis=0)[2]
#spatial_query=point_cloud[abs( point_cloud[:,2]-mean_Z)<1000]
point_cloud[point_cloud[:, 2] <0, 2] = 150
spatial_query=point_cloud
xyz=spatial_query[:,:3]
rgb=spatial_query[:,3:]
ax = plt.axes(projection='3d')
ax.scatter(xyz[:,0], xyz[:,1], xyz[:,2], c = rgb/255, s=3)
plt.show()
ax = plt.axes(projection='3d')
ax.plot_trisurf(xyz[:,0], xyz[:,1], xyz[:,2],cmap='viridis', edgecolor='none')
plt.show()