
import sys  # Importing the sys module to access command-line arguments

# Function to perform addition
def addition(num1, num2):
    add = num1 + num2
    return add

# Function to perform subtraction
def subtraction(num1, num2):
    sub = num1 - num2
    return sub

# Function to perform multiplication
def multiplication(num1, num2):
    mult = num1 * num2
    return mult

# Fetching the first command-line argument and converting it to float
num1 = float(sys.argv[1])

# Fetching the operation (+, -, *) specified in the second command-line argument
operation = sys.argv[2]

# Fetching the second command-line argument and converting it to float
num2 = float(sys.argv[3])

# Checking the operation specified and performing the appropriate calculation
if operation == "add":  # If the operation is addition
    output = addition(num1, num2)  # Perform addition
    print(output)  # Print the result

if operation == "sub":  # If the operation is subtraction
    output = subtraction(num1, num2)  # Perform subtraction
    print(output)  # Print the result

if operation == "multi":  # If the operation is multiplication
    output = multiplication(num1, num2)  # Perform multiplication
    print(output)  # Print the result

