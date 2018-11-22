import cv2
import numpy as np

img = np.zeros((400,400))
img2 = np.zeros((400,400,3))

img2[:,:,0] = 127
img2[:,:,1] = 127
img2[:,:,2] = 127


cv2.imshow('img2', img2)
cv2.imshow('img', img)

"""
cv2.imwrite("black_img.png", img)
cv2.imwrite("gray_img.png", img2)
"""

k = cv2.waitKey(0)

if k == ord('q'):
    cv2.destroyAllWindows()
