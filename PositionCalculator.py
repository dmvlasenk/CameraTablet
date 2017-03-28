#read from 4 courners array and finger position calculate the mouse position 
import math
from operator import itemgetter
import  ctypes
import numpy as np

class TPositionCalculator:
    m_cornersDisplX = []
    m_cornersDisplY = []
    m_CornersArr = []
    m_CountCorners = 0
    m_MousePosition = (1, 1)
    m_CornersX = []
    m_CornersY = []
    m_PolygonNormals = []
    m_Resolution = []    
    
    def getCorner(self, aIndex):
         cur_corner = (self.m_CornersArr[aIndex])[0] 
         return cur_corner
    
    def setPolygonNormals(self):
        self.m_PolygonNormals = []
        for index in range(0, self.m_CountCorners):
             cur_corner = self.getCorner(index) 
             index_prev = self.m_CountCorners-1 if index ==  0 else index-1
             corner_next = self.getCorner(index_prev) 
             polygon_line = corner_next -  cur_corner 
             normal = []             
             if(abs(polygon_line[0]) > abs(polygon_line[1]) ):
                 normal = [polygon_line[1], -polygon_line[0]]
             else:
                 normal = [-polygon_line[1], polygon_line[0]]
             #prove_dot = np.dot(normal, polygon_line)
             #print(cur_corner, corner_next, polygon_line, normal,prove_dot)
             self.m_PolygonNormals.append(normal)

    

    def setCornersArr(self, aCornersX, aCornersY):
        self.m_CornersX = aCornersX
        self.m_CornersY = aCornersY
        self.m_CornersArr  = np.array([aCornersX, aCornersY])
        self.m_CornersArr = self.m_CornersArr.T.reshape((-1,1,2))
        self.m_CountCorners = len(self.m_CornersArr)
        self.setPolygonNormals()
    
    def calcCornersDisplXY(self):
        SM_CXSCREEN = 0
        SM_CYSCREEN = 1
        dist_x = ctypes.windll.user32.GetSystemMetrics(SM_CXSCREEN)
        dist_y = ctypes.windll.user32.GetSystemMetrics(SM_CYSCREEN)
        self.m_Resolution = [dist_x, dist_y]
        self.m_cornersDisplX = [1, dist_x, dist_x, 1]
        self.m_cornersDisplY = [1, 1, dist_y, dist_y]
        #print(dist_x, dist_y, "resolution screen")
        
    def __init__(self, aCornersX, aCornersY):
        self.calcCornersDisplXY()
        self.setCornersArr(aCornersX, aCornersY)
       
    def calculateMousePosition(self, aFingerCoor):
        if not self.isPointInPolygon(aFingerCoor):
              return self.m_MousePosition
        coor_x = self.calcCoordinate(aFingerCoor, 0)
        coor_y = self.calcCoordinate(aFingerCoor, 1)
        self.m_MousePosition = (int(np.round(coor_x)), int(np.round(coor_y)))
        return self.m_MousePosition 
    
    
    def calcDist(self, point0, point1):
        dist_x = point0[0] - point1[0]
        dist_y = point0[1] - point1[1]
        dist = math.sqrt(dist_x * dist_x  + dist_y * dist_y)
        return dist 
        
    def isPointInPolygon(self, aPointPos):
        testx = aPointPos[0]
        testy = aPointPos[1]
        nvert = self.m_CountCorners
        output = False
        for i in range(0, nvert):
            j = nvert-1 if i == 0 else i-1
            bool0 = ((self.m_CornersY[i]>testy) != (self.m_CornersY[j]>testy)) 
            bool1 = (testx < (self.m_CornersX[j]-self.m_CornersX[i]) * (testy-self.m_CornersY[i]) / (self.m_CornersY[j]-self.m_CornersY[i]) + self.m_CornersX[i]) 
            if (bool0  and bool1):
               output = not output
        return output;
      
   
        
         
    def calcLinePointDist(self, aLineOrigin, aLineNormal, aPoint):
        dist = aPoint - aLineOrigin
        norm_dist = np.dot(dist, aLineNormal)
        return abs(norm_dist)
        
    def calcCoordinate(self, aFingerCoor, aIndexCoor):
        index0 = aIndexCoor
        index1 = aIndexCoor + 2
        dist0 = self.calcLinePointDist(self.getCorner(index0), self.m_PolygonNormals[index0], aFingerCoor)
        dist1 = self.calcLinePointDist(self.getCorner(index1), self.m_PolygonNormals[index1], aFingerCoor)
        distances_to_corners = [float(dist0), float(dist1)]
        index_of_min = min(enumerate(distances_to_corners), key=itemgetter(1))[0] 
        min_value = distances_to_corners[index_of_min]
        if(min_value < 1):
            weights_distances = [0.0] * len(distances_to_corners)
            weights_distances[index_of_min] = 1.0 
        else:
            weights_distances_from =  [1/i for i in distances_to_corners]
            #print(distances_to_corners, weights_distances_from,  "sdfsdf")
            weights_distances = [float(i)/sum(weights_distances_from ) for i in weights_distances_from]
        #print(weights_distances)
        
        cur_resolution = self.m_Resolution[aIndexCoor]
        output = cur_resolution * weights_distances[1] #the position of the first line is zero, therefore weights_distances[0] does not matter
        #print(output, "cur_pos")
        return output;

     

if __name__ == '__main__':
    vertx1 = [105, 434, 440, 171]
    verty1 = [132, 160, 303, 280]
    #corners_arr = np.array([[[103, 108]],[[437, 129]], [[451, 286]], [[176, 267]]])
    pos_calculator = TPositionCalculator(vertx1, verty1)
    x_point  = 106
    y_point= 133
    finger_coor = (x_point, y_point)
    mouse_pos = pos_calculator.calculateMousePosition(finger_coor)
    x_point  = 2
    y_point= 2
    mouse_pos2 = pos_calculator.calculateMousePosition(finger_coor)
        