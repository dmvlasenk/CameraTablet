import numpy as np
import cv2
import os     
name_window = 'camera window'

def addRectangulars(frame_from, corners_arr):
    add_frame = np.zeros(frame_from.shape, np.uint8) 
    cv2.polylines(add_frame,[corners_arr],True,(0,255,255))
    frame = cv2.add(add_frame, frame_from)
    return frame 


cv2.namedWindow(name_window)
cap = cv2.VideoCapture(0)

ret, frame_from = cap.read()

corners_arr = np.array([corners_x, corners_y])
corners_arr = corners_arr.T.reshape((-1,1,2))

while(cap.isOpened()):
    ret, frame_from = cap.read()
    frame_from  = cv2.flip(frame_from, -1)
    frame = addRectangulars(frame_from, corners_arr)
    if ret==True:
        cv2.imshow(name_window,frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break
# Release everything if job is finished
cap.release()
#out.release()
cv2.destroyAllWindows()

