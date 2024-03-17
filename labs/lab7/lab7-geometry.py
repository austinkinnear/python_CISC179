# Using this for the circle area, rather than 3.14.... cause we can
import math

# exception class for errors
class GeometryError(BaseException):
    pass 

# Base shape class
class Shape:
    def __init__(self):
        raise NotImplementedError("Cannot instantiate an abstract class.")

    def area(self):
        raise NotImplementedError("This method should be overridden in derived classes.")

# Rectangle class for rectangles
class Rectangle(Shape):
    def __init__(self, length, width):
        assert length > 0 and width > 0, "Length and width need to be positive."
        self.length = length  # Store length
        self.width = width    # Store width

    def area(self):
        # Calculate the area of the rectangle
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side_length):
        # Call the Rectangle init because a square is equal lengths and widths
        super().__init__(side_length, side_length)

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        assert radius > 0, "Radius must be a positive number."
        self.radius = radius  # Stores the radius

    def area(self):
        # Area of the circle
        return math.pi * self.radius ** 2

# Try block implemented 
try:
    # Random objects implemented for testing
    rectangle = Rectangle(10, 5)
    square = Square(4)
    circle = Circle(3)

    # Printing areas 
    print(f"Rectangle area: {rectangle.area()}")
    print(f"Square area: {square.area()}")
    print(f"Circle area: {circle.area()}")

    # Assert statements checking accuracy
    assert rectangle.area() == 50, "Rectangle area calculation error."
    assert square.area() == 16, "Square area calculation error."
    assert round(circle.area(), 2) == 28.27, "Circle area calculation error."

except AssertionError as e:
    # Assertion errors
    print(f"Assertion error: {e}")
except GeometryError as e:
    # Geometry errors
    print(f"Geometry error: {e}")
except Exception as e:
    # Unexpected erros
    print(f"Unexpected error: {e}")
