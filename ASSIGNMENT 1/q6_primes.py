'''
This program finds prime numbers in a given range.
'''

start = int(input("Enter start: "))
end = int(input("Enter end: "))

count = 0
total = 0

for x in range(start, end + 1):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            print(x)
            count += 1
            total += x

print("Count:", count)
print("Sum:", total)