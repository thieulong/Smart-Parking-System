import math

def calculate_distance(a, b):
    
    xa = a[0] + round((a[2]-a[0])/2)
    ya = a[1] + round((a[-1]-a[1])/2)

    xb = b[0] + round((b[2]-b[0])/2)
    yb = b[1] + round((b[-1]-b[1])/2)

    distance = math.sqrt(math.pow((xb-xa),2)+math.pow((yb-ya),2))

    return distance

def find_closest_parking(parking_list, entrance):

    distance_list = list()

    for i in range(len(parking_list)):

        distance = calculate_distance(a=parking_list[i], b=entrance)

        distance_list.append(distance)

    min_distance = min(distance_list)

    min_index = distance_list.index(min_distance)

    closest_parking = parking_list[min_index]

    return closest_parking