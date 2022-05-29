import cv2
from os import path
from parking_availability import parking_availability
import distance_calc

print("-"*50)
print("SMART PARKING SYSTEM".center(50))
print("-"*50)

while True:

    print()

    print("Enter your option:")
    print("1. Capture new parking area")
    print("2. Use saved parking area")

    choice = int(input("Choose: "))

    if choice == 1:

        import capture_parking_lot

        print()

        print("Display captured parking area?")
        print("1. Yes")
        print("2. No")

        choice = int(input("Choose: "))

        if choice == 1: 

            import display_captured_parking_lot

            break

        elif choice == 2:

            print()

            print("[INFO] Skip display parking area.")

        print("[INFO] Please draw parking area.")

        import draw_parking_area

        print("[STATUS] Complete drawing parking area.")

        import label_parking_lot

        print("[STATUS] Complete label parking area.")

        print("[INFO] Please draw parking entrance")

        import draw_parking_entrance

        print("[STATUS] Complete drawing parking entrance.")

        break

    elif choice == 2:

        if path.exists('parking_lot.png'): 

            print()

            print("[INFO] Found saved parking area.")

            print("[INFO] Saved parking area chosen.")

            print()

            print("Display captured parking area?")
            print("1. Yes")
            print("2. No")

            choice = int(input("Choose: "))

            if choice == 1: 

                import display_captured_parking_lot

                break

            elif choice == 2:

                print()

                print("[INFO] Skip display parking area.")

                break

        else:

            print("[ERROR] No parking area found, please capture new parking area.")

camera = cv2.VideoCapture(0)

print("[INFO] Initializing camera.")

cv2.namedWindow("Camera")

file = open("parking_labels.txt")

labels = file.read().splitlines()

file = open("parking_entrance_coordinates.txt")

entrance = file.read().split()

entrance = [int(i) for i in entrance]

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

            box_center_x = parking_lot_coords[i][0] + round((parking_lot_coords[i][2]-parking_lot_coords[i][0])/2) - 5
            box_center_y = parking_lot_coords[i][1] + round((parking_lot_coords[i][-1]-parking_lot_coords[i][1])/2)

            cv2.putText(img=frame,
                        text=labels[i],
                        org=(box_center_x, box_center_y),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.3,
                        color=(0, 255, 0),
                        thickness=1)

        parking_lots = parking_availability()

        available_parking_lot = parking_lots[0]

        unavailable_parking_lot = parking_lots[1]

        # print("Available:", available_parking_lot)
        # print("Unavailable:", unavailable_parking_lot)

        if len(unavailable_parking_lot) > 0:

            for i in range(len(unavailable_parking_lot)):

                cv2.rectangle(img=frame,
                              pt1=(unavailable_parking_lot[i][0], unavailable_parking_lot[i][1]),
                              pt2=(unavailable_parking_lot[i][2], unavailable_parking_lot[i][-1]),
                              color=(0,0,255),
                              thickness=1)

        if len(available_parking_lot) > 0:

            closest_parking = distance_calc.find_closest_parking(parking_list=available_parking_lot, entrance=entrance)

            closest_parking_label = labels[parking_lot_coords.index(closest_parking)]

        cv2.rectangle(img=frame,
                          pt1=(entrance[0], entrance[1]),
                          pt2=(entrance[2], entrance[-1]),
                          color=(0,0,255),
                          thickness=1)

        cv2.putText(img=frame,
                    text="IN",
                    org=(entrance[0]+round((entrance[2]-entrance[0])/2)-5, entrance[1]+round((entrance[-1]-entrance[1])/2)+5),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.5,
                    color=(255, 0, 0),
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

        cv2.putText(img=frame,
                    text="Closest parking lot: {}".format(closest_parking_label),
                    org=(440,460),
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
    