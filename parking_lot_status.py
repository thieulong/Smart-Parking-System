import cv2

car_cascade = cv2.CascadeClassifier('cars.xml')

def parking_lot_status(filename):

    parking_lot = cv2.imread(filename)

    gray = cv2.cvtColor(parking_lot, cv2.COLOR_BGR2GRAY)

    detected_cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    if len(detected_cars) == 0:
    
        return "available"

    elif len(detected_cars) > 0:

        return "unavailable"
