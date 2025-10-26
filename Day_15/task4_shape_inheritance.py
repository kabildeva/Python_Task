import math

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = (self.a + self.b + self.c)/2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

c = Circle(5)
s = Square(4)
t = Triangle(3, 4, 5)

print("Circle - Area:", c.area(), "Perimeter:", c.perimeter())
print("Square - Area:", s.area(), "Perimeter:", s.perimeter())
print("Triangle - Area:", t.area(), "Perimeter:", t.perimeter())
