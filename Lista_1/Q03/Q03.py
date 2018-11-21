import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("../img/lena.png")
black_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
white_img = np.ones((img.shape[0], img.shape[1], 3), dtype=np.uint8)

white_img *= 255

#cv2.imshow('img', cv2.max(img, black_img))
#cv2.imshow('img2', cv2.max(img, white_img))

k = cv2.waitKey(0)

if k == ord('q'):
    cv2.destroyAllWindows()

