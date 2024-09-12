import open3d as o3d
import numpy as np

def convert_rcs_to_ply(rcs_file, ply_file):
    # Note: Replace this section with actual RCS reading logic.
    # This is a placeholder for demonstration purposes.

    # Load RCS file (assuming conversion to a format open3d can handle)
    # For demonstration, let's use a dummy point cloud
    points = np.random.rand(1000, 3)  # Dummy data for demonstration
    
    # Create a PointCloud object
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)

    # Save to PLY file
    o3d.io.write_point_cloud(ply_file, pcd)

convert_rcs_to_ply('D:/PointCloudData/Eka_15mm_res_RCS/Eka_15mm_res.rcs', 'output_file.ply')





