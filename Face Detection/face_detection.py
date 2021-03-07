#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 16:34:46 2021

@author: altair
"""

import cv2
from cv2 import imread
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import CascadeClassifier
from cv2 import rectangle

print(cv2.__version__)

# load the photograph
pixels = imread('test2.jpg')

# load pretrained model
classifier = CascadeClassifier('haarcascade_frontalface_default.xml')


# perform face detection
bboxes = classifier.detectMultiScale(pixels, 1.05, 8)

# print bounding box for each detected face
for box in bboxes:
    # extract
    x, y, width, height = box
    x2, y2 = x + width, y + height
    # draw a rectangle over the pixels
    rectangle(pixels, (x, y), (x2, y2), (0,0,255), 1)
    
# show the image
imshow('face detection', pixels)

# keep the window open until pressing a key
waitKey(0)
# close the window
destroyAllWindows()
    
    