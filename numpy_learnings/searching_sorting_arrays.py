import numpy as np

# np.sort() == sorts the array
a = np.array([10, 56, 256, 343, 12, 78])
print("Sorted array:", np.sort(a))


# np.argsort() == returns the indices that would sort the array

print("Indices to sort: ", np.argsort(a))

# np.searchsorted() == search where a number would go in a sorted array

sorted_arr = np.array([10, 20, 30, 40, 50])  # in this array the number 25 go between 20-30 so that it's index is 2
print(np.searchsorted(sorted_arr, 25))

# np.where() == finds hte index where the condition is true

arr = np.array([10, 20, 30, 40])

print(np.where(arr > 20))