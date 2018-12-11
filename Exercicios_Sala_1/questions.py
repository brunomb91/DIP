import cv2
import numpy as np

"""
# Somar duas imagens multiplicando por uma constante
img1 = cv2.imread("lena.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("messi.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img2, (img1.shape[0], img1.shape[1]))

cv2.imshow("img1", (img1 + img2)*5)
# cv2.imshow("img2", img2)

k = cv2.waitKey(0)

if k == ord("q"):
    cv2.destroyAllWindows()
"""

"""
# Somar o maximo de duas imagens
img1 = cv2.imread("lena.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("messi.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img2, (img1.shape[0], img1.shape[1]))

img3 = cv2.max(img1, img2)

cv2.imshow("img3", (img3))
# cv2.imshow("img2", img2)

k = cv2.waitKey(0)

if k == ord("q"):
    cv2.destroyAllWindows()
"""

"""
# Diferenciacao absoluta
img1 = cv2.imread("lena.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("messi.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img2, (img1.shape[0], img1.shape[1]))

img3 = cv2.absdiff(img1, img2)

cv2.imshow("img3", img3)

k = cv2.waitKey(0)

if k == ord("q"):
    cv2.destroyAllWindows()
"""

# Transformacoes Geometricas: stretch, rotation, resize
img1 = cv2.imread("lena.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("messi.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img2, (img1.shape[0], img1.shape[1]))

M = cv2.getRotationMatrix2D((img2.shape[0]/2, img2.shape[1]/2), 180, 1.0)
img3 = cv2.warpAffine(img2, M, (img2.shape[0], img2.shape[1]))

cv2.imshow("img3", img3)
cv2.imshow("img2", img2)
k = cv2.waitKey(0)

if k == ord("q"):
    cv2.destroyAllWindows()


