'''
This program is a number guessing game.
'''

import random

number = random.randint(1, 50)

for i in range(7):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Correct!")
        break
    elif guess > number:
        print("Too high")
    else:
        print("Too low")
else:
    print("Better luck next time!")