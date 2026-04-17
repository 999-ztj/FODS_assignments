'''
This program finds numbers divisible by 9 but not by 6.
'''

start = int(input("Enter start: "))
end = int(input("Enter end: "))

for x in range(start, end + 1):
    if x % 9 == 0 and x % 6 != 0:
        print(x)