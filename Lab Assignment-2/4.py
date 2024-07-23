# Write a Python program that prompts the user to input two number and raises a TypeError exception if the input are not  numerical

def get_number(prompt):
    user_input = input(prompt)
    if not user_input.isdigit():
        raise TypeError(f"Error: '{user_input}' is not a numerical input.")
    return int(user_input)

def main():
    try:
        num1 = get_number("Enter thje first number: ")
        num2 = get_number("Enter the second number: ")
        print(f"The numbers you entered are {num1} and {num2}.")
    except TypeError as e:
        print(e)

if __name__ == "__main__":
    main()
