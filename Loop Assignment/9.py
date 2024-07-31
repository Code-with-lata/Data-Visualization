# 9. Accept numbers using input() function until the user enters 0. If user
# input 0 then break the while loop and display the sum of all the numbers.

total_sum = 0

while True:
    number = float(input("Enter a number (enter 0 to stop): "))
    
    if number == 0:
        break
    
    total_sum += number

print(f"The sum of all the numbers is: {total_sum:.2f}")
