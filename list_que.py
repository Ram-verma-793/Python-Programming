"""Given a list in Python and provided the index of the elements,
write a program to swap the two elements in the list."""

li = [23, 65, 19, 90]
idx1 = 0
idx2 = 2

print("Before swap",li)
temp = li[idx1]
li[idx1] = li[idx2]
li[idx2] = temp
print("After swap",li)