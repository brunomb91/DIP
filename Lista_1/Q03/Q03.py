import cv2
import numpy as np
from matplotlib import pyplot as plt
import copy

def nothing(x):
    pass

cv2.namedWindow('img', cv2.WINDOW_KEEPRATIO)
cv2.namedWindow('img2', cv2.WINDOW_KEEPRATIO)

cv2.createTrackbar("b", "img", 1, 350, nothing)
cv2.createTrackbar("g", "img", 1, 350, nothing)
cv2.createTrackbar("r", "img", 1, 350, nothing)

#const = 2

while True:
    img = cv2.imread("../img/lena.png", cv2.IMREAD_COLOR)
    img2 = copy.deepcopy(img)

    #black_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    #white_img = np.ones((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    #white_img *= 255

    b = cv2.getTrackbarPos('b','img')
    g = cv2.getTrackbarPos('g','img')
    r = cv2.getTrackbarPos('r','img')

    img[:,:,0] *= b
    img[:,:,1] *= g
    img[:,:,2] *= r

    #img2 = img - black_img
    #img3 = img - white_img

    #cv2.imshow('img', img3)
    #cv2.imshow('img2', img2)
    cv2.imshow('img', img)
    cv2.imshow('img2', img2)

    k = cv2.waitKey(0)

    if k == ord('q'):
        cv2.destroyAllWindows()

