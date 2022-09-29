# import cv2
# import numpy as np
# # Creating mouse callback function
# def draw_circle(event,x,y,flags,param):
#     if(event == cv2.EVENT_LBUTTONDBLCLK):
#             cv2.circle(img,(x,y),100,(255,255, 0),-1)
# # Creating a black image, a window and bind the function to window
# img = cv2.imread('park.jpg')
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_circle)
# while(1):
#     cv2.imshow('image',img)
#     if cv2.waitKey(20) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()




import cv2
import pickle
import numpy as np


def draw_circle(event, x, y, flags, params):
    if (event == cv2.EVENT_LBUTTONDBLCLK):
        cv2.circle(bigger, (x, y), 100, (255, 255, 0), -1)


img = cv2.imread('park.jpg')
bigger = cv2.resize(img, (1610,950))
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
# img = cv2.imread('park.jpg')
# # bigger = cv2.resize(img, (1610,950))
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', mouseClick)

# width,height = 330, 140  # this is  changeable
# poslist = []


        # poslist.append((x,y))

# def mouseClick(events, x,y,flags, params):
#     events = dir(cv2).EVENT_
#     mouse_events = [j for j in dir(cv2) if 'EVENT' in j]
#     print(mouse_events)



while(1):
    cv2.imshow('image',bigger)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

#
