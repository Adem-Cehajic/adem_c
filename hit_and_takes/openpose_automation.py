import os
import subprocess
import glob

# Define OpenPose folder locations
openpose_bin = "/home/ademc/openpose/build/examples/openpose/openpose.bin"
all_takes_folder = "/home/ademc/hit_and_takes/all_takes"
openpose_output = "/home/ademc/hit_and_takes/openpose_output"
openpose_folder = "/home/ademc/openpose"  # Path to the OpenPose folder

# Ensure the output folder exists
os.makedirs(openpose_output, exist_ok=True)

# Find all cam02.mp4 files in the all_takes directory
cam02_files = glob.glob(os.path.join(all_takes_folder, "**", "cam02.mp4"), recursive=True)

# Process each cam02.mp4 file
for cam02_file in cam02_files:
    # Extract the parent folder name of the video file (e.g., "cmu_bike01_2")
    parent_folder_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(cam02_file)))))
    video_output_folder = os.path.join(openpose_output, parent_folder_name)
    os.makedirs(video_output_folder, exist_ok=True)

    # Construct the OpenPose command
    openpose_command = [
        openpose_bin,
        "--video", cam02_file,
        "--face",
        "--hand",
        "--write_json", video_output_folder,
        "--display", "0",  # Optional: Disable display window
        "--render_pose", "0",  # Optional: Disable rendering to save computation
        "--frame_last", "0",  # Process only the first frame
        "--net_resolution", "-1x128"  # Set network resolution
    ]

    # Run the command
    print(f"Processing video: {cam02_file}")
    subprocess.run(openpose_command, cwd=openpose_folder, check=True)
    print(f"JSON output saved to: {video_output_folder}")