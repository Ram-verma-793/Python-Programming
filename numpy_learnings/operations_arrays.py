import numpy as np

arr = np.array([10, 20, 30, 40, 50])

#  1. Boolean Indexing & Filtering
#     Select elements that match a condition.
print(arr[arr>10])  # filters the elements that greater than 10
print(arr[arr==20]) # equal to 20

# 2. Arithmetic Operations on Arrays
#    Add, subtract, multiply arrays directly (element-wise).


a = np.array([10, 2, 3])
b = np.array([4, 5, 6])

print("sum: ", a + b)


# 3. Broadcasting
#    Perform operations between arrays of different shapes

a = np.array([1, 2, 3])
b = np.array(4)
print("sum on different shape arrays: ", a + b)

# 4. Indexing with where()
#    Find positions of elements that meet a condition.

arr = np.array([10, 20, 30, 40, 50])
print(np.where(arr == 10))


# 5. Random Module in NumPy
#    np.random.rand(), np.random.randint() for generating random data (useful for ML & testing).

print("random floating number: ", np.random.rand())  # the rand() generates floating number between 0 and 1

print("random integer number: ", np.random.randint(1, 6))