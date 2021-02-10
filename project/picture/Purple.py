import numpy as np
import cv2

img = cv2.imread('C:/Users/Admin/Desktop/Project/picture/vb.jpg')

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_red = np.array([120,50,10])
upper_red = np.array([130,255,255])

mask1 = cv2.inRange(hsv, lower_red, upper_red)
res2 = cv2.bitwise_and(img,img, mask= mask1)

kernel = np.ones((6,6),np.uint8)

opening = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,kernel)


cv2.imshow('opening',opening)
cv2.imshow('img',img)
cv2.imshow('mask',mask1)
cv2.imshow('res',res2)


#ไม่ค่อยเนียนเท่าไหร่
