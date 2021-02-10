import numpy as np
import cv2

img = cv2.imread('C:/Users/Admin/Desktop/Project/picture/red.jpg')

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_red = np.array([0,160,130])
upper_red = np.array([5,255,255])

mask1 = cv2.inRange(hsv, lower_red, upper_red)
res2 = cv2.bitwise_and(img,img, mask= mask1)

kernel = np.ones((5,5),np.uint8)

closing = cv2.morphologyEx(res2,cv2.MORPH_CLOSE,kernel)
dilation = cv2.dilate(closing,kernel,iterations = 1)

cv2.imshow('dilation',dilation)
cv2.imshow('closing',closing)
cv2.imshow('img',img)
cv2.imshow('mask',mask1)
cv2.imshow('res',res2)

#อันนี้ถ้าไม่ใช้เทคนิคช่วยอาจจะโอเคละ
