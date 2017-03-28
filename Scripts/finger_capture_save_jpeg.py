#read from camera frames and save them in folder \img as jpeg if 'c' is pressed

import numpy as np
import cv2
import time

path_to = "c:\\Dmitry_Soft\\python\\tablet\\img"
name_window = 'camera window'
    
cap = cv2.VideoCapture(0)

count_frames = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    frame  = cv2.flip(frame, -1)
    cv2.imshow(name_window,frame)
    if ret==True:
        cur_key = cv2.waitKey(1)
        if cur_key ==27:    # Esc key to stop
            break
        elif cur_key==ord('c'):  
            count_frames += 1 
            name_img_to_full = path_to + '\\finger'  + str(count_frames) + ".jpg"   
            cv2.imwrite(name_img_to_full,frame)        
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()