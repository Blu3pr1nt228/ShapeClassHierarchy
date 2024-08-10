# Shape Class Hierarchy

## Overview

This project demonstrates a class hierarchy for representing different shapes using Object-Oriented Programming (OOP) principles, specifically inheritance and polymorphism.

## Classes

### Shape (Base Class)
- **Attributes:**
  - `color` (str): The color of the shape
- **Methods:**
  - `__init__(color: str)`: Initializes the shape with the given color.
  - `calculate_area() -> float`: Abstract method to calculate the area of the shape.
  - `calculate_perimeter() -> float`: Abstract method to calculate the perimeter of the shape.
  - `get_color() -> str`: Retrieves the color of the shape.
  - `set_color(color: str)`: Sets the color of the shape.

### Circle (Derived Class)
- **Attributes:**
  - `radius` (float): The radius of the circle.
- **Methods:**
  - `__init__(color: str, radius: float)`: Initializes the circle with the given color and radius.
  - `calculate_area() -> float`: Calculates the area of the circle (πr²).
  - `calculate_perimeter() -> float`: Calculates the perimeter (circumference) of the circle (2πr).

### Rectangle (Derived Class)
- **Attributes:**
  - `length` (float): The length of the rectangle.
  - `width` (float): The width of the rectangle.
- **Methods:**
  - `__init__(color: str, length: float, width: float)`: Initializes the rectangle with the given color, length, and width.
  - `calculate_area() -> float`: Calculates the area of the rectangle (length * width).
  - `calculate_perimeter() -> float`: Calculates the perimeter of the rectangle (2 * (length + width)).

### Triangle (Derived Class)
- **Attributes:**
  - `side1` (float): The length of the first side of the triangle.
  - `side2` (float): The length of the second side of the triangle.
  - `side3` (float): The length of the third side of the triangle.
- **Methods:**
  - `__init__(color: str, side1: float, side2: float, side3: float)`: Initializes the triangle with the given color and side lengths.
  - `calculate_area() -> float`: Calculates the area of the triangle using Heron's formula.
  - `calculate_perimeter() -> float`: Calculates the perimeter of the triangle (side1 + side2 + side3).

## Running the Program

1. Ensure you have Python installed.
2. Save the source code files (`shape.py`, `shapes.py`, `main.py`) and the documentation file (`README.md`) in the same directory.
3. Run the main program using the command:

   ```bash
   python main.py
