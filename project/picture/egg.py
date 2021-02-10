import numpy as np
import cv2

img = cv2.imread('C:/Users/Admin/Desktop/Project/picture/egg.jpg')

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_red = np.array([5,95,200])
upper_red = np.array([20,170,255])

mask1 = cv2.inRange(hsv, lower_red, upper_red)
res2 = cv2.bitwise_and(img,img, mask= mask1)

kernel = np.ones((5,5),np.uint8)


erosion = cv2.erode(res2,kernel,iterations = 1)


cv2.imshow('erosion',erosion)
#cv2.imshow('closing',closing)
#cv2.imshow('img',img)
cv2.imshow('mask',mask1)
cv2.imshow('res',res2)


