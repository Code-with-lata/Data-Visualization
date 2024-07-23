# Write a Python program that prompts the user to input a integer and raise a valueError exception if the input is not a valid integer.

def get_integer():
    try:
        user_input = input("Please enter an integer: ")
        user_integer = int(user_input)
        print(f"You entered the integer: {user_integer}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Run the function to prompt the user
get_integer()