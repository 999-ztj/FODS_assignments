"""
This program creates a Staff class with attributes: emp_id, full_name,
address, phone_number, marital_status, dependents, and salary.
It allows adding multiple staff members, saves them to staff.csv,
and displays the list of staff. Uses try/except for error handling.
"""

import csv
import os

class Staff:
    def __init__(self, emp_id, full_name, address, phone_number, marital_status, dependents, salary):
        self.emp_id = emp_id
        self.full_name = full_name
        self.address = address
        self.phone_number = phone_number
        self.marital_status = marital_status
        self.dependents = dependents
        self.salary = salary


def save_to_file(staff_list):
    try:
        file = open("staff.csv", "w", newline="")
        writer = csv.writer(file)

        # Write header
        writer.writerow(["emp_id", "full_name", "address", "phone_number",
                         "marital_status", "dependents", "salary"])

        # Write each staff record
        for s in staff_list:
            writer.writerow([s.emp_id, s.full_name, s.address, s.phone_number,
                             s.marital_status, s.dependents, s.salary])
        file.close()
        print("Staff data saved to staff.csv")

    except Exception as e:
        print("Error saving file:", e)


def view_staff():
    try:
        if not os.path.exists("staff.csv"):
            print("No staff file found. Please add staff first.")
            return

        file = open("staff.csv", "r")
        reader = csv.reader(file)
        rows = list(reader)
        file.close()

        print()
        print("=== Staff List ===")
        print("-" * 60)
        for row in rows:
            print(", ".join(row))
        print("-" * 60)

    except Exception as e:
        print("Error reading file:", e)


# Main program
staff_list = []

print("=== Staff Management System ===")
print()

while True:
    print("1. Add Staff Member")
    print("2. View All Staff")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        print()
        emp_id = input("Employee ID    : ")
        full_name = input("Full Name      : ")
        address = input("Address        : ")
        phone_number = input("Phone Number   : ")
        marital_status = input("Marital Status : ")
        dependents = input("Dependents     : ")
        salary = input("Salary         : ")

        new_staff = Staff(emp_id, full_name, address, phone_number,
                          marital_status, dependents, salary)
        staff_list.append(new_staff)
        save_to_file(staff_list)
        print()

    elif choice == "2":
        view_staff()
        print()

    elif choice == "3":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
        print()
