# 14 Python program to check the validity of password input by users

import re

def is_valid_password(password):
    
    if len(password) < 8:
        return False
    
    if not re.search(r'[a-z]', password):
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'\d', password):
        return False
    
    if not re.search(r'[!@#$%^&*(),.?"\'{}|<>]', password):
        return False
    
    return True

password = input("Enter your password: ")

if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid. It must meet the following criteria:")
    print("- At least 8 characters long")
    print("- Contains both uppercase and lowercase letters")
    print("- Contains at least one digit")
    print("- Contains at least one special character (e.g., @, #, $)")
