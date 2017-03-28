import cv2

def setCameraProperties():
    name_window = 'Press esc after finish'
    cv2.namedWindow(name_window)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_SETTINGS, 0);
    ret, frame_from = cap.read()
    
    
    while(cap.isOpened()):
        ret, frame_from = cap.read()
        frame = cv2.flip(frame_from, -1)
        if ret==True:
            cv2.imshow(name_window,frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        else:
            break
    # Release everything if job is finished
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    setCameraProperties()