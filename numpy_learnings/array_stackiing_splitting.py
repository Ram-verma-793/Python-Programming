'''

✅ 3. Array Stacking and Splitting

These operations are super useful when you're combining or breaking down arrays, especially in data preprocessing.
'''

import numpy as np

# np.concatenate() == joins arrays 
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[5, 6, 7]])

result = np.concatenate((a, b), axis=0)
print("Concatenate: \n", result)

# np.vstack() == stack arrays vertically(row wise)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Vertical stack: \n", np.vstack((a, b)))
