'''
🔁 What is Operator Overloading?
Operator overloading lets you customize the behavior of operators (+, -, >, ==, etc.) for your own classes.

📌 In simple words:
You can tell Python what + should do when used with your objects (like Car + Car).

'''

class operator_overloading:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __mul__(self,other):
        return self.value * other.value
    
    def __sub__(self, other):
        return self.value - other.value

    def __truediv__(self, other):
        return self.value / other.value
    
op1 = operator_overloading(int(input("value 1: ")))
op2 = operator_overloading(int(input("value 2: ")))

print("sum: ", op1 + op2)
print("multiply: ", op1 * op2)
print("subtract: ", op1 - op2)
print("divide: ", op1 / op2)
