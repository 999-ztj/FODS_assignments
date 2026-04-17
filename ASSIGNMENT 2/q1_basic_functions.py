"""
This program uses a function to calculate sum, difference, product, and quotient.
"""

def calculate(x, y):
    print("Sum:", x + y)
    print("Difference:", x - y)
    print("Product:", x * y)
    print("Quotient:", x / y)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

calculate(x, y)