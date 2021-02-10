import numpy as np
import cv2

img = cv2.imread('C:/Users/Admin/Desktop/Project/picture/yellow.jpg')

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_red = np.array([20,100,192])
upper_red = np.array([50,255,255])

mask1 = cv2.inRange(hsv, lower_red, upper_red)
res2 = cv2.bitwise_and(img,img, mask= mask1)

kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(res2,cv2.MORPH_OPEN,kernel)


cv2.imshow('mask1',mask1)
cv2.imshow('res2',res2)
cv2.imshow('opening',opening)
