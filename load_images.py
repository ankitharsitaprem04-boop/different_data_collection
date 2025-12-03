
import cv2
import os

images = []
path = "C:/Users/KIIT0001/OneDrive/Desktop/images"



for file in os.listdir(path):
    img = cv2.imread(os.path.join(path, file))
    images.append(img)

print("Loaded", len(images), "images")

