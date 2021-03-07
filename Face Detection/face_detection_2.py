#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 21:46:53 2021

@author: altair
"""

from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from mtcnn.mtcnn import MTCNN

# draw each face seperately
def draw_faces(filename, result_list):
    #load the image
    data = pyplot.imread(filename)
    # plot each faces as subplot
    for i in range(len(result_list)):
        # get coordinates
        x1, y1, width, height =  result_list[i]['box']
        x2, y2 = x1+width, y1+height
    # define subplot
        pyplot.subplot(1, len(result_list), i+1)
        pyplot.axis('off')
        # plot face
        pyplot.imshow(data[y1:y2, x1:x2])
        #show the plot
        pyplot.show()
        
filename = 'test2.jpg'
# load the image from the file
pixels = pyplot.imread(filename)
# create the detector, using default weights
detector = MTCNN()
# detect faces in the image
faces = detector.detect_faces(pixels)
# display faces on the original image
draw_faces(filename, faces)
        