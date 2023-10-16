# Function to subtract two numbers
def add(a, b):
    return a + b


# Function to subtract two numbers
def subtract(a, b):
    return a - b


# Function to multiply two numbers
def multiply(a, b):
    return a * b


# Function to divide two numbers
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# Prompt the user for input
print("User Choice:")
print("Enter 'add' for addition")
print("Enter 'subtract' for subtraction")
print("Enter 'multiply' for multiplication")
print("Enter 'divide' for division")

# Take user input for operation choice
user_choice = input("Enter operation: ")

# Take user input for two numbers
number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))

# Perform the selected operation
if user_choice == "add":
    result = add(number_1, number_2)
elif user_choice == "subtract":
    result = subtract(number_1, number_2)
elif user_choice == "multiply":
    result = multiply(number_1, number_2)
elif user_choice == "divide":
    result = divide(number_1, number_2)
else:
    result = "Invalid input. Please enter a valid operation."

# Display the result
print("Result:", result)
