import glob
from parking_lot_status import parking_lot_status

parking_lot_image = sorted(glob.glob("parking_lots/*.png"))

print(parking_lot_image)

file = open("parking_area_coordinates.txt")

lines = file.readlines()

lines = [line.strip() for line in lines]

parking_lot_coords = list()

for i in range(len(lines)):
    
    coords = lines[i].split()

    left = int(coords[0])

    top = int(coords[1])
    
    right = int(coords[2])
    
    bottom = int(coords[3])

    coords = [left, top, right, bottom]

    parking_lot_coords.append(coords)

def parking_availability():

    available_parking_lots = list()

    unavailable_parking_lots = list()

    for i in range(len(parking_lot_image)):
        
        if parking_lot_status(filename=parking_lot_image[i]) == "available":

            available_parking_lots.append(parking_lot_coords[i])

        if parking_lot_status(filename=parking_lot_image[i]) == "unavailable":

            unavailable_parking_lots.append(parking_lot_coords[i])

    return available_parking_lots, unavailable_parking_lots
