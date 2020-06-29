import stl
import numpy as np
from stl import mesh
file_data_path="PointClouds/Measurement1.txt"
point_cloud= np.loadtxt(file_data_path)
mean_Z=np.mean(point_cloud,axis=0)[2]
spatial_query=point_cloud
xyz=spatial_query[:,:3]

data = np.zeros(len(xyz), dtype=mesh.Mesh.dtype)
mobius_mesh = mesh.Mesh(data, remove_empty_areas=False)
mobius_mesh.x[:] = xyz[:,0]
mobius_mesh.y[:] = xyz[:,1]
mobius_mesh.z[:] = xyz[:,2]
mobius_mesh.save('mysurface.stl')

