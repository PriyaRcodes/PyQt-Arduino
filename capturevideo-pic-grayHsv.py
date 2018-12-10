'''
To capture an image from live video and convert it to HSV and GrayScale using OpenCV
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)                          #Using the default camera

while True:
    ret, frame = cap.read()
    cv2.imshow('Video',frame)
    k = cv2.waitKey(5)                             #pauses for 5 milliseconds between frames
    
    if k==27:
        returnvalue,img = cap.read()               #captures the image when you press Esc
        break

cv2.imshow('image',img)                            #Displaying that image

imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)       #Converting original color image to HSV
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)     #Converting original color image to Gray scale

f1 = plt.figure()
plt.imshow(imgHSV,cmap = 'hsv')
f1.show()

f2 = plt.figure()
plt.imshow(imgGray,cmap = 'gray',interpolation='bicubic')
f2.show()

cap.release()                                      #Releasing capture
cv2.destroyWindow('Video')                         #To close the Video 
