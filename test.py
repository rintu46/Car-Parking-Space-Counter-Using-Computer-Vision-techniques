import cv2
import pickle
import cvzone
import numpy as np


# video feed
cap = cv2.VideoCapture('vdo.mp4')
img = cv2.imread('1.jpg')


with open('carpark2', 'rb') as f:
    poslist = pickle.load(f)

width,height = 100, 240  # this is  changeable


def checkPark(imgProc):
    for pos in poslist:
        x,y = pos


        imgCrop = imgDilate[y:y+height, x:x+width]
        # cv2.imshow(str(x*y),imgCrop)
        count = cv2.countNonZero(imgCrop)
        cvzone.putTextRect(resize,str(count),(x,y+height-3),scale=1.5,thickness=2,offset=0)

        # if count <2000:
        #     color = (0,255,0)
        #     thickness=5
        # else:
        #     color = (0,0, 255)
        #     thickness = 3
        # cv2.rectangle(resize, pos, (pos[0] + width, pos[1] + height), color, thickness)

while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)

    success, img = cap.read()
    resize = cv2.resize(img, (1600, 1050))
    imgGray = cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(3,3),10)
    imgThreshold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    imgMedian = cv2.medianBlur(imgThreshold,5)

    kernel = np.ones((3,3),np.uint8)
    imgDilate = cv2.dilate(imgMedian,kernel, iterations=1)

    checkPark(imgDilate)

    for pos in poslist:
        cv2.rectangle(resize, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 4)


    cv2.imshow('img',resize)
    # cv2.imshow('img blur', imgBlur)
    # cv2.imshow('imgThreshold', imgThreshold)
    # cv2.imshow('imgMedian', imgMedian)    cv2.waitKey(90)
