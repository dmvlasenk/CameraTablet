#recognize finger 

import numpy as np
import cv2
import time

from mouse import *
from PositionCalculator import *

#corners_x = [105, 434, 440, 171]
#corners_y = [132, 160, 303, 280]

path_from = "c:\\Dmitry_Soft\\python\\tablet\\img"
template_file = 'template_finger.jpg'
template_file_full = path_from + '\\' + template_file

name_window = 'camera window'
    
meth ='cv2.TM_CCOEFF_NORMED'


def addRectangulars(frame_from, corners_arr):
    add_frame = np.zeros(frame_from.shape, np.uint8) 
    cv2.polylines(add_frame,[corners_arr],True,(0,255,255))
    frame = cv2.add(add_frame, frame_from)
    return frame 


def matchTemplate(img_full, img_template, meth):
    w, h = img_template.shape[::-1]
    img = img_full.copy()

    # Apply template Matching
    method = eval(meth)
    res = cv2.matchTemplate(img,img_template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return [top_left, bottom_right]

def findFinger(frame, img_template, meth):   
    img_full = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    [top_left, bottom_right]  = matchTemplate(img_full, img_template, meth)

    cv2.rectangle(frame,top_left, bottom_right, 255, 2)
    return top_left
    # plt.subplot(122),plt.imshow(img_full,cmap = 'gray')
    # plt.show()
    #print top_left   

cap = cv2.VideoCapture(0)
img_template = cv2.imread(template_file_full, 0)
corners_arr = np.array([corners_x, corners_y])
corners_arr = corners_arr.T.reshape((-1,1,2))
   
mouse = TMouse()
pos_calculator = TPositionCalculator(corners_x, corners_y)
while(cap.isOpened()):
    ret, frame = cap.read()
    frame  = cv2.flip(frame, -1)
    finger_position = findFinger(frame, img_template, meth)
    mouse_pos = pos_calculator.calculateMousePosition(finger_position)
    print(finger_position, mouse_pos, "ttt")
    mouse.move_mouse(mouse_pos)
    frame_with_rect = addRectangulars(frame, corners_arr)    
    cv2.imshow(name_window,frame_with_rect)

#
#    for i in range(10):
#        x = int(500+math.sin(math.pi*i/100)*500)
#        y = int(500+math.cos(i)*100)
#        p = (x,y)     
#        mouse.move_mouse(p)
    
    
    if ret==True:
        cur_key = cv2.waitKey(10)
        if cur_key ==27:    # Esc key to stop
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()