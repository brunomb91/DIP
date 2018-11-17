import cv2
import numpy as np

img = cv2.imread("img/baboon.png")

cv2.imshow('img', img)

# cv2.imwrite("black_img.png", img)

k = cv2.waitKey(0)

if k == ord('q'):
    cv2.destroyAllWindows()
