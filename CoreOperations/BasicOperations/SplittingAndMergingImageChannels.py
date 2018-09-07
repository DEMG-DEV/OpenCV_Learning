import cv2
import numpy as np

img = cv2.imread('data/messi5.jpg')

b, g, r = cv2.split(img)

# print image-b
cv2.imshow('Image-b', b)
cv2.waitKey(0)
cv2.destroyAllWindows()

# print image-g
cv2.imshow('Image-g', g)
cv2.waitKey(0)
cv2.destroyAllWindows()

# print image-r
cv2.imshow('Image-r', r)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.cv2.merge((b, g, r))
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
