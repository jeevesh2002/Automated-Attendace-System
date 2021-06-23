import cv2
import os
def resize():    
    path = input("Enter path of image directory")
    for root, subdir, files in os.walk(path):
        for file in files:
            image_path = os.path.realpath(file)
            image = cv2.imread(f"initial_assets/{file}",cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(image, dsize=[250,250])
            cv2.imwrite(f"final_assets/resized_{file}",resized_image)
            


