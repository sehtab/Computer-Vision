#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 14:57:02 2021

@author: altair
"""

from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from mtcnn.mtcnn import MTCNN

# draw an image with detected object
def draw_image_with_box(filename, result_list):
    #load the image
    data = pyplot.imread(filename)
    # plot the image
    pyplot.imshow(data)
    # get the context for drawing box
    ax = pyplot.gca()
    # plot each box
    for result in result_list:
        # get coordinates
        x, y, width, height = result['box']
        # create the shape
        rect = Rectangle((x, y), width, height, fill=False, color='red')
        #draw the box
        ax.add_patch(rect)
        # draw the dots
    for key, value in result['keypoints'].items():
            # create and draw dot
        dot = Circle(value, radius=2, color='red')
        ax.add_patch(dot)
            # show the plot
    pyplot.show()
            
filename = 'test1.jpg'
# load image from the file
pixels = pyplot.imread(filename)
# create the detector, using default weights
detector = MTCNN()
# detect faces in the image
faces = detector.detect_faces(pixels)
# display faces on the original image
draw_image_with_box(filename, faces)
        