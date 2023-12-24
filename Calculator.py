#####################################################################
# ---------------------CodeSoft Internship--------------------------#
# Created: 5/12/2023 9:25:34 PM                                     #
# Author: Salah Eldeen Mohamed Hemdan                               #
# Project: Calculator                                               #
#####################################################################

############################ Function Section ################################
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

############################ Program Section ################################
# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display operation choices
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get user operation choice
choice = input("Enter choice (1, 2, 3, or 4): ")

# Perform calculation based on user choice
if choice in ('1', '2', '3', '4'):
    if choice == '1':
        result = add(num1, num2)
        operation = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        operation = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        operation = '*'
    elif choice == '4':
        result = divide(num1, num2)
        operation = '/'

    # Display the result
    print(f"{num1} {operation} {num2} = {result}")
else:
    print("Invalid choice. Please choose a valid operation (1, 2, 3, or 4).")
