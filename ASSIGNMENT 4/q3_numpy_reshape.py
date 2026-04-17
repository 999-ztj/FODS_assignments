"""
This program creates an array of 12 random integers using NumPy,
sorts the array, and reshapes it into a 3x4 matrix.
"""

import numpy as np

# Create an array of 12 random integers between 1 and 100
random_array = np.random.randint(1, 100, size=12)
print("Original random array:", random_array)

# Sort the array
sorted_array = np.sort(random_array)
print("Sorted array:", sorted_array)

print()

# Reshape into a 3x4 matrix
matrix = sorted_array.reshape(3, 4)
print("Reshaped into 3x4 matrix:")
print(matrix)

print()

# Also show 4x3 reshape
matrix2 = sorted_array.reshape(4, 3)
print("Reshaped into 4x3 matrix:")
print(matrix2)
