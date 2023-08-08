import cv2
import numpy as np
#from ImageStack import imstack
def imStack(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
cap=cv2.VideoCapture(0)

def empty(a):
    pass
cv2.namedWindow("Parameter")
cv2.resizeWindow("Parameter",600,120)
cv2.createTrackbar("Th1","Parameter",150,255,empty)
cv2.createTrackbar("Th2","Parameter",255,255,empty)
cv2.createTrackbar("Area","Parameter",1000,10000,empty)


def getCont(img,imgCont):
    cnt,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    ar = cv2.getTrackbarPos("Area", "Parameter")
    for c in cnt:

        area= cv2.contourArea(c)
        if area>ar:
            cv2.drawContours(imgCont, cnt, -1, (191, 0, 255))
            per=cv2.arcLength(c,True)
            approx=cv2.approxPolyDP(c,0.02*per,True)
            x,y,w,h=cv2.boundingRect(approx)
            cv2.rectangle(imgCont,(x,y),(x+w,y+h),(0,255,0),5)
            cv2.putText(imgCont,"Points :"+str(len(approx)),(x+w+20,y+20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),2)
            cv2.putText(imgCont, "Area :" + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.5,(0, 255, 0), 2)


while True:
    success,img=cap.read()
    img=cv2.resize(img,(480,360))

    imgCont=img.copy()
    imgBlur=cv2.GaussianBlur(img,(7,7),1)
    imgGray=cv2.cvtColor(imgBlur,cv2.COLOR_BGR2GRAY)

    th1=cv2.getTrackbarPos("Th1","Parameter")
    th2=cv2.getTrackbarPos("Th2", "Parameter")

    imgCanny=cv2.Canny(imgGray,th1,th2)
    imgDila=cv2.dilate(imgCanny,np.ones((5,5)),iterations=1)
    getCont(imgDila,imgCont)


    hstack=imStack(0.8,([img,imgGray,imgCanny],[imgDila,imgDila,imgCont]))

    cv2.imshow("image",hstack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break