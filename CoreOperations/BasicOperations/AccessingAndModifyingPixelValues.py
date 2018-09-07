import cv2
import numpy as np

img = cv2.imread('data/messi5.jpg')

px = img[100, 100]
print(px)

blue = img[100, 100, 0]
print(blue)

# accessing only blue pixel
img[100, 100] = [255, 255, 255]
print(img[100, 100])

# accessing RED value
print(img.item(10, 10, 2))

# modifying RED value
img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))
