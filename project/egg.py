import cv2
import numpy as np

img = cv2.imread('egg.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([12,60,150])
upper_blue = np.array([17,185,255])

mask = cv2.inRange(hsv,lower_blue,upper_blue)

res = cv2.bitwise_and(img,img,mask = mask)



cv2.imshow('res image', res)
