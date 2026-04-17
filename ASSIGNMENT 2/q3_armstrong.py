"""
This program checks whether a number is an Armstrong number.
"""

def is_armstrong(num):
    total = 0
    n = len(str(num))
    temp = num

    while temp > 0:
        digit = temp % 10
        total += digit ** n
        temp //= 10

    return total == num

num = int(input("Enter a number: "))

if is_armstrong(num):
    print("Armstrong number")
else:
    print("Not an Armstrong number")