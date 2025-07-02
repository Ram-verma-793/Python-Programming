# count() => returns the number of times a value appears in a tuple

my_tuple = ("Apple", "Mango", 3.14, 256, True, "Apple", 1, 3, 1, 5, 256, True)
print(my_tuple.count("Apple"))

# index() => returns the index of the first occurrence of a value but if the value is not exist this throw typeerror

print(my_tuple.index(3.14))

# Accessing the tuple

print(my_tuple[4])
for i in my_tuple: 
    print(i)

# print the range
print(my_tuple[0:5])

