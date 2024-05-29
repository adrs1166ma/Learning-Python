import cv2
import numpy as np

# img1 = np.zeros((200,300), np.uint8)
# img2 = np.ones((200,300), np.uint8)
#
# cv2.imshow('imgZEROS', img1)
# cv2.imshow('imgONES', img2)
#

img = cv2.imread('alpaca.jpg')
imgGris = cv2.imread('alpaca.jpg',0)

cv2.imshow('imgBGR', img)
cv2.imshow('imgGris', imgGris)
cv2.waitKey(0)
cv2.destroyAllWindows()