import numpy as np
import cv2
import argparse

cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()
	
	lower = np.array([17, 15, 100])
	upper = np.array([75,75, 255])
	mask = cv2.inRange(frame, lower, upper)
	output = cv2.bitwise_and(frame, frame, mask = mask)

	
	cv2.imshow('frame',output)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
cap.release()
cv2.destroyAllWindows()
