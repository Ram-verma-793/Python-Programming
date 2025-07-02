'''
🔗 Inheritance in Python
🧠 What is Inheritance?
Inheritance allows one class (child/derived class) to reuse the features (variables and methods) of another class (parent/base class).

It helps in code reuse and logical hierarchy.

Syntax =>

class Parent:
    # parent class code

class Child(Parent):
    # child class inherits from Parent

'''



class car:
    def color(self):
        print("The car has a color")

    def brand(self):
        print("The car has a brand name")

class mercedes(car):

    def wheels(self):
        print("The mercedes has it's own wheels!")

# creating the object
myCar = car()
mc = mercedes()

mc.color()
mc.brand()
mc.wheels()