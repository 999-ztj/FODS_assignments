"""
Matrix operations using NumPy with dimension validation.
Performs addition, subtraction, and multiplication.
Raises exceptions if dimensions are incompatible.
"""

import numpy as np

print("=== Matrix Operations ===\n")

try:
    # Input Matrix 1
    rows1 = int(input("Enter rows for Matrix 1: "))
    cols1 = int(input("Enter columns for Matrix 1: "))

    print(f"Enter {rows1 * cols1} elements for Matrix 1:")
    matrix1 = np.array(list(map(int, input().split()))).reshape(rows1, cols1)

    print()

    # Input Matrix 2
    rows2 = int(input("Enter rows for Matrix 2: "))
    cols2 = int(input("Enter columns for Matrix 2: "))

    print(f"Enter {rows2 * cols2} elements for Matrix 2:")
    matrix2 = np.array(list(map(int, input().split()))).reshape(rows2, cols2)

    print("\nMatrix 1:\n", matrix1)
    print("\nMatrix 2:\n", matrix2)

    # Addition & Subtraction
    if matrix1.shape != matrix2.shape:
        raise ValueError("Addition/Subtraction not possible: matrices must have same dimensions.")

    print("\nAddition Result:\n", matrix1 + matrix2)
    print("\nSubtraction Result:\n", matrix1 - matrix2)

except ValueError as e:
    print("\nError:", e)

# Multiplication (separate so it still runs)
if cols1 == rows2:
    print("\nMultiplication Result:\n", np.dot(matrix1, matrix2))
else:
    print("\nError: Multiplication not possible due to invalid dimensions.")