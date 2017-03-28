#reads frames from camera. if s is pressed, show the last frame. click on the left upper corner of the nail, then on 
#lower down corner of the nail, then nail image will be saved 
import cv2
#left_up,right_down
import numpy as np
import Config 

#read stream from camera, return frame if 's' is pressed
def getFrameFromCamera():
    name_window = 'camera window'
    cv2.namedWindow(name_window)
    cap = cv2.VideoCapture(0)
    ret, frame_from = cap.read()
    output = []
    while(cap.isOpened()):
        ret, frame = cap.read()
        frame  = cv2.flip(frame, -1)
        if ret==True:
            cv2.imshow(name_window,frame)
            cur_key = cv2.waitKey(1) 
            if cur_key == 27:
                break
            if cur_key == ord('s'):
                output = frame
                break
        else:
            break
    # Release everything if job is finished
    cap.release()
    #out.release()
    cv2.destroyAllWindows()
    return output



def setCorners(x, y):
    global corners_x, corners_y, add_frame 
    if (len(corners_x) >= 2):
        corners_x = []
        corners_y = []
        add_frame = np.zeros(add_frame.shape, np.uint8) 
    corners_x.append(x)
    corners_y.append(y)
    if (len(corners_x) == 1):
        cv2.circle(add_frame,(x,y),5,(0,0,255),-1)
    if (len(corners_x) == 2):
        cv2.rectangle(add_frame,(corners_x[0],corners_y[0]),(corners_x[1],corners_y[1]),(0,255,255))

# mouse callback function
def save_corners(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        setCorners(x, y)

    
def setFingerTemplate(big_image, name_template_file):
    global add_frame
    name_window = 'big image'
    cv2.namedWindow(name_window)
    cv2.setMouseCallback(name_window,save_corners)
    add_frame = np.zeros(big_image.shape, np.uint8) 
    while(True):
        frame_with_rect = cv2.add(add_frame, big_image)
        cv2.imshow(name_window,frame_with_rect)
        cur_key = cv2.waitKey(1)
        if cur_key == 27:
            break
        if cur_key == ord('s') and (len(corners_x) == 2):
            template_img = big_image[corners_y[0]:corners_y[1], corners_x[0]:corners_x[1]]
            cv2.imwrite(name_template_file,template_img)
            break
    cv2.destroyAllWindows()

def saveTemplateFile():    
    global corners_x, corners_y, add_frame 
    #x and y coors of corners
    corners_x = []
    corners_y = []
    add_frame = []        
    big_image = getFrameFromCamera()
    print "hi there, everyone!"
    if big_image != []:
        #cv2.imwrite(name_img_full,big_image)
        setFingerTemplate(big_image, Config.TEMPLATE_FILE_FULL)
    

if __name__ == "__main__":
    saveTemplateFile()
    

