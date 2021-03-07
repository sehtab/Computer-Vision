# Face Detection

This project is a Computer vision project which will detect faces in a photo frame.'Face_detection.py'  is an opencv project. 'face_detection_1.py' and 'face_detection_2.py' are Deep learning projects.
In this project:
* Face is detected in a non-trivial computer vision problem for identifying and localizing faces in images
* Face detection is performed using cascade classifier using the OpenCV library.
* Face detection is achieved using a Multi-task Cascade CNN via the MTCNN library.

## Face detection Using OpenCV

Classifier Cascade face detection algorithm is used. The benefit of this implementation is the model provides pre-trained face detection models and provides an interface to train a model on user's dataset.

## Face Detection using Deep Learning

In this program Multi-Task Cascaded Convolution Neural Network (MTCNN) is used. Rhe network uses a cascade structure with three networks;  first the image is rescaled, second model filters the bounding box and third model proposes facial landmarks.'face_detection_1.py' using deep learning detect face on image. 'face_detection_2.py' also uses deep learning and after face detection return face images.

