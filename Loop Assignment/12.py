# 12. Python program to check if a given number is an Armstrong number
number = int(input("Enter an integer number: "))

original_number = number
num_digits = len(str(number))
sum_of_powers = 0

while number > 0:
    digit = number % 10
    sum_of_powers += digit ** num_digits
    number //= 10

if sum_of_powers == original_number:
    print(f"{original_number} is an Armstrong number.")
else:
    print(f"{original_number} is not an Armstrong number.")
