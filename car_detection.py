import cv2

camera = cv2.VideoCapture(2)

car_cascade = cv2.CascadeClassifier('cars.xml')

while True:
    
    ret,frame = camera.read()

    if ret:
        
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        car = car_cascade.detectMultiScale(gray,1.1,5)
        
        for (x,y,w,h) in car:
            
            cv2.rectangle(img=frame,
                         pt1=(x,y),
                         pt2=(x+w,y+h),
                         color=(0,255,0),
                         thickness=2)

            cv2.putText(img=frame,
                       text="Car",
                       org=(x, y + h + 25), 
                       fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
                       fontScale=1, 
                       color=(0, 255, 0),
                       thickness=2)

    cv2.namedWindow("Car detect")

    cv2.imshow("Car detect", frame)
    
    if cv2.waitKey(1) & 0xFF == 27:

        break

camera.release()

cv2.destroyAllWindows()