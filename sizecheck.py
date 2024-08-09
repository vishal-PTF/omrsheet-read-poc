import cv2
import os

# Get the directory where OpenCV is installed
opencv_dir = os.path.dirname(cv2.__file__)

# Calculate the total size of the OpenCV directory
total_size = 0
for dirpath, dirnames, filenames in os.walk(opencv_dir):
    for f in filenames:
        fp = os.path.join(dirpath, f)
        total_size += os.path.getsize(fp)

# Convert the size to MB
total_size_mb = total_size / (1024 * 1024)

print(f"OpenCV library size: {total_size_mb:.2f} MB")
