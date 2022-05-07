import cv2
from parking_availability import parking_availability

camera = cv2.VideoCapture(2)

print("[INFO] Initializing camera.")

cv2.namedWindow("Camera")

file = open("parking_area_coordinates.txt")

print("[INFO] Loading parking coordinates ...")

lines = file.readlines()

lines = [line.strip() for line in lines]

total_parking_lots = len(lines)

parking_lot_coords = list()

for i in range(len(lines)):
    
    coords = lines[i].split()

    left = int(coords[0])

    top = int(coords[1])
    
    right = int(coords[2])
    
    bottom = int(coords[3])

    coords = [left, top, right, bottom]

    parking_lot_coords.append(coords)

while True:

    ret, frame = camera.read()

    frame = cv2.flip(frame, 1)

    if not ret:
        
        print("[ERROR] Failed to initialize camera.")
        
        break

    if ret:

        for i in range(len(parking_lot_coords)):

            parking_lot = frame[parking_lot_coords[i][1]: parking_lot_coords[i][-1],
                                parking_lot_coords[i][0]: parking_lot_coords[i][2]]

            cv2.imwrite("parking_lots/{}.png".format(i),
                        img=parking_lot)

            cv2.rectangle(img=frame,
                          pt1=(parking_lot_coords[i][0], parking_lot_coords[i][1]),
                          pt2=(parking_lot_coords[i][2], parking_lot_coords[i][-1]),
                          color=(0,255,0),
                          thickness=1)

        parking_lots = parking_availability()

        available_parking_lot = parking_lots[0]

        unavailable_parking_lot = parking_lots[1]

        print("Available:", available_parking_lot)
        print("Unavailable:", unavailable_parking_lot)

        if len(unavailable_parking_lot) > 0:

            for i in range(len(unavailable_parking_lot)):

                cv2.rectangle(img=frame,
                              pt1=(unavailable_parking_lot[i][0], unavailable_parking_lot[i][1]),
                              pt2=(unavailable_parking_lot[i][2], unavailable_parking_lot[i][-1]),
                              color=(0,0,255),
                              thickness=1)

        cv2.putText(img=frame,
                    text="Total parking lots: {}".format(total_parking_lots),
                    org=(10,440),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.5,
                    color=(0, 255, 0),
                    thickness=1)

        cv2.putText(img=frame,
                    text="Available parking lots: {}".format(len(available_parking_lot)),
                    org=(10,460),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.5,
                    color=(0, 255, 0),
                    thickness=1)

        
        width = 1800

        height = 1080
        
        dim = (width, height)

        frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

        cv2.imshow("Camera", frame)

        key = cv2.waitKey(1)

        if key%256 == 27:
            
            # ESC
            
            print("[INFO] Camera terminated.")
            
            break
    