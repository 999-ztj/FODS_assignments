"""
This program creates a class called Learner with attributes:
roll_no, full_name, address, enrollment_year, program, and group.
It takes input for all attributes and displays the details.
"""

class Learner:
    def __init__(self, roll_no, full_name, address, enrollment_year, program, group):
        self.roll_no = roll_no
        self.full_name = full_name
        self.address = address
        self.enrollment_year = enrollment_year
        self.program = program
        self.group = group

    def display(self):
        print("=== Learner Details ===")
        print("Roll No         :", self.roll_no)
        print("Full Name       :", self.full_name)
        print("Address         :", self.address)
        print("Enrollment Year :", self.enrollment_year)
        print("Program         :", self.program)
        print("Group           :", self.group)


# Take input from the user
print("Enter Learner Details:")
print()
roll_no = input("Roll No         : ")
full_name = input("Full Name       : ")
address = input("Address         : ")
enrollment_year = input("Enrollment Year : ")
program = input("Program         : ")
group = input("Group           : ")

# Create a Learner object with the input
learner1 = Learner(roll_no, full_name, address, enrollment_year, program, group)

print()

# Display the learner details
learner1.display()
