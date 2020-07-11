class Point:

    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Point constructor")

    def tostring(self):
        return "{x = %d, y=%d}" % (self.x, self.y)


class Circle(Point):

    radius = 0.0

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
        print("Circle constructor")

    def tostring(self):
        return "{x = %d, y=%d, radius=%d}" % (self.x, self.y, self.radius)

    def calcCircum(self):
        PI = 3.14159
        return 2 * PI * self.radius


p = Point(10, 20)
print(p.tostring())

circle = Circle(10, 20, 5)
print(circle.tostring())
print(circle.calcCircum())

