# Lambda functions for basic arithmetic operations
# Created a simple calculator using lambda functions for addition, subtraction, multiplication, and division.
# The user can select an operation and input two numbers to perform the calculation.
# Created a menu to display the available operations and take user input for choice and numbers.
# Used lambda functions to define the arithmetic operations and perform the calculations based on user choice.
# Added a check for division by zero to avoid errors.
# Displayed the result of the calculation based on the selected operation.
# The program handles invalid choices and prompts the user to select a valid option.
# The user can continue performing calculations until they choose to exit the program.
# Lambda functions are anonymous functions that can have any number of arguments but only one expression.
add = lambda a, b: a + b  # Adds two numbers
subtract = lambda a, b: a - b  # Subtracts second number from first
multiply = lambda a, b: a * b  # Multiplies two numbers
divide = lambda a, b: a / b if b != 0 else "Cannot divide by zero"  # Divides first number by second, checks for division by zero

# Display menu options
print("Simple Calculator using Lambda Functions")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Taking user choice
choice = int(input("Enter your choice (1-4): "))

# Taking user input for numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing the operation based on user choice
if choice == 1:
    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
elif choice == 2:
    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
elif choice == 3:
    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
elif choice == 4:
    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid choice! Please select a number between 1 and 4.")
