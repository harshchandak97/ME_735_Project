import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_range = np.array([0,50,50])
	upper_range = np.array([100,255,255])

	mask = cv2.inRange(hsv, lower_range, upper_range)

	cv2.imshow('Masked', mask)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()

#Callibrate to detect any color
#Have HSV - Hue Saturation and Value bars
#Track its movement 