import math

a=int(input("Enter A:"))
b=int(input("Enter B:"))
c=int(input("Enter C:"))
r=int(input("Enter R:"))
trapezoid = ((a + b) * c) / 2
circle = math.pi*r**2
cylinder = math.pi * (r ** 2)
cone = (1/3) * math.pi * (r ** 2)
sphere = (4/3) * math.pi * (r ** 3)

print("\n Trapezoid Value:",trapezoid)
print("\n circle",circle)
print("\n Cylinder",cylinder)
print("\n Cone:",cone)
print("\n Sphere:",sphere)
