"""
This program counts frequency of numbers in a list.
"""

def count_frequency(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

# testing with 3 lists
print(count_frequency([1,2,2,3]))
print(count_frequency([4,4,4,5]))
print(count_frequency([7,8,7,9]))