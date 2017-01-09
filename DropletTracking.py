import numpy as np
import cv2

cap = cv2.VideoCapture("C:\\Users\\prana\\Desktop\\droplet.mov")
fourcc = cv2.VideoWriter_fourcc(*'DVIX')
#frameVid = cv2.VideoWriter('frame.avi',-1, 20.0, (640,480))
#maskVid = cv2.VideoWriter('mask.avi',-1, 20.0, (640,480))
#resVid = cv2.VideoWriter('res.avi',-1, 20.0, (640,480))
#cap = cv2.VideoCapture(0) 
while(cap.isOpened()):
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([38,50,50])
    upper_blue = np.array([130,255,255])
    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    if ret == True:
        #frameVid.write(frame)
        #maskVid.write(mask)
        #resVid.write(res)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
cv2.destroyAllWindows()
cap.release()
#frameVid.release()
#maskVid.release()
#resVid.release()
