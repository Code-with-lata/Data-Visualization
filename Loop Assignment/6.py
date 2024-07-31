#6. Write a python program to reverse a number using a while loop.

number = int(input("Enter an integer number: "))
reversed_number = 0
original_number = number

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10

print(f"The reversed number of {original_number} is : {reversed_number}.")
