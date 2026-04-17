"""
This program generates a NumPy array and performs basic operations:
finding the sum, mean, largest and smallest values.
"""

import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("Array:", numbers)
print()

total_sum = np.sum(numbers)
print("Sum of all elements:", total_sum)

mean_value = np.mean(numbers)
print("Mean value:", mean_value)

largest = np.max(numbers)
smallest = np.min(numbers)
print("Largest value:", largest)
print("Smallest value:", smallest)
