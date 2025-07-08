'''
🔹 What is NumPy?
NumPy (Numerical Python) is a Python library used for:

Fast mathematical operations on large data

Creating arrays, matrices, and performing linear algebra, statistics, etc.

Much faster than Python lists (internally written in C)
'''

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 100])
print(arr)
print(type(arr))

average = np.mean(arr)
print("Average: ", average)



