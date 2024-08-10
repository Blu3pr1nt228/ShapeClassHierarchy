import math
from shape import Shape

class Circle(Shape):
    def __init__(self, color: str, radius: float):
        super().__init__(color)
        self._radius = radius

    def calculate_area(self) -> float:
        """Calculate the area of the circle."""
        return math.pi * self._radius ** 2

    def calculate_perimeter(self) -> float:
        """Calculate the perimeter (circumference) of the circle."""
        return 2 * math.pi * self._radius

class Rectangle(Shape):
    def __init__(self, color: str, length: float, width: float):
        super().__init__(color)
        self._length = length
        self._width = width

    def calculate_area(self) -> float:
        """Calculate the area of the rectangle."""
        return self._length * self._width

    def calculate_perimeter(self) -> float:
        """Calculate the perimeter of the rectangle."""
        return 2 * (self._length + self._width)

class Triangle(Shape):
    def __init__(self, color: str, side1: float, side2: float, side3: float):
        super().__init__(color)
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

    def calculate_area(self) -> float:
        """Calculate the area of the triangle using Heron's formula."""
        s = (self._side1 + self._side2 + self._side3) / 2
        area = math.sqrt(s * (s - self._side1) * (s - self._side2) * (s - self._side3))
        return area

    def calculate_perimeter(self) -> float:
        """Calculate the perimeter of the triangle."""
        return self._side1 + self._side2 + self._side3
