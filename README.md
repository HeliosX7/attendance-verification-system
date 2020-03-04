
# Attendance Verification System | Face Detection and Recognition 👥
---

## Group Information

* Amulya Ratna Mishra

* Angshuman Saikia

* Kanhu Hembram

* Nikhil Hembram

* Rahul Kumar

* Sujit Brajabasi

---

## Problem Statement

In attendance system using picture of a single person at a time, it might be possible that the system can be easily misguided by a picture. It is also possible that for consecutive scheduled events, the person might have to appear in front of camera for multiple times, the situation become worse when there are large number of people. In this project, solution is based on fact that entire group can mark their attendance without being bothered by taking picture of group and running face-recognition to mark their presence. The system also eliminates the requirement to be arranged in a desired order.

---

## Workflow

<img src="https://github.com/HeliosX7/attendance-verification-system/blob/master/images/workflow.JPG" width="350">

---

## Solution Overview

### Collection of data:
* We used the VGG-Face dataset.
* We also made a program to create custom face recognition dataset.
* This was done by using opencv to capture frames at different time intervals during the video stream.
### Face Detection & Image Processing :
* Used dlib’s CNN based frontal face detector along with opencv to detect the faces and crop them into 200X200 pixels.
*  We also added padding the images when required. 
* We also converted the RGB image into grayscale.
### Face Recognition :
* For the recognition part we opted to train a Convolutional Neural Network.
* The model we used is VGG-Face Model.
* It has 16 layers comprising of 75M parameters.
* The model architecture is a linear sequence of layer transformations of the following types: Convolution + ReLU activations, MaxPooling, Softmax.
* We also have implemented Keras Image Data Generator for augmenting more training samples.

---

## References & Dataset

[Dataset Link](https://www.robots.ox.ac.uk/~vgg/data/vgg_face/)