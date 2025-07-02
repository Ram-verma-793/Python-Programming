li = ["Apple", "Mango", "Banana", "Orange", "guava"]
# printing the list
print(li)

#  list methods

# append() => Add item at the end
li.append("pineApple")
print(li)

#  insert(i, val) => insert item at index i
li.insert(3, "Chiku")
print(li)

# remove(val) => removes the first occurrence

li.remove("Chiku")
print(li)

# pop() => removes the last item

li.pop()
print(li)

# sort() => sorts the list alphabetical

li.sort()
print(li)

# reverse() => reverse the list

li.reverse()
print(li)

# len() => returns the length of the list

print(len(li))


# extend() => add two list

li_2 = [1, 2, 3, 4, 5]
li.extend(li_2)
print(li)

# changing the value at the index

li_2[2] = 256
print(li_2)

# change at list items by the indexing range

li_2[1:3] = [512, "lion", "loki"]
print(li_2)
