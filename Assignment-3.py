 # Task 1
def factorial(num):
    ans = 1
    for i in range(1, num+1):
         ans = ans*i
         
    return ans

num = int(input("Enter a number : "))
ans = factorial(num)
print(f"Factorial of the number is : {ans}")

# Task 2
    
import math

number = float(input("Enter a number: "))


square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)

# Displaying the calculated results
print(f"Square Root: {square_root}")
print(f"Logarithm: {natural_log}")
print(f"Sine: {sine_value}")
