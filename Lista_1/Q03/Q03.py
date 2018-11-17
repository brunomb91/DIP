import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("../img/lena.png")

hist,_ = np.histogram(img.ravel(),256,[0,256])

cdf = hist.cumsum()
"""
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
"""
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

"""
for i in cv2.split(img): 
    hist,_ = np.histogram(i.ravel(),256,[0,256])
    plt.plot(np.arange(256), hist); plt.show()
"""

"""
cv2.imwrite("black_img.png", img)
cv2.imwrite("gray_img.png", img2)
"""

cv2.imshow('img',img)

k = cv2.waitKey(0)

if k == ord('q'):
    cv2.destroyAllWindows()

