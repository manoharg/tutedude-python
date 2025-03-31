# Task 1
num = int(input("Enter a number: "))

if num%2==0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

# Task 2
total_sum = 0

for number in range(1, 51):
    total_sum += number 
print(f"The sum of numbers from 1 to 50 is : {total_sum}")    
