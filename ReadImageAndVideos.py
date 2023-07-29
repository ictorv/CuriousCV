import cv2
 # Image
'''
img=cv2.imread("Resources/img.jpg")
cv2.imshow("MyCar",img)
cv2.waitKey(0)
'''
# Video
frameWidth=360
frameHeight=360

cap=cv2.VideoCapture("Resources/vid.mp4")

# cap.set(3,frameWidth)
# cap.set(4,frameHeight)

while True:
    success,img=cap.read()
    img=cv2.resize(img,(frameWidth,frameWidth))
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

