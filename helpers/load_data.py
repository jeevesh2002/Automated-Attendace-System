import tensorflow as tf
import os
# for finding number of images
data_dir = os.getcwd()
for root, subdir, files in os.walk(f"{data_dir}/final_assets"):
    image_count = sum(1 for _ in files)
print(image_count)

