# 8.Write a python program finding the factorial of a given number using a while loop.
number = int(input("Enter a non-negative integer: "))

factorial = 1
original_number = number

while number > 1:
    factorial *= number
    number -= 1

print(f"The factorial of {original_number} is {factorial}.")
