import numpy as np
import cv2

im = cv2.VideoCapture(0)

def isolateRed(src):
	lower = np.array([60, 60, 100])
	upper = np.array([75,75, 255])
	mask = cv2.inRange(src, lower, upper)
	output = cv2.bitwise_and(src, src, mask = mask)
	return output

while(True):
	ret, frame = im.read()
	frame = isolateRed(frame)
	imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	ret, thresh = cv2.threshold(imgray, 90, 255, 0)
	im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	vid = cv2.drawContours(frame, contours, -1, (0,255,0), 3)
	cv2.imshow('vid',imgray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
im.release()
cv2.destroyAllWindows()
