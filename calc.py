#!/usr/bin/env python

import argparse

# Initialize the parser
parser = argparse.ArgumentParser(description="Simple calculator script that adds or subtracts two numbers.")

# Add arguments
parser.add_argument("num1", type=float, help="The first number")
parser.add_argument("num2", type=float, help="The second number")
parser.add_argument("-o", "--operation", choices=["add", "subtract"], default="add",
                    help="The operation to perform: add or subtract")

# Parse the arguments
args = parser.parse_args()

# Perform the operation based on the argument
if args.operation == "add":
    result = args.num1 + args.num2
elif args.operation == "subtract":
    result = args.num1 - args.num2

# Print the result
print(f"The result is: {result}")
