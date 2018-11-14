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
        ret, thresh = cv2.threshold(imgray, 128, 255, 100)
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #vid = cv2.drawContours(red, contours, -1, (0,255,0), 3)

        # Filter out small contours
        x_values = []
        y_values = []
        radii = []
        for cnt in contours:
                perimeter = cv2.arcLength(cnt, True)
                if perimeter > 500:
                        # Get enclosing circles
                        (x,y),radius = cv2.minEnclosingCircle(cnt)
                        center = (int(x), int(y))
                        radius = int(radius)
                        cv2.circle(red, center, radius, (0,255,0), 2)
                        cv2.circle(red, center, 2, (255,0,0), 3)
                        x_values.append(x)
                        y_values.append(y)
                        radii.append(radius)
        
        if len(radii) > 0:
                avg_x = int(sum(x_values) / len(x_values))
                avg_y = int(sum(y_values) / len(y_values))
                avg_r = int(sum(radii) / len(radii))
                cv2.circle(red, (avg_x,avg_y),avg_r, (0,255,255),2) # Mean circle outline
                cv2.circle(red, (avg_x,avg_y),2, (0,0,255),3) # Mean circle center
        
        cv2.imshow('hello', red)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                                break
im.release()
cv2.destroyAllWindows()
