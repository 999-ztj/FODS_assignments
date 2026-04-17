"""
This program accepts two integers from the user, performs addition,
subtraction, multiplication, and division, and saves results to a file
with the current date and time. It keeps running until the user exits.
"""

import datetime

# File to save results
output_file = "results.csv"

print("=== Calculator with File Saving ===")
print("Type 'exit' when asked for first number to quit.")
print()

# Keep running until user wants to exit
while True:
    # Ask for first number or exit
    first_input = input("Enter first number (or 'exit' to quit): ")

    if first_input.lower() == "exit":
        break

    second_input = input("Enter second number: ")

    # Convert to integers
    num1 = int(first_input)
    num2 = int(second_input)

    # Get current date and time
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    # Perform operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    # Handle division by zero
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Cannot divide by zero"

    # Save results to file (append mode)
    file = open(output_file, "a")
    file.write(f"Date/Time  : {timestamp}\n")
    file.write(f"Numbers    : {num1} and {num2}\n")
    file.write(f"Addition   : {addition}\n")
    file.write(f"Subtraction: {subtraction}\n")
    file.write(f"Multiply   : {multiplication}\n")
    file.write(f"Division   : {division}\n")
    file.write("-" * 40 + "\n")
    file.close()

    print(f"Results saved at {timestamp}")
    print()

# Show file contents when user exits
print()
print("=== Saved Results ===")
file = open(output_file, "r")
contents = file.read()
file.close()
print(contents)
