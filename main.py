import cv2

camera = cv2.VideoCapture(2)

print("[INFO] Initializing camera.")

cv2.namedWindow("Camera")

file = open("parking_area_cordinates.txt")

print("[INFO] Loading parking cordinates ...")

lines = file.readlines()

lines = [line.strip() for line in lines]

while True:

    ret, frame = camera.read()

    if not ret:
        
        print("[ERROR] Failed to initialize camera.")
        
        break

    for i in range(len(lines)):

        cords = lines[i].split()

        left = int(cords[0])
    
        top = int(cords[1])
        
        right = int(cords[2])
        
        bottom = int(cords[3])

        cv2.rectangle(img=frame,
                      pt1=(left, top),
                      pt2=(right, bottom),
                      color=(0,255,0),
                      thickness=2)

        crop = frame[top:bottom, left:right]
    
        # cv2.imwrite("realtime_parking_areas/{}.png".format(i), crop)

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)

    if key%256 == 27:
        
        # ESC
        
        print("[INFO] Camera terminated.")
        
        break
    