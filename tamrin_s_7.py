from abc import ABC, abstractmethod
import math
#/////////////////////////////////////////////////////
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass  
    @abstractmethod
    def calculate_perimeter(self):
        pass
#/////////////////////////////////////////////////////////
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
#///////////////////////////////////////////////////////
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return 3.14159 * self.radius * self.radius
    def calculate_perimeter(self):
        return 2 * 3.14159 * self.radius
#////////////////////////////////////////////////
shapes = [ Rectangle(4, 5), Circle(3) ]
#/////////////////////////////////////////////////
for shape in shapes:
    print("Area:", shape.calculate_area())
    print("Perimeter:", shape.calculate_perimeter())
    print("-------------")