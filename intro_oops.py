'''
OOPs in Python (Object-Oriented Programming System)
OOP (Object-Oriented Programming) is a programming paradigm that uses objects and classes to structure code.
Python supports OOP, making it easy to design programs around real-world entities.

🔹 Basic OOP Concepts in Python


Class	A blueprint or template for creating objects
Object	An instance of a class
Constructor	A special method __init__() used to initialize object properties
Self	Refers to the current instance of the class
Inheritance	Allows one class to inherit properties of another class
Encapsulation	Hides internal details and only shows what is necessary
Polymorphism	Ability to use the same method in different ways (e.g., method overriding)
'''


class Student:
    def setName(self, name):
        
        self.name = name
        
    def setAge(self, age):
        self.age = age

    def getName(self):
        return self.name    
    
    def getAge(self):
        return self.age


# creating object
student1 = Student()
student1.setName("Ram")
student1.setAge(20)

names = student1.getName()
age = student1.getAge()
print(names)
print(age)