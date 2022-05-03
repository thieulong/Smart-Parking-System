import cv2

camera = cv2.VideoCapture(0)

print("[INFO] Initializing camera.")

cv2.namedWindow("Camera")

while True: 
    
    ret, frame = camera.read()
    
    if not ret:
        
        print("[ERROR] Failed to initialize camera.")
        
        break
    
    cv2.imshow("Camera", frame)
    
    key = cv2.waitKey(1)
       
    if key%256 == 27:
        
        # ESC
        
        print("[INFO] Camera terminated.")
        
        break
    
    elif key%256 == 32:
        
        # SPACE 
        
        img_name = "parking_lot.png"
        
        print("[INFO] Saving '{}' ...".format(img_name))
        
        cv2.imwrite(img_name, frame)
        
        print("[INFO] '{}' saved successfully!".format(img_name))

        camera.release()

        cv2.destroyAllWindows() 
        
        break