import numpy as np
import cv2

img = cv2.imread("lena.png", cv2.IMREAD_COLOR)
img2 = cv2.imread("messi.jpg", cv2.IMREAD_COLOR)
img2 = cv2.resize(img2, (img.shape[0], img.shape[1]))

cv2.imshow("sub", img-img2)

k = cv2.waitKey(0)

if k == ord("q"):
    cv2.destroyAllWindows()
