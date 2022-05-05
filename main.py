from zoneinfo import available_timezones
import cv2

camera = cv2.VideoCapture(2)

print("[INFO] Initializing camera.")

cv2.namedWindow("Camera")

# Parking lot cordinates

file = open("parking_area_cordinates.txt")

print("[INFO] Loading parking cordinates ...")

lines = file.readlines()

lines = [line.strip() for line in lines]

total_parking_lots = len(lines)

available_parking_lot = total_parking_lots

parking_lot_cords = list()

available_parking_lot_cords = list()

occupied_parking_lot_cords = list()

for i in range(len(lines)):
    
    cords = lines[i].split()

    left = int(cords[0])

    top = int(cords[1])
    
    right = int(cords[2])
    
    bottom = int(cords[3])

    cords = [left, top, right, bottom]

    parking_lot_cords.append(cords)

    available_parking_lot_cords.append(cords)

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
            
            cv2.rectangle(img=frame,
                        pt1=(x,y),
                        pt2=(x+w,y+h),
                        color=(0,255,0),
                        thickness=2)

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

                    if parking_lot_cords[i] in available_parking_lot_cords:

                        occupied_parking_lot_cords.append(parking_lot_cords[i])

                        available_parking_lot_cords.remove(parking_lot_cords[i])

                # else:

                #     if parking_lot_cords[i] in occupied_parking_lot_cords:

                #         available_parking_lot_cords.append(parking_lot_cords[i])

                #         occupied_parking_lot_cords.remove(parking_lot_cords[i])

            if len(occupied_parking_lot_cords) > 0:

                for i in range(len(occupied_parking_lot_cords)):

                    if car[0] >= occupied_parking_lot_cords[i][0] and car[0] + car[2] <= occupied_parking_lot_cords[i][2] and car[1] >= occupied_parking_lot_cords[i][1] and car[1] + car[3] <= occupied_parking_lot_cords[i][3]:

                        continue

                    else:

                        available_parking_lot_cords.append(occupied_parking_lot_cords[i])

                        occupied_parking_lot_cords.remove(occupied_parking_lot_cords[i])

                        # It got removed so the for loop cannot continue due to missing element

            available_parking_lot = len(available_parking_lot_cords)


        cv2.putText(img=frame,
                    text="Total parking lots: {}".format(total_parking_lots),
                    org=(10,20),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.8,
                    color=(0, 255, 0),
                    thickness=2)

        cv2.putText(img=frame,
                    text="Available parking lots: {}".format(available_parking_lot),
                    org=(10,50),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.8,
                    color=(0, 255, 0),
                    thickness=2)

        cv2.imshow("Camera", frame)

        key = cv2.waitKey(1)

        if key%256 == 27:
            
            # ESC
            
            print("[INFO] Camera terminated.")
            
            break
    