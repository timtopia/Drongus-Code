import numpy as np
import cv2

im = cv2.VideoCapture(0)

def isolateRed(src):
        lower = np.array([1, 32, 100])
        upper = np.array([75,75, 255])
        mask = cv2.inRange(src, lower, upper)
        output = cv2.bitwise_and(src, src, mask = mask)
        return output

while(True):
        ret, frame = im.read()
        red = isolateRed(frame)
        imgray = cv2.cvtColor(red, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, 0, 255, 0)
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #vid = cv2.drawContours(red, contours, -1, (0,255,0), 3)
        
        try:
                circles = cv2.HoughCircles(imgray, cv2.HOUGH_GRADIENT, 1, 500, param1 = 50, param2 = 30, minRadius = 0, maxRadius = 0)
                circles = np.uint16(np.around(circles))
                x_values = []
                y_values = []
                radii = []
                for i in circles[0,:]:
                        cv2.circle(red, (i[0],i[1]),i[2], (0,255,0),2) # Outline
                        cv2.circle(red, (i[0],i[1]),2, (0,0,255),3) # Center
                        x = i[0]
                        y = i[1]
                        radius = i[2]
                        x_values.append(x)
                        y_values.append(y)
                        radii.append(radius)
                avg_x = int(sum(x_values) / len(x_values))
                avg_y = int(sum(y_values) / len(y_values))
                avg_r = int(sum(radii) / len(radii))
                cv2.circle(red, (avg_x,avg_y),avg_r, (0,255,255),2) # Outline
                cv2.circle(red, (avg_x,avg_y),2, (0,0,255),3) # Center
        except:                
                print('peepee')
        
        cv2.imshow('hello', red)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                                break
im.release()
cv2.destroyAllWindows()
