# 11.Python program to check if the given string is a palindrome

string = input("Enter a string: ")
normalized_string = string.lower()

import re
normalized_string = re.sub(r'[^a-z0-9]', '', normalized_string)

if normalized_string == normalized_string[::-1]:
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')

