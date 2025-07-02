#  List comprehension is a short and clean way to create a list using a single line of code.

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(li)

new_list = [i for i in li if i%2 == 0]
print(new_list)

# Q: Write a list comprehension to get all numbers from 1 to 20 that are divisible by 3.

result = [i for i in li if i%3 == 0]
print("From 1-20 divisible by 3: ", result)