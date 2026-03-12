import math
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,length):
        self.width = width
        self.length = length
    def area(self):
        return self.width*self.length
class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self):
        return self.length*self.length
class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        return self.base*self.height*0.5
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi*self.radius**2
shapes = (Rectangle(4,5),Square(5),Triangle(6,3),Circle(2))
for shape in shapes:
    print(shape.area())