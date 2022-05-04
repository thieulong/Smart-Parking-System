file = open("parking_area_cordinates.txt")

lines = file.readlines()

lines = [line.strip() for line in lines]

parking_lot_cords = list()

for i in range(len(lines)):
    
    cords = lines[i].split()

    left = int(cords[0])

    top = int(cords[1])
    
    right = int(cords[2])
    
    bottom = int(cords[3])

    cords = [left, top, right, bottom]

    parking_lot_cords.append(cords)


car = [195, 69, 46, 46]

for i in range(len(parking_lot_cords)):

    if car[0] >= parking_lot_cords[i][0] and car[0] + car[2] <= parking_lot_cords[i][2] and car[1] >= parking_lot_cords[i][1] and car[1] + car[3] <= parking_lot_cords[i][3]:

        print(parking_lot_cords[i])