import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while (1):
    _, frame = cap.read()

    kernel = np.ones((5, 5), np.float32) / 25
    dst = cv2.filter2D(frame, -1, kernel)

    cv2.imshow('Original', frame)
    cv2.imshow('Averaging', dst)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
