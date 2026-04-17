"""
This program reads content from one file and copies it into another file.
The user enters both file names. It uses try/except to handle errors
such as input file not found or output file already existing.
"""

import os

print("=== File Copy Program ===")
print()

# Get file names from user
input_file = input("Enter the name of the input file: ")
output_file = input("Enter the name of the output file: ")

print()

try:
    # Check if input file exists
    if not os.path.exists(input_file):
        print("Error: Input file does not exist.")
    # Check if output file already exists
    if os.path.exists(output_file):
        print("Error: Input file does not exist.")
    # Read from input file
    file_in = open(input_file, "r")
    content = file_in.read()
    file_in.close()

    # Write to output file
    file_out = open(output_file, "w")
    file_out.write(content)
    file_out.close()

    print(f"File copied successfully from '{input_file}' to '{output_file}'.")

except FileNotFoundError as e:
    print(e)

except FileExistsError as e:
    print(e)

except Exception as e:
    print("An unexpected error occurred:", e)
