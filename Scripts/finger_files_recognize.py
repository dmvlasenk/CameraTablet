#recognize files reading from files path_full
from os import listdir
from os.path import isfile, join
import cv2
from matplotlib import pyplot as plt

path_from = "C:\Dmitry_Soft\python\opencv_img_from"
template_file = 'te.jpg'
path_full = path_from + '\\full'

template_file_full = path_from + '\\' + template_file
files_full = [f for f in listdir(path_full) if isfile(join(path_full, f))]

# All the 6 methods for comparison in a list
meth ='cv2.TM_CCOEFF_NORMED'


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
   
    
for picture_file in files_full:
    picture_file_full = path_full + '\\' + picture_file 

    img_full_colored = cv2.imread(picture_file_full)
    img_full = cv2.cvtColor(img_full_colored, cv2.COLOR_BGR2GRAY) 
    img_template = cv2.imread(template_file_full, 0)
    [top_left, bottom_right]  = matchTemplate(img_full, img_template, meth)

    cv2.rectangle(img_full,top_left, bottom_right, 255, 2)
    plt.subplot(122),plt.imshow(img_full,cmap = 'gray')
    plt.show()
    print top_left
    