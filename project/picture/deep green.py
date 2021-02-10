import numpy as np
import cv2

img = cv2.imread('C:/Users/Admin/Desktop/Project/picture/deep green.jpg')

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_red = np.array([65,68,40])
upper_red = np.array([85,255,200])

mask1 = cv2.inRange(hsv, lower_red, upper_red)
res2 = cv2.bitwise_and(img,img, mask= mask1)

kernel = np.ones((3,3),np.uint8)
dilation = cv2.dilate(res2,kernel,iterations = 1)



cv2.imshow('dilation',dilation)
cv2.imshow('img',img)
cv2.imshow('mask',mask1)
cv2.imshow('res',res2)


#ถ้าไม่ใช้ dil ก็โอเคอยู่ เลือกเอา
