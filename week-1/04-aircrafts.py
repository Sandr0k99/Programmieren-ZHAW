import math

xcord1 = int(input("Coordinate X Plane 1: "))
ycord1 = int(input("Coordinate Y Plane 1: "))
xcord2 = int(input("Coordinate X Plane 2: "))
ycord2 = int(input("Coordinate y Plane 2: "))

distance = math.sqrt((xcord2 - xcord1) ** 2 + (ycord2 - ycord1) ** 2)

print(f"The distance is {distance}")