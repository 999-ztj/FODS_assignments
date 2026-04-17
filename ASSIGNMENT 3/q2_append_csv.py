"""
This program takes student details as input from the user and
appends them to the existing file "records.csv".
Fields: student_name, roll_no, program, year, and group.
"""

print("=== Add New Student Record ===")
print()

# Take input from the user
student_name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
program = input("Enter program: ")
year = input("Enter year: ")
group = input("Enter group: ")

# Create the new line in CSV format
new_record = f"{student_name},{roll_no},{program},{year},{group}\n"

# Append the new record to the file
file = open("records.csv", "a")
file.write(new_record)
file.close()

print()
print("Record added successfully!")
print("Added:", new_record.strip())
