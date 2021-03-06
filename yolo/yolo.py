#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 23:25:05 2021

@author: altair
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# load yolo
net = cv2.dnn.readNet('yolov3-tiny.cfg', 'yolov3-tiny.weights')
classes = []
with open('coco.names','r') as f:
    classes = [line.strip() for line in f.readlines()]
print(classes)
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0,255, size=(len(classes),3))

# loading image
image = cv2.imread('test3.jpg')
print(type(image))
#image = cv2.resize(image, None, fx=0.4, fy=0.4)
height, width, channels = image.shape

# detecting objects
blob = cv2.dnn.blobFromImage(image, 0.00392, (416,416), (0,0,0), True, crop = False)
for b in blob:
    for n, img_blob in enumerate(b):
        cv2.imshow(str(n), img_blob)
net.setInput(blob)
outs = net.forward(output_layers)

# showng info on the screen
class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            # object detected
            center_x = int(detection[0]*width)
            center_y = int(detection[1]*height)
            w = int(detection[2]*width)
            h = int(detection[3]*height)
            # rectangles coordinate
            x = int(center_x - w/2)
            y = int(center_y - h/2)
            
            boxes.append([x,y,w,h])
            confidences.append(float(confidence))
            class_ids.append(class_id)
            
indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
print(indexes)
 
font = cv2.FONT_HERSHEY_PLAIN
for i in range(len(boxes)):
    if i in indexes:
      x,y,w,h = boxes[i]
      label = str(classes[class_ids[i]])
      color = colors[i]
      cv2.rectangle(image, (x,y), (x+w, y+h), color,2)
      cv2.putText(image, label, (x, y+30), font, 3, color,3)   
    
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()