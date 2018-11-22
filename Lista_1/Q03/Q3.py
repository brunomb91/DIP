import numpy as np
import cv2

img = cv2.imread("../img/lena.png")
img = np.float32(img)
#img *= 255.0/img.max()

black_img = np.ones((img.shape[0], img.shape[1], 3), dtype=np.uint8)
white_img = np.ones((img.shape[0], img.shape[1], 3), dtype=np.uint8)
white_img *= 255

#img2 = 0.3*img + 0.7*white_img
#img3 = 0.3*img + 0.7*black_img

cv2.imshow("img", img)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)

k = cv2.waitKey(0)

if k == ord('q'):
    cv2.destroyAllWindows()

