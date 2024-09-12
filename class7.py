import open3d as o3d
import numpy as np
import laspy

# Load the point cloud from the .ply file using Open3D
ply_file_path = "C:/Users/diksh/Desktop/open3d_data/download/BunnyMesh/BunnyMesh.ply"
point_cloud = o3d.io.read_point_cloud(ply_file_path)

# Check if the point cloud has been loaded successfully
print(f"Loaded point cloud has {len(point_cloud.points)} points")

if len(point_cloud.points) == 0:
    print("Error: No points found in the point cloud. Please check the input file.")

def save_as_las(o3d_pcd, output_file):
    # Convert Open3D point cloud to numpy array (XYZ)
    points = np.asarray(o3d_pcd.points)
    
    if points.size == 0:
        print("No points available to save.")
        return

    # Create a LAS header
    header = laspy.LasHeader(point_format=3, version="1.2")
    
    # Create a LAS data object with the header
    las_data = laspy.LasData(header)
    
    # Assign the points
    las_data.x = points[:, 0]
    las_data.y = points[:, 1]
    las_data.z = points[:, 2]

    # Write to the .las file
    las_data.write(output_file)

# Now call the function with the loaded point cloud and output file path
save_as_las(point_cloud, "output_fileNewFragment.las")
