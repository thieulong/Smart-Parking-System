from PIL import Image

img = Image.open(r"parking_lot.png")

file = open("parking_area_cordinates.txt")

print("[INFO] Opened parking cordinates list.")

lines = file.readlines()

lines = [line.strip() for line in lines]

print("[INFO] Reading parking area cordinates ...")

for i in range(len(lines)):
    
    cords = lines[i].split()
    
    left = int(cords[0])
    
    top = int(cords[1])
    
    right = int(cords[2])
    
    bottom = int(cords[3])
    
    crop = img.crop((left, top, right, bottom))
    
    crop.save("parking_areas/{}.png".format(i))
    
    print("[INFO] Saved {}.png in parking_areas/".format(i))