import cv2 as cv
import urllib.request
import numpy as np

url='http://192.168.3.62/1280x1024.mjpeg'
cv.namedWindow("Live_Cam_Testing",cv.WINDOW_AUTOSIZE)
cap=cv.VideoCapture(url)

if not cap.isOpened():  
    print("Failed to open WebCam")
    exit()
while True:
    img_resp=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(img_resp.read()),dqtype=np.uint8)
    im=cv.imdecode(imgnp,-1)
    cv.imshow('Live Cam Testing',im)
    key=cv.waitKey(5)
    if key==ord('q'):
        break
cap.release()
cv.destroyAllWindows()