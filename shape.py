from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color: str):
        self._color = color

    @abstractmethod
    def calculate_area(self) -> float:
        """Calculate the area of the shape."""
        raise NotImplementedError

    @abstractmethod
    def calculate_perimeter(self) -> float:
        """Calculate the perimeter of the shape."""
        raise NotImplementedError

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self._color

    def set_color(self, color: str):
        """Set the color of the shape."""
        self._color = color
