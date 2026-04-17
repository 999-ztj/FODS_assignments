'''
This program sums positive and negative numbers separately.
'''

pos_sum = 0
neg_sum = 0

while True:
    x = int(input("Enter number: "))

    if x >= 0:
        pos_sum += x
    else:
        neg_sum += x

    choice = input("Continue? (y/n): ")
    if choice.lower() == 'n':
        break

print("Positive sum:", pos_sum)
print("Negative sum:", neg_sum)