import cv2
import numpy as np

img = cv2.imread("../img/baboon.png")
img2 = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if j >= (128) and j <= (384) and i >= (256) and i <= (512):
            img2[i,j] = img2[i,j] + img[i,j]

img3 = img2[256:512, 128:384] 
img3 = cv2.resize(img3, (img.shape[0],img.shape[1]))

cv2.imshow('img', img)
cv2.imshow('img3', img3)

# cv2.imwrite("baboon_result.png", img3)

k = cv2.waitKey(0)

if k == ord('q'):
    cv2.destroyAllWindows()
