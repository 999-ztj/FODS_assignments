"""
This program checks whether a number is positive/negative and even/odd.
"""

x = int(input("Enter a number: "))

if x > 0:
    if x % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
elif x < 0:
    if x % 2 == 0:
        print("Negative and  Even")
    else:
        print("Negative and Odd")
else:
    print("Zero")



