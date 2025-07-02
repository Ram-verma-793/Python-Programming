''' 
🧩 What Are Access Modifiers?
Access modifiers are used to control the visibility or access level of class members (variables or methods) from outside the class.

Python has three access levels:

Modifier	Syntax	Access Level
Public	var	Accessible everywhere
Protected	_var	Accessible inside class & subclass
Private	__var	Accessible only inside the class

'''

class modifiers:
    def public_function(self):
        self.name = "ram"
        print(self.name)
    def __private_function(self):  # we can make a function or attribute private private using __(double underscores) before the function name
        self.age = 10
        print(self.age)

    def _protected_function(self):  # we can make a function or attribute private private using _(single underscore) before the function name
        print("this is protected")

mod = modifiers()
mod.public_function()
#  mod.__private_function()   we can't access private function like this
mod._modifiers__private_function()
mod._protected_function()
    