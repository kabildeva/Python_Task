import math
r = float(input("Enter radius r: "))
h = float(input("Enter height h: "))
surface_area = 2 * math.pi * r * h + 2 * math.pi * r * r
volume = math.pi * r * r * h
print("Surface area of cylinder:", surface_area)
print("Volume of cylinder:", volume)
