#!/usr/bin/env python

# Data Types
int_var = 42
float_var = 3.14
str_var = "Hello, world!"
list_var = [1,3,5,7,9]
muli_dim_list_var = [[1,2,3],[4,5,6]]
dict_var = {"foo": "bar", "fizz": "buzz"}
tuple_var = (1,2)
singleton_var = (1,)

# Order of Operations (PEMDAS)
standard_result = 1 + 2 * 3              # Output: 7 (multiplication, then addition)
paren_result = (1 + 2) * 3               # Output: 9 (parenthesis addition, then multiplication)
multi_expression_result = 1 - 2 * 3 + 4  # Output: -1 multiplication, then left to right
multi_paren_result = (1 - 2) * (3 + 4)   # Output: -7 parens, then multiplication
exp_result = 2 ** 3                      # Output: 8 (2 cubed)
exp_func_result = pow(2, 3)
mod_result = 5 % 3                       # Output: 2 (division remainder)

# File Management
file_path = 'example.text'

# Write to a file
with open(file_path, 'w') as file:
    file.write("Hello, world!\n")
    file.write("This is another line.\n")

# Append to a file
with open(file_path, 'a') as file:
    file.write("Appended line!\n")

# Read a file
with open(file_path, 'r') as file:
    content = file.read()
    print(content)

# Manually open and close a file
file = open('example.txt', 'r')
try:
    content = file.read()
    print(content)
finally:
    file.close()

# Create a file
with open("new.txt", "w") as file:
    # Write some text to the file
    file.write("I'm alive!")

# Delete a file
import os

new_path = "new.txt"

# Check if the file exists before attempting to delete
if os.path.exists(new_path):
    file_size = os.stat(file_path).st_size # Get the file size
    print(f"The size of '{file_path}' is: {file_size} bytes")

    os.remove(new_path)  # Delete the file
    print(f"{new_path} has been deleted.")
else:
    print(f"{new_path} does not exist.")


# Multi Return Function
def calculate(a, b):
    sum_res = a + b
    diff_res = a - b

    # Return multiple values
    return sum_res, diff,res

# Call the function and unpack the results
sum_val, diff_val = calculate(10, 5)

print("Sum:", sum_val)          # Output: Sum: 15
print("Difference:", diff_val)  # Output: Difference: 5

# Determine location and insert data within a file

file_name = 'sample_file.txt'
with open(file_name, 'w') as file:
    file.write("First line\n")
    file.write("Insert above")

insert_text = "INSERTED TEXT\n"

with open(file_name, 'r+') as file:
    content = file.read()

    position = content.find("Insert above")  # Create a variable for the insert position

    # If the position was found, insert the new text
    if position != -1:
        # Move the cursor to the desired position and write the insertion data
        file.seek(position)
        file.write(insert_text)
        file.write(content[position:])  # Append the rest of the content
    else:
        print("Position not found.")

# Read and print the modified content
with open(file_name, 'r') as file:
    modified_content = file.read()
    print("Modified file content:")
    print(modified_content)



# User Input
def greet_user():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

greet_user()

# Recursive Function
def factorial(n):
    # Base case if n is 0 or 1, the factorial is 1
    if n == 0 or n ==1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

factorial(5) # 120

# Data Validation
def safe_division():
    while True:
        try:
            numerator = float(input("Enter the numerator: "))
            denominator = float(input("Enter the denominator: "))

            result = numerator / denominator

            print(f"The result of {numerator} divided by {denominator} is: {result}")
            break  # Exit the loop after successful division

        except ValueError:
            print("Invalid input! Please enter numeric values.")

        except ZeroDivisionError:
            print("Error: Cannot divide by zero! Please enter a non-zero denominator.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

safe_division()

# Conditional Statements
def simple_for_loop():
    numbers = [1,2,3]
    for num in numbers:
        print(num)

def simple_while_loop():
    count = 1
    while count <= 3:
        print(count)
        count += 1

# Command line arguments
