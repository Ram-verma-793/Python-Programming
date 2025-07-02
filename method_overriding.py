'''
🔁 What is Method Overriding?
Method Overriding means:

A child class provides a specific implementation of a method that is already defined in its parent class.

✅ Why override?
To change or extend the behavior of the parent method in the child.

Common in cases like different behaviors for different types (e.g., Animal → Dog, Shape → Circle).
'''

class Fruit:
    def taste(self):
        print("The fruits have a taste.")

class Mango(Fruit):
    def taste(self):
        super().taste() # this is method overriding
        print("The mangos have it's own taste.!")

mango = Mango()
mango.taste()