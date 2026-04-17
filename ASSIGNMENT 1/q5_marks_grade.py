"""
This program inputs marks for 6 subjects, then calculates the total,
average, percentage, and grade based on the given rules.
"""

print("Enter marks for 6 subjects (out of 100):")

marks = []
for i in range(1, 7):
    mark = float(input(f"  Subject {i}: "))
    marks.append(mark)

total = sum(marks)
average = total / 6
percentage = (total / 600) * 100

if percentage >= 85:
    grade = "Distinction"
elif percentage >= 70:
    grade = "First Division"
elif percentage >= 55:
    grade = "Second Division"
elif percentage >= 45:
    grade = "Third Division"
else:
    grade = "Fail"

print()
print("===== Result =====")
print(f"Marks         : {marks}")
print(f"Total         : {total} / 600")
print(f"Average       : {average:.2f}")
print(f"Percentage    : {percentage:.2f}%")
print(f"Grade         : {grade}")