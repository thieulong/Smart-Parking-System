import cv2

camera = cv2.VideoCapture(2)

print("[INFO] Initializing camera.")

cv2.namedWindow("Camera")

# Parking lot cordinates

file = open("parking_area_cordinates.txt")

print("[INFO] Loading parking cordinates ...")

lines = file.readlines()

lines = [line.strip() for line in lines]

parking_lot_cords = list()

for i in range(len(lines)):
    
    cords = lines[i].split()

    left = int(cords[0])

    top = int(cords[1])
    
    right = int(cords[2])
    
    bottom = int(cords[3])

    cords = [left, top, right, bottom]

    parking_lot_cords.append(cords)

# Car recognition

car_cascade = cv2.CascadeClassifier('cars.xml')

while True:

    ret, frame = camera.read()

    if not ret:
        
        print("[ERROR] Failed to initialize camera.")
        
        break

    if ret:

        for i in range(len(parking_lot_cords)):

            cv2.rectangle(img=frame,
                        pt1=(parking_lot_cords[i][0], parking_lot_cords[i][1]),
                        pt2=(parking_lot_cords[i][2], parking_lot_cords[i][-1]),
                        color=(0,255,0),
                        thickness=2)

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        car = car_cascade.detectMultiScale(gray,1.1,1)
        
        for (x,y,w,h) in car:
            
            # cv2.rectangle(img=frame,
            #             pt1=(x,y),
            #             pt2=(x+w,y+h),
            #             color=(0,255,0),
            #             thickness=2)

            # cv2.putText(img=frame,
            #         text="Car",
            #         org=(x, y + h + 25), 
            #         fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
            #         fontScale=1, 
            #         color=(0, 255, 0),
            #         thickness=2)

            car = [x, y, w, h]

            for i in range(len(parking_lot_cords)):
        
                if car[0] >= parking_lot_cords[i][0] and car[0] + car[2] <= parking_lot_cords[i][2] and car[1] >= parking_lot_cords[i][1] and car[1] + car[3] <= parking_lot_cords[i][3]:
                
                    cv2.rectangle(img=frame,
                            pt1=(parking_lot_cords[i][0], parking_lot_cords[i][1]),
                            pt2=(parking_lot_cords[i][2], parking_lot_cords[i][-1]),
                            color=(0,0,255),
                            thickness=2)


        cv2.imshow("Camera", frame)

        key = cv2.waitKey(1)

        if key%256 == 27:
            
            # ESC
            
            print("[INFO] Camera terminated.")
            
            break
    