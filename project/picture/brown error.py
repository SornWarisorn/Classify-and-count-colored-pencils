import numpy as np
import cv2

img = cv2.imread('C:/Users/Admin/Desktop/Project/picture/brown.jpg')

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_red = np.array([140,20,20])
upper_red = np.array([255,100,100])

mask1 = cv2.inRange(hsv, lower_red, upper_red)
res2 = cv2.bitwise_and(img,img, mask= mask1)

kernel = np.ones((7,7),np.uint8)

dilation = cv2.dilate(mask1,kernel,iterations = 2)
closing = cv2.morphologyEx(dilation,cv2.MORPH_CLOSE,kernel)



cv2.imshow('dilation',dilation)
cv2.imshow('closing',closing)
cv2.imshow('img',img)
cv2.imshow('mask',mask1)
cv2.imshow('res',res2)

#หาช่วงยากสัดๆ เลยเอ๋อ
