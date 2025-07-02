'''
💥 What is an Exception?
An exception is an error that occurs at runtime, causing your program to crash if not handled.

For example:

print(10 / 0)   # ❌ ZeroDivisionError

'''

# zero division error

# try:
#     x = 10/0
# except ZeroDivisionError:
#     print("you cannot divide by zero") 
#     print("It's working!")   

# we can handle multiple errors at the same time

# try:
#     x = int(input("Enter a number: "))
#     print(10/x)
# except ZeroDivisionError:
#     print("Cannot divide by zero!!")
# except ValueError:
#     print("This is not a valid number!")
#     print("Hey look that's all working now")



# using the else and finally block

try:
    f = open("file.txt", 'r')
    content = f.read()
except FileNotFoundError as e:
    print("File not found",e)    # e catch the reason of the error
else:
    print("File read successfully!")
    print(content)
finally:
    print("The finally block always runs..")