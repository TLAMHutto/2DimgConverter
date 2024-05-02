import numpy as np
import cv2

# Load depth map
depth_map = cv2.imread('../motocyclePic.png', cv2.IMREAD_UNCHANGED)
if len(depth_map.shape) > 2:  # Check if the image has more than one channel
    depth_map = depth_map[:, :, 0]  # Use the first channel assuming it contains the depth information

# Assumed camera intrinsics
width, height = depth_map.shape[1], depth_map.shape[0]
f_x = width / 2
f_y = height / 2
c_x = width / 2
c_y = height / 2

# Create a meshgrid of pixel coordinates
x = np.linspace(0, width - 1, width)
y = np.linspace(0, height - 1, height)
x, y = np.meshgrid(x, y)

# Convert to 3D coordinates
Z = depth_map.astype(float)
X = (x - c_x) * Z / f_x
Y = (y - c_y) * Z / f_y

# Reshape and stack to create point cloud
points = np.stack((X, Y, Z), axis=-1).reshape(-1, 3)

# Save to file (optional)
np.savetxt('../point_cloud.xyz', points, fmt='%f')

print("Point cloud saved as point_cloud.xyz")
