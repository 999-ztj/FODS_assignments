"""
This program reads the file "records.csv" and displays its contents.
The fields are: student_name, roll_no, program, year, and group.
"""

# Open and read the CSV file
file = open("records.csv", "r")

# Read all lines from the file
lines = file.readlines()

file.close()

print("=== Student Records ===")
print()

# Display the header line first
print(lines[0].strip())
print("-" * 50)

# Display each student record
for i in range(1, len(lines)):
    line = lines[i].strip()
    if line:  # skip empty lines
        # Split by comma to get each field
        fields = line.split(",")
        print("Name       :", fields[0])
        print("Roll No    :", fields[1])
        print("Program    :", fields[2])
        print("Year       :", fields[3])
        print("Group      :", fields[4])
        print("-" * 50)
