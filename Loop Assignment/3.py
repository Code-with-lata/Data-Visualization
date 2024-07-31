# 3.Python Program to Check if a Number is Positive, Negative or 0

# Input: Get a number from user
number = int(input("Enter a number: "))

# Check if the number is positive, negative or zero
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print(f"The number is zero.")
