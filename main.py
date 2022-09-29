import cv2
import pickle
import cvzone
import numpy as np


# video feed
# cap = cv2.VideoCapture('2.mp4')


with open('carpark3', 'rb') as f:
    poslist = pickle.load(f)

width,height = 60, 30  # this is  changeable


def checkPark(imgProc):
    spaceCounter = 0

    for pos in poslist:
        x,y = pos


        imgCrop = imgDilate[y:y+height, x:x+width]
        # cv2.imshow(str(x*y),imgCrop)
        count = cv2.countNonZero(imgCrop)
        # cvzone.putTextRect(resize,str(count),(x,y+height-3),scale=1.5,thickness=2,offset=0)

        if count <200:
            color = (0,255,0)
            thickness=5
            spaceCounter+=1
        else:
            color = (0,0, 255)
            thickness = 3
        cv2.rectangle(resize, pos, (pos[0] + width, pos[1] + height), color, thickness)

    # cvzone.putTextRect(resize, str(spaceCounter), (100,200), scale=5, thickness=5, offset=20)
    cvzone.putTextRect(resize, f'{spaceCounter}/{len(poslist)}', (180, 100), scale=5, thickness=5, offset=20)

while True:

    # if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
    #     cap.set(cv2.CAP_PROP_POS_FRAMES,0)

    # success, img = cap.read()
    # resize = cv2.resize(img, (1600, 1050))
    img = cv2.imread('2.jpg')
    resize = cv2.resize(img, (1610, 950))
    imgGray = cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(3,3),10)
    imgThreshold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    imgMedian = cv2.medianBlur(imgThreshold,5)

    kernel = np.ones((3,3),np.uint8)
    imgDilate = cv2.dilate(imgMedian,kernel, iterations=1)

    checkPark(imgDilate)

    # for pos in poslist:
    #     cv2.rectangle(resize, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 4)


    cv2.imshow('img',resize)
    # cv2.imshow('img blur', imgBlur)
    # cv2.imshow('imgThreshold', imgThreshold)
    # cv2.imshow('imgMedian', imgMedian)
    cv2.waitKey(10)
