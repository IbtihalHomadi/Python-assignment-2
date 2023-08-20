
# Program to Calculatre area and Perimeter of Shapes
import math

class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    

class Circle(Shape):
    def __init__(self, Radius):
        self.radius = Radius

    def calculate_area(self):
        return math.pi * self.radius**2
        
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self,Side):
        self.side = Side

    def calculate_area(self):
        return self.side * self.side

    def calculate_perimeter(self):
        return 4* self.side


class Rectangle:
    def __init__(self,Length,Width):
        self.length = Length
        self.width = Width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2*(self.length + self.width)


class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3



radius =3
circle = Circle(radius)
circle_area = circle.calculate_area()
circle_perimeter = circle.calculate_perimeter()

print("Radius of the circle:",radius)
print("Circle Area: ", circle_area)
print("Circle Perimeter:", circle_perimeter)

#------------------------------------------

side = 4
square = Square(side)
square_area = square.calculate_area()
square_perimeter = square.calculate_perimeter()
print("\Square: Side =", side)
print("Square Area:", square_area)
print("Square Perimeter:", square_perimeter)
#------------------------------------------

length = 5
width = 7
rectangle = Rectangle(length, width)
rectangle_area = rectangle.calculate_area()
rectangle_perimeter = rectangle.calculate_perimeter()
print("\nRectangle: Length =",length," Width =",width)
print("Rectangle Area:", rectangle_area)
print("Rectangle Perimeter:", rectangle_perimeter)

#------------------------------------------

base = 5
height = 4
s1 = 4
s2 = 3
s3 = 5
triangle = Triangle(base,height,s1,s2,s3)
triangle_area = triangle.calculate_area()
triangle_perimeter = triangle.calculate_perimeter()
print("\nTriangle: Base =",base," Height =",height," side1 =",s1," side2 =",s2," side3 =",s3)
print("Triangle Area:", triangle_area)
print("Triangle Perimeter:", triangle_perimeter)
print("\n")
#------------------------------------------


