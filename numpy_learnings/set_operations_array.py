import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# np.unique()  == get all the unique elements
unique_val = np.unique(arr)
print("unique values : ", unique_val)

# np.union1d(arr1, arr2) == union of two arrays (all unique elements)
a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([4, 5, 6, 7, 8, 0])

print("Union: ", np.union1d(a, b))

# np.intersect1d(arr1, arr2) == common elements
a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([4, 5, 6, 7, 8, 0])

print("Intersection: ", np.intersect1d(a, b))

# np.setdiff1d(arr1, arr2) == Elements in arr1 but not in arr2

print("set difference: ", np.setdiff1d(a, b))


# np.setxor1d(arr1, arr2) == Elements in either arr1 or arr2 but not both

print("XOR: ", np.setxor1d(a, b))
