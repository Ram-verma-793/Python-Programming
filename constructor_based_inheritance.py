class Animal:
    def __init__(self):
        print("This is an animal class!")

class Lion(Animal):
    def __init__(self):
        super().__init__()
        print("This is a sub class of the Animal class")

# creating the object
animal = Animal()

l = Lion()

