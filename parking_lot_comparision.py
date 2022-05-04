import cv2
import numpy as np

original = cv2.imread("parking_areas/0.png")
realtime = cv2.imread("realtime_parking_areas/0.png")

if original.shape != realtime.shape:
    print("[ERROR] Images have same size and channels")

difference = cv2.subtract(original, realtime)
b, g, r = cv2.split(difference)

if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    print("[INFO] Images are completely equal")

else:
    print("[INFO] Images are different")