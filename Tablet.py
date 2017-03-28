# -*- coding: utf-8 -*-
#class, storing information about corners of the tablet
#left_up,right_up,right_down,left_down
import numpy as np
import cv2 

from Mouse import *
from PositionCalculator import *
import Config 


# mouse callback function (can't be a part of classs TTablet)
def saveTabletCorners(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        TTablet.m_CornersX.append(x)
        TTablet.m_CornersY.append(y)
        cv2.circle(TTablet.m_AddFrame,(x,y),5,(0,0,255),-1)
               
     
class TTablet:     
    #x and y coors of corners
    m_CornersX = []
    m_CornersY = []
    m_AddFrame = [] #<frame for the additional points on the tablet corners
    m_Mouse = None
    m_IsOn = True

    def __init__(self):
        self.m_Mouse = TMouse()
        self.m_IsOn = True
        
    def setCorners(self):
        name_window = 'Set Corners'
        cv2.namedWindow(name_window)
        cv2.setMouseCallback(name_window, saveTabletCorners)
        cap = cv2.VideoCapture(0)
        ret, frame_from = cap.read()
        TTablet.m_CornersX = []
        TTablet.m_CornersY = []
        TTablet.m_AddFrame = np.zeros(frame_from.shape, np.uint8) 
        #print ("start setCorners")
                   
        while(cap.isOpened()):
            ret, frame_from = cap.read()
            frame_from  = cv2.flip(frame_from, -1)
            frame = cv2.add(TTablet.m_AddFrame, frame_from)
            if ret==True:
                cv2.imshow(name_window,frame)
                #print ("fasdfasdf")
                if cv2.waitKey(1) & (len(TTablet.m_CornersX) > 3):
                    break
            else:
                break
        # Release everything if job is finished
        cap.release()
        #out.release()
        cv2.destroyAllWindows()
    
    def addRectangulars(self, frame_from, corners_arr):
        add_frame = np.zeros(frame_from.shape, np.uint8) 
        cv2.polylines(add_frame,[corners_arr],True,(0,255,255))
        frame = cv2.add(add_frame, frame_from)
        return frame 
    
    def matchTemplate(self, img_full, img_template, aMeth):
        w, h = img_template.shape[::-1]
        img = img_full.copy()
        # Apply template Matching
        method = eval(aMeth)
        res = cv2.matchTemplate(img,img_template,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        return [top_left, bottom_right]
    
    def findFinger(self, aFrame, aImgTemplate, aMeth):   
        img_full = cv2.cvtColor(aFrame, cv2.COLOR_BGR2GRAY) 
        [top_left, bottom_right]  = self.matchTemplate(img_full, aImgTemplate, aMeth)
        cv2.rectangle(aFrame, top_left, bottom_right, 255, 2)
        return top_left
        # plt.subplot(122),plt.imshow(img_full,cmap = 'gray')
        # plt.show()
        #print top_left    
        
    def click(self, aButtonNamee= "left"):
         if self.m_IsOn==True:
             self.m_Mouse.click(button_name=aButtonNamee) 
       
        
    def turnOnOff(self):    
        self.m_IsOn = not self.m_IsOn; 
        #print("Tablet.m_IsOn", self.m_IsOn)
        
    def showTablet(self):   
        cap = cv2.VideoCapture(0)
        img_template = cv2.imread(Config.TEMPLATE_FILE_FULL, 0)
        corners_arr = np.array([TTablet.m_CornersX, TTablet.m_CornersY])
        corners_arr = corners_arr.T.reshape((-1,1,2))
        #mouse = TMouse()
        pos_calculator = TPositionCalculator(TTablet.m_CornersX, TTablet.m_CornersY)
        name_window = 'Tablet'
        while(cap.isOpened()):
            ret, frame = cap.read()
            frame  = cv2.flip(frame, -1)
            finger_position = self.findFinger(frame, img_template, Config.RECOGNIZE_METHOD)
            mouse_pos = pos_calculator.calculateMousePosition(finger_position)
            #print(finger_position, mouse_pos, "ttt")
            if self.m_IsOn==True:
                self.m_Mouse.move_mouse(mouse_pos)
            frame_with_rect = self.addRectangulars(frame, corners_arr)    
            cv2.imshow(name_window,frame_with_rect)
            if ret==True:
                cur_key = cv2.waitKey(10)
                if cur_key ==27:    # Esc key to stop
                    break
            else:
                break
        
        # Release everything if job is finished
        cap.release()
        cv2.destroyAllWindows()        

if __name__ == '__main__':
    tablet = TTablet()
    tablet.setCorners()
    tablet.showTablet()
    tablet.click()
    tablet.turnOnOff()


     