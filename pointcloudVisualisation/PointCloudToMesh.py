import numpy as np
import open3d as o3d
#create paths and load data
input_path="PointClouds/"
output_path="MeshOutput/"
dataname="Measurement1.xyz"
point_cloud= np.loadtxt(input_path+dataname)
#Format to open3d usable objects
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(point_cloud[:,:3])
pcd.colors = o3d.utility.Vector3dVector(point_cloud[:,3:6]/255)
#pcd.normals = o3d.utility.Vector3dVector(point_cloud[:,6:9])
o3d.visualization.draw_geometries([pcd])

#radius determination
distances = pcd.compute_nearest_neighbor_distance()
avg_dist = np.mean(distances)
radius = 3 * avg_dist
#computing the mehs
bpa_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(pcd,o3d.utility.DoubleVector([radius, radius * 2]))
#decimating the mesh
dec_mesh = bpa_mesh.simplify_quadric_decimation(100000)
dec_mesh.remove_degenerate_triangles()
dec_mesh.remove_duplicated_triangles()
dec_mesh.remove_duplicated_vertices()
dec_mesh.remove_non_manifold_edges()
o3d.io.write_triangle_mesh(output_path+"bpa_mesh.ply", dec_mesh)