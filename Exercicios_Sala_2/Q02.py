import numpy as np
import cv2

img = cv2.imread("messi.jpg", cv2.IMREAD_COLOR)
img2 = cv2.imread("opencv_logo.png", cv2.IMREAD_COLOR)
img3 = cv2.resize(img, (img2.shape[1],img2.shape[0]))

print img2.shape
print img3.shape

img2_not = cv2.bitwise_not(img2)
bitwise_and = cv2.bitwise_and(img2, img3)
bitwise_or = cv2.bitwise_or(img2, img3)
bitwise_xor = cv2.bitwise_xor(img2, img3)

cv2.imshow("img2_not", img2_not)
cv2.imshow("bitwise_and", bitwise_and)
cv2.imshow("bitwise_or", bitwise_or)
cv2.imshow("bitwise_xor", bitwise_xor)

k = cv2.waitKey(0)

if k == ord("q"):
    cv2.destroyAllWindows()
