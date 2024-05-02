import numpy as np
import open3d as o3d

# Load point cloud
points = np.loadtxt('../point_cloud.xyz')
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)

# Visualize the point cloud
o3d.visualization.draw_geometries([pcd])

