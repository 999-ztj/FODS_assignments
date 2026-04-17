"""
This program sorts student names in reverse alphabetical order.
"""

def sort_names(names):
    return sorted(names, reverse=True)

names = input("Enter names separated by comma: ").split(",")

print("Sorted names:", *sort_names(names))