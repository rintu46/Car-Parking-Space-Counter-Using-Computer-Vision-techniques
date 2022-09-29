import cv2
import pickle
import numpy as np


# width,height = 100, 240  # this is  changeable
# width,height = 290, 190
width,height = 60, 30


# poslist = []

try:
    with open('carpark3', 'rb') as f:
        poslist = pickle.load(f)
except:
    poslist = []


def draw_circle(event, x, y, flags, params):
    if (event == cv2.EVENT_LBUTTONDBLCLK):
        poslist.append((x,y))

    if (event == cv2.EVENT_RBUTTONDBLCLK):
        for i,pos in enumerate(poslist):
            x1,y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                poslist.pop(i)

    with open('carpark3', 'wb') as f:
        pickle.dump(poslist,f)


while(1):
    img = cv2.imread('2.jpg')
    bigger = cv2.resize(img, (1610, 950))
    # a1 = [(2096, 1244), (236, 1144), (188, 1684), (212, 1612)]
    # a2 = [(800, 550), (430, 550), (520, 392), (825, 350)]
    # a3 = [(648, 343), (596, 213), (437, 218), (324, 352)]
    # for pos in poslist:
    #     for area in [a2]:
    #         cv2.polylines(bigger, [np.array(area, np.int32)], True, (15, 220, 10), 6)
    for pos in poslist:
        cv2.rectangle(bigger, pos, (pos[0]+width, pos[1]+height), (255,0,255),2)

    cv2.imshow('image',bigger)
    cv2.setMouseCallback('image', draw_circle)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

# cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_circle)











