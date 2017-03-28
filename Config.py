# -*- coding: utf-8 -*-
#config file
import cv2 

PATH_IMG = "c:\\temp"
TEMPLATE_FILE = 'template_finger.jpg'
TEMPLATE_FILE_FULL = PATH_IMG + '\\' + TEMPLATE_FILE
RECOGNIZE_METHOD = 'cv2.TM_CCOEFF_NORMED' 
HOTKEY_CLICK_LEFT = 'alt+shift+1'
HOTKEY_CLICK_RIGHT = 'alt+shift+2'
HOTKEY_TURN_TABLET = 'alt+shift+q'