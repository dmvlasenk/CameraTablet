#recognize finger 
import cv2

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_SETTINGS, 0);
cap.release()
cv2.destroyAllWindows()