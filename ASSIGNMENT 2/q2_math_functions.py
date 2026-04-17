"""
This program performs mathematical operations using separate functions.
"""

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def floor_div(x, y):
    return x // y

def power(x, y):
    return x ** y

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Addition:", add(x, y))
print("Multiplication:", multiply(x, y))
print("Division:", divide(x, y))
print("Floor Division:", floor_div(x, y))
print("Exponentiation:", power(x, y))