#task 1
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Performing the operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division to avoid division by zero error
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (cannot divide by zero)"

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")

## Task 2
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenating first name and last name into the full name
full_name = first_name + " " + last_name

# Printing a personalized greeting message
print(f"\nHello, {full_name}! Welcome to python program.")
