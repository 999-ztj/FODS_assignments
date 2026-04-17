'''
This program calculates factorial of a positive integer.
'''

x = input("Enter a number: ")

if not x.isdigit():
    print("Invalid input! Please enter a positive integer.")
else:
    x = int(x)
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    print("Factorial:", fact)