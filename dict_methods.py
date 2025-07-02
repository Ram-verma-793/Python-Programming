my_dict = {
    "name": "parrot",
    "type": "bird",
    "color": "green",
    "age": 1
}
my_dict2 = {
    "name": "lion",
    "type": "animal",
    "color": "brown",
    "age": 3
}

print(my_dict)

# keys() => returns all keys
print(my_dict.keys())

# value() => returns all values
print(my_dict.values())

# items() => returns all key-value pairs
print(my_dict.items())

# get(key) => get value
print(my_dict.get("color"))

# update(dict2) => add/update from another dictionary
my_dict.update(my_dict2)
print(my_dict)