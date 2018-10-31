import numpy as np
import cv2

cap = cv2.VideoCapture(0)

#motion
fgbg = cv2.createBackgroundSubtractorMOG2()

#face
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    # Background removal
    fgmask = fgbg.apply(frame)

    #finding faces
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor= 1.1,
        minNeighbors = 5
        )

    #square
    for (x,y,w,h) in faces:
        cv2.rectangle(gray,(x,y),(x+w,y+h), (0,255,0), 2)
    
    # Display the resulting frame
    cv2.imshow('frame',fgmask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
