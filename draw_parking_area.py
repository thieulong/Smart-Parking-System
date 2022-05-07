import cv2

print("[INFO] Loading parking lot image ...")

image = "parking_lot.png"

img = cv2.imread(image)

file = open("parking_area_coordinates.txt","r+")

file.truncate(0)

file.close()

print("[INFO] Parking lot image loaded successfully!")
    
print("[INFO] Click and drag to draw parking area. Press SPACE to save after each area")

ix = -1
iy = -1
drawing = False

a = 0
b = 0
c = 0
d = 0

parking_lot = 0

def draw_reactangle_with_drag(event, x, y, flags, param):
    global ix, iy, drawing, img, a, b, c, d
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img = cv2.imread(image)
            cv2.rectangle(img, 
                          pt1=(ix,iy), 
                          pt2=(x, y),
                          color=(0,255,0),
                          thickness=2)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        img = cv2.imread(image)
        cv2.rectangle(img, 
                      pt1=(ix,iy), 
                      pt2=(x, y),
                      color=(0,255,0),
                      thickness=2)
        
        a = ix
        b = iy
        c = x
        d = y 

cv2.namedWindow("Parking area")

while True:
    
    cv2.imshow("Parking area", img)
    
    cv2.setMouseCallback("Parking area", draw_reactangle_with_drag)
    
    if cv2.waitKey(5) == 32:

        parking_lot += 1
        
        print("[INFO] SPACE pressed! New parking area saved.")

        print("[INFO] Number of parking lots: {}".format(parking_lot))
        
        cv2.imwrite("parking_lot.png", img)
        
        with open('parking_area_coordinates.txt', 'a') as file:
            
            file.write("{} {} {} {}\n". format(a, b, c, d))
        
        continue
    
    if cv2.waitKey(5) == 27:
        
        print("[INFO] Exit drawing parking area.")
        
        break
    
cv2.destroyAllWindows()