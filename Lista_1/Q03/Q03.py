import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("img/lena.png")

hist,_ = np.histogram(img.ravel(),256,[0,256])

plt.plot(np.arange(256), hist);plt.show()

"""
cv2.imwrite("black_img.png", img)
cv2.imwrite("gray_img.png", img2)

k = cv2.waitKey(0)

if k == ord('q'):
    cv2.destroyAllWindows()
"""
