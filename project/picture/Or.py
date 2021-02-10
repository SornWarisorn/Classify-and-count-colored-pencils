import numpy as np
import cv2

img = cv2.imread('C:/Users/Admin/Desktop/Project/picture/Or.jpg')

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_red = np.array([5,160,100])
upper_red = np.array([20,255,255])

mask1 = cv2.inRange(hsv, lower_red, upper_red)
res2 = cv2.bitwise_and(img,img, mask= mask1)

kernel = np.ones((9,9),np.uint8)

opening = cv2.morphologyEx(res2,cv2.MORPH_OPEN,kernel)



cv2.imshow('open',opening)
#cv2.imshow('ero',erosion)
cv2.imshow('img',img)
cv2.imshow('mask',mask1)
cv2.imshow('res',res2)


