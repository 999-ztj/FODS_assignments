"""
This program takes a list of at least 12 numbers from the user,
sorts the list, and performs slicing to extract elements at index
ranges 3-6, 6-9, and 4-10.
"""

print("Enter at least 12 numbers separated by spaces:")
user_input = input()

numbers = [int(x) for x in user_input.split()]

if len(numbers) < 12:
    print("Error: Please enter at least 12 numbers.")
else:
    print("\nOriginal list:", numbers)

    numbers.sort()
    print("Sorted list:", numbers)

    print("\nSlice [3:6] (index 3 to 5):", numbers[3:6])
    print("Slice [6:9] (index 6 to 8):", numbers[6:9])
    print("Slice [4:10] (index 4 to 9):", numbers[4:10])