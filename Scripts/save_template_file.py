import cv2
#left_up,right_up,right_down,left_down
import numpy as np

PATH_IMG = "c:\\Dmitry_Soft\\python\\tablet\\img"
TEMPLATE_FILE = 'template_finger.jpg'
TEMPLATE_FILE_FULL = PATH_IMG + '\\' + TEMPLATE_FILE

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


#x and y coors of corners
corners_x = []
corners_y = []
add_frame = []

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
    

            
big_image = getFrameFromCamera()
if big_image != []:
    #cv2.imwrite(name_img_full,big_image)
    setFingerTemplate(big_image, TEMPLATE_FILE_FULL)
    

