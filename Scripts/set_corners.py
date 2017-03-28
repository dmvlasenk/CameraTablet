#set corners_x, corners_y - x and y coordinates of coners
#left_up,right_up,right_down,left_down
import numpy as np
import cv2
import os     
     

name_window = 'camera window'

#x and y coors of corners
corners_x = []
corners_y = []

# mouse callback function
def save_corners(event,x,y,flags,param):
    global corners_x, corners_y, img, add_frame

    if event == cv2.EVENT_LBUTTONDOWN:
        corners_x.append(x)
        corners_y.append(y)
        cv2.circle(add_frame,(x,y),5,(0,0,255),-1)
        

cv2.namedWindow(name_window)
cv2.setMouseCallback(name_window,save_corners)


cap = cv2.VideoCapture(0)

ret, frame_from = cap.read()
add_frame = np.zeros(frame_from.shape, np.uint8) 


while(cap.isOpened()):
    ret, frame_from = cap.read()
    frame_from  = cv2.flip(frame_from, -1)
    frame = cv2.add(add_frame, frame_from)
    if ret==True:
        cv2.imshow(name_window,frame)
        if cv2.waitKey(1) & (len(corners_x) > 3):
            break
    else:
        break
# Release everything if job is finished
cap.release()
#out.release()
cv2.destroyAllWindows()

