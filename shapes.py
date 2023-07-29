import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
cv2.imshow("Image",img)

'''
Color
'''
img[:]=(122,122,0)
cv2.imshow("OxfordBlue",img)

'''
Line
'''
cv2.line(img,(0,0),(512,512),(0,0,0),3)
cv2.imshow("Line",img)

'''
Rectangle
'''
cv2.rectangle(img,(200,200),(300,300),(0,0,255),2)
cv2.imshow("Rectangle",img)

'''
Circle
'''
cv2.circle(img,(250,250),25,(255,0,0),cv2.FILLED)
cv2.imshow("Circle",img)

'''
Text
'''
cv2.putText(img,"Hello",(200,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
cv2.imshow("Text",img)

cv2.waitKey(0)