import numpy as np

arr1 = np.array([20, 60, 10, 2, 48, 25, 13, 256])
arr2 = np.array([[10, 20, 30, 40, 50], [60, 70, 80, 90, 100]])
print("slicing: ",arr1[::2])

# .shape == know the size/ structure of the array

print(arr1.shape)

#  .ndim == Helps understand dimensions (1d, 2d, 3d)

print(arr1.ndim)

#  .size == Total no. of elements

print(arr1.size)

# .dtype == type of data (int, float)

print(arr1.dtype)

# .reshape() == rearrange data shape (1d => 2d)

# .flatten() == converts multi d array => 1d array
print(arr2.flatten())

# .transpose() == switching rows <==> columns in 2d/ 3d
transpose = arr2.transpose()
print("Transpose: ", transpose)

# maths----------------------

# .sum() == sum 
print( "sum: ",arr1.sum())

# .mean() == mean/ average
print("average", arr1.mean())

# .min() == min of the array
print("min is: ", arr1.min())

# .max() == max of the array
print("max is: ", arr1.max())

# .argmin() == get index of min
print("index of min is: ", arr1.argmin())

# .argmax() == get index of max
print("index of max is: ", arr1.argmax())

# .astype() == when converting data types (float => int)
float_array = arr1.astype(float)
print("before converted: ", arr1)
print("converted to float: ")

# .copy() == avoid unexpected changes when duplicate arrays
arr_copy = arr1.copy()
print("copid array: ", arr_copy)

# .sort() == sorts the array
arr1.sort()
print("sorted", arr1)

# ravel() == this is like the flatten method but it is more memory efficient then that
# converts multi-d array into one-d array

arr_2d = np.array([[1, 2], [3, 4]])
r = arr_2d.ravel()
print("ravel() method", r)