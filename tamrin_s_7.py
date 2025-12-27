from abc import ABC, abstractmethod
import math

# /////////////////////////////////////////////////////
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


# ///////////////////////////////////////////////////////////
class Rectangle(Shape):
    def __init__(self, rectangle_width, rectangle_height):
        self.rectangle_width = rectangle_width
        self.rectangle_height = rectangle_height

    def calculate_area(self):
        return self.rectangle_width * self.rectangle_height

    def calculate_perimeter(self):
        return 2 * (self.rectangle_width + self.rectangle_height)


# /////////////////////////////////////////////////////////
class Circle(Shape):
    def __init__(self, circle_radius):
        self.circle_radius = circle_radius

    def calculate_area(self):
        return math.pi * self.circle_radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.circle_radius


# //////////////////////////////////////////////////
shapes_list = [Rectangle(4, 5), Circle(3)]

# ///////////////////////////////////////////////////
for shape in shapes_list:
    print("Area:", shape.calculate_area())
    print("Perimeter:", shape.calculate_perimeter())
    print("-------------")
