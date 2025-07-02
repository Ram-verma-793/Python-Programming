my_set = {"ram", "shyam", "apple", 3.14, 512, True}
set_02 = {"red", "green", "pink", "blue", "black"}

# add() => add item to the set
my_set.add("Banana")
print(my_set)

# remove() => remove item (error if not found)
my_set.remove("shyam")
print(my_set)

# discard() => remove item (no error)
my_set.discard(512)

# pop() => removes and returns random item
my_set.pop()
print(my_set)

# clear() => removes all the items
my_set.clear()
print(my_set)

# update(set2) => add elements from the ther set
my_set.update(set_02)
print(my_set)