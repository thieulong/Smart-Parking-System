import cv2 as cv
import numpy as np

camera = cv.VideoCapture(2)
car_cascade = cv.CascadeClassifier('cars.xml')

while True:
    
    ret,frame = camera.read()

    if ret:
        
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        car = car_cascade.detectMultiScale(gray,1.1,5)
        
        for (x,y,w,h) in car:
            
            cv.rectangle(img=frame,
                         pt1=(x,y),
                         pt2=(x+w,y+h),
                         color=(0,255,0),
                         thickness=2)

            cv.putText(img=frame,
                       text="Car",
                       org=(x, y + h + 25), 
                       fontFace=cv.FONT_HERSHEY_SIMPLEX, 
                       fontScale=1, 
                       color=(0, 255, 0),
                       thickness=2)

    cv.namedWindow("Car detect")
    cv.imshow("Car detect", frame)
    
    if cv.waitKey(1) & 0xFF == 27:
        break

camera.release()
cv.destroyAllWindows()