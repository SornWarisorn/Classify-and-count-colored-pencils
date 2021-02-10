import numpy as np
import cv2

img = cv2.imread('black.jpg')

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_red = np.array([100,0,0])
upper_red = np.array([130,255,78])

mask1 = cv2.inRange(hsv, lower_red, upper_red)
res2 = cv2.bitwise_and(img,img, mask= mask1)

kernel = np.ones((7,7),np.uint8)

closing = cv2.morphologyEx(mask1,cv2.MORPH_CLOSE,kernel)
erosion = cv2.erode(closing,kernel,iterations = 2)


cv2.imshow('erosion',erosion)
cv2.imshow('closing',closing)
cv2.imshow('img',img)
cv2.imshow('mask',mask1)
cv2.imshow('res',res2)

#อันนี้ตอน ero เเล้วมันเล็กลงเยอะไปหน่อย
