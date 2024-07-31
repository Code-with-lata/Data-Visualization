# 1. Using input() function take one number from the user and using ternary operators
# check whether the number is even or odd

number = int(input("Enter a number: "))

result = "Even" if number % 2 == 0 else "Odd"

print("The number", number, "is", result + ".")


# 2. Using input function take two number and then swap the number
#  user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Swap the numbers
temp= num1
num1 = num2
num2 = temp

# Print the swapped numbers
print("After swapping: First number =", num1, "Second number =", num2)


# 3. Write a Program to Convert Kilometers to Miles
#  user input
kilometers = int(input("Enter the distance in kilometers: "))

# Conversion factor
convert_kl_m = 0.621371

# Convert kilometers to miles
miles = kilometers * convert_kl_m

# Print the result
print(kilometers, "kilometers is equal to", miles, "miles.")


# 4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year

principal_rs = 200
time = 5
# Annual interest rate (percent)
rate_of_interest = 5
# Simple Interest
simple_interest = (principal_rs * time * rate_of_interest) / 100

# Print the result
print("The Simple Interest on Rs.", principal_rs, "for", time, "years at", rate_of_interest, "% per year is Rs.", simple_interest)
