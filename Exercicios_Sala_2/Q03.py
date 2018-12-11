import numpy as np
import cv2

img = cv2.imread("lena.png", cv2.IMREAD_COLOR)
img2 = cv2.imread("messi.jpg", cv2.IMREAD_COLOR)
img2 = cv2.resize(img2, (img.shape[0], img.shape[1]))
img3 = np.zeros((img.shape[0],img.shape[1]), np.uint8)

"""
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img3[i,j] = cv2.max(img[i,j], img2[i,j])
"""

cv2.imshow("new_img", cv2.max(img,img2))

k = cv2.waitKey(0)

if k == ord("q"):
    cv2.destroyAllWindows()
