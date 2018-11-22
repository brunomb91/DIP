import numpy as np
import cv2

x = 1
y = 120

img = cv2.imread("../img/lena.png")

black_img = np.ones((img.shape[0], img.shape[1], 3), dtype=np.uint8)
white_img = np.ones((img.shape[0], img.shape[1], 3), dtype=np.uint8)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        for k in range(img.shape[2]):
            white_img[i,j,k] = np.clip(x*img[i,j,k] + y, 0, 255)
            black_img[i,j,k] = np.clip(x*img[i,j,k] - y, 0, 255)

"""
cv2.imwrite("results/lena_white.png", white_img)
cv2.imwrite("results/lena_black.png", black_img)
"""

cv2.imshow("img", img)
cv2.imshow("img2", white_img)
cv2.imshow("img3", black_img)

k = cv2.waitKey(0)

if k == ord('q'):
    cv2.destroyAllWindows()

