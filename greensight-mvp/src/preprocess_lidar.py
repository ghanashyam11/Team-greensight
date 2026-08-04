import laspy
import numpy as np
import open3d as o3d

def load_lidar(file_path):
    lidar = laspy.read(file_path)
    points = np.vstack((lidar.x, lidar.y, lidar.z)).transpose()
    return points

def visualize_lidar(points):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    o3d.visualization.draw_geometries([pcd])

def compute_canopy_metrics(points):
    z = points[:, 2]
    canopy_height = z.max() - z.min()
    density = len(points) / ((points[:,0].ptp()) * (points[:,1].ptp()))
    return canopy_height, density

if __name__ == "__main__":
    pts = load_lidar("data/forest_sample.las")
    h, d = compute_canopy_metrics(pts)
    print(f"Canopy Height: {h:.2f}m | Density: {d:.4f} pts/m²")
    visualize_lidar(pts)
