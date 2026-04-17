"""
This program removes duplicates and sorts numbers.
"""

nums = list(map(int, input("Enter numbers separated by space: ").split()))

new_list = sorted(set(nums))

print("Result:", new_list)