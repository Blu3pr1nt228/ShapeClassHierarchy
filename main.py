from shapes import Circle, Rectangle, Triangle

def main():
    shapes = [
        Circle("Red", 5),
        Rectangle("Green", 4, 6),
        Triangle("Blue", 3, 4, 5)
    ]

    for shape in shapes:
        print(f"Shape Color: {shape.get_color()}")
        print(f"Area: {shape.calculate_area()}")
        print(f"Perimeter: {shape.calculate_perimeter()}")
        print("---")

if __name__ == "__main__":
    main()
