"""The ternary operator in Python is a one-line shorthand for if-else statements.
It's used to write simple conditional expressions in a compact way."""


age = int(input("Enter age: "))
result = "major" if age>18 else "minor"
print(result)

# wap to check if the given number is even or odd using ternary operator.

num = int(input("Enter a number: "))
res = "even" if num%2 == 0 else "odd"
print(res)