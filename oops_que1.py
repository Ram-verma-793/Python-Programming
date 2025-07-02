'''
Write a Python class named Rectangle to represent a rectangle shape.
The class should have the following functionalities:

A method named set_dimensions that takes two parameters width and
height and sets the attributes of the rectangle object accordingly.
A method named area that calculates and returns the area of the
rectangle
A method named perimeter that calculates and returns the perimeter of
the rectangle
Use this to create objects of the class and print the width, height, area and
'''

class Rectangle:
    def set_dimensions(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)
    
# creating the object

rect = Rectangle()
rect.set_dimensions(10,20)

print("Area: ", rect.area())
print("Perimeter: ",rect.perimeter())

