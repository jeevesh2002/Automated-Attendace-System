import tensorflow as tf
import os
data_dir = os.getcwd()
for root, subdir, files in os.walk(f"{data_dir}/final_assets"):
    image_count = 0
    for file in files:
        image_count = image_count + 1
print(image_count)

