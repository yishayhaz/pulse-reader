import cv2
import numpy as np

def multi_clahe(img, num):
    # create a CLAHE object
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

    # apply CLAHE to the input image
    cl1 = clahe.apply(img)

    for i in range(num):
        cl1 = clahe.apply(cl1)

    return cl1

def image_map():
    img = cv2.imread('photos/hand.jpg')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    result = multi_clahe(gray, 2)

    cv2.imshow('Result', result)
    cv2.waitKey(0)

image_map()