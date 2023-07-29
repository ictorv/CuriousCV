import numpy as np
import cv2
img=cv2.imread("Resources/img.jpg")

'''
Resize
'''
imgRes=cv2.resize(img,(200,200))
cv2.imshow("Resized",imgRes)

'''
Grayscale
'''
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayImg",imgGray)

'''
Blur
'''
imgBlur=cv2.GaussianBlur(img,(9,9),0)
cv2.imshow("Blur",imgBlur)

'''
Edge Detection
'''
imgEdge=cv2.Canny(img,200,200)
cv2.imshow("Edge Detection",imgEdge)

'''
Dilation
'''
kernel=np.ones((5,5),np.uint8)
imgDial=cv2.dilate(imgEdge,kernel,iterations=1)
cv2.imshow("Dialated",imgDial)

'''
Erosion
'''
imgErode=cv2.erode(imgDial,kernel,iterations=1)
cv2.imshow("Eroded",imgErode)

'''
Crop
'''
print(img.shape)
imgCrop=img[100:,90:1100]
cv2.imshow("Crop",imgCrop)


cv2.imshow("Image",img)
cv2.waitKey(0)
