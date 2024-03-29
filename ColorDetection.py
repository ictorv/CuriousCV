import numpy as np
import cv2

cap=cv2.VideoCapture(0)

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,220)
cv2.createTrackbar("HUE Min","HSV",0,179,empty)
cv2.createTrackbar("HUE Max","HSV",179,179,empty)
cv2.createTrackbar("SAT Min","HSV",0,255,empty)
cv2.createTrackbar("SAT Max","HSV",255,255,empty)
cv2.createTrackbar("VALUE Min","HSV",0,255,empty)
cv2.createTrackbar("VALUE MAX","HSV",255,255,empty)
while True:
    _,img=cap.read()
    img = cv2.resize(img, (480, 360))
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min=cv2.getTrackbarPos("HUE Min", "HSV")
    h_max=cv2.getTrackbarPos("HUE Max", "HSV")
    s_min=cv2.getTrackbarPos("SAT Min", "HSV")
    s_max=cv2.getTrackbarPos("SAT Max", "HSV")
    v_min=cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max=cv2.getTrackbarPos("VALUE MAX", "HSV")

    lower=np.array([h_min,s_min,v_min])
    upper = np.array([h_max, s_max, v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    res=cv2.bitwise_and(img,img,mask=mask)

    mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)

    #cv2.imshow("Capture",img)
    #cv2.imshow("HSVCapture", imgHSV)
    #cv2.imshow("MaskCapture", mask)
    #cv2.imshow("ResCapture", res)

    hStack=np.hstack([img,mask,res])
    cv2.imshow("Capture", hStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break