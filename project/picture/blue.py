import numpy as np
import cv2

img = cv2.imread('deep blue.jpg')

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_red = np.array([92,100,160])
upper_red = np.array([120,255,255])

mask1 = cv2.inRange(hsv, lower_red, upper_red)
res2 = cv2.bitwise_and(img,img, mask= mask1)

#kernel = np.ones((8,8),np.uint8)
#opening = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,kernel)


#cv2.imshow('open',opening)
#cv2.imshow('img',img)
cv2.imshow('mask',mask1)
cv2.imshow('res',res2)


#อันนี้ขอบตอน op เเล้วไม่เนียน
