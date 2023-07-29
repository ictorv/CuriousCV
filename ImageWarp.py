import cv2
import numpy as np

points=np.zeros((4,2),dtype=int)
count=0
def mousePoints(event,x,y,flags,params):
    global count
    if event==cv2.EVENT_LBUTTONDOWN:
        points[count]=x,y
        count=count+1
        print(points)
        print(count)

img=cv2.imread("Resources/cards.jpg")
width=250
height=350

while True:
    if count==4:
        pts1=np.float32([points[0],points[1],points[2],points[3]])
        pts2 = np.float32([[0,0], [width,0], [0,height], [width,height]])
        mat=cv2.getPerspectiveTransform(pts1,pts2)
        warp=cv2.warpPerspective(img,mat,(width,height))
        cv2.imshow("warped",warp)

    for i in range(0,4):
        cv2.circle(img,(points[i][0],points[i][1]),3,(0,255,0),cv2.FILLED)
    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image",mousePoints)

    key=cv2.waitKey(1)
    if key==ord('q'):
        break