import cv2
import numpy as np

def imstack(scale,imgArr):

    hor=()
    for j in range(0,len(imgArr)):
        app = ()
        for i in range(0,len(imgArr[0])):
            if (len(np.shape(imgArr[j][i]))==2):
                 imgArr[j][i]=cv2.cvtColor(imgArr[j][i],cv2.COLOR_GRAY2BGR)
            imgArr[j][i]=cv2.resize(imgArr[j][i],None,fx=scale,fy=scale)
            app+=(imgArr[j][i],)

        hor+=(np.hstack(app),)

    img=np.vstack(hor)
    return img

cap=cv2.VideoCapture(0)
frameWidth=360
frameHeight=360
while True:
    success,img=cap.read()

    img = cv2.resize(img, (frameWidth, frameWidth))
    imgBlur = cv2.GaussianBlur(img, (9, 9), 0)
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    imgEdge=cv2.Canny(img,200,200)

    arr=[[img,imgGray],[imgEdge,imgBlur]]
    imag=imstack(1,arr)

    cv2.imshow("GrayImg",imag)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


'''
array1=[1,2,3]
array2=[4,5,6]
array3=[array1,array2]
print(np.hstack((array3[0],array3[1])))
'''

'''
arr=[[1,2,3],[4,5,6]]
print(np.shape(arr)[1])
print(len(arr[0]))
'''