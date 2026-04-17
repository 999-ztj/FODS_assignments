"""
This program is a dice guessing game.
"""

import random

dice = random.randint(1, 6)

guess = int(input("Guess the dice value (1-6): "))

if guess == dice:
    print("😊 Correct!")
elif abs(guess - dice) == 1:
    print("😐 Close!Dice was:", dice)
else:
    print("❌ Wrong! Dice was:", dice)