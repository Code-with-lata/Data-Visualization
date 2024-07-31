# 1. Declare a div() function with two parameters. Then call the function and pass two
# numbers and display their division.
def div(a,b):
    if b==0:
        return "division by zero not allowed"
    return a/b
a = int(input("enter no 1: "))
b= int(input("enter no 2: "))    
answer = div(a,b)
print("result : ",answer)


# 2. Declare a square() function with one parameter.Then call the function and pass
# one number and display the square of that number .
def square(a):
    if a ==0:
        return 0
    return a*a
a = float(input("enter number = "))
square_of_no = square(a)
print("square of number ",a,": ",square_of_no)

# 3. Using max() and min() functions display the maximum and minimum of 5 random numbers.
import numpy as np
numbers = np.random.randint(1, 100, 5)

max_num = max(numbers)
min_num = min(numbers)

print("random numbers:", numbers)
print("maximum number is:", max_num)
print("minimum number is:", min_num)


# 4. Accept a name from the user and display that in lower case using lower() function
def lower(user_name):
    lowercase_name = user_name.lower()
    return lowercase_name
user_name = input("Enter your name: ")
name = lower(user_name)
print("Your name in lower case is:",name)


# 1. Write a Python program to count the occurrences of each word in a
# given sentence
# string = “To change the overall look of your document. To change the look
# available in the gallery”

from collections import Counter
import re
sentence = "To change the overall look of your document. To change the look available in the gallery"
# Remove punctuation and split the sentence into words
words = re.findall(r'\b\w+\b', sentence.lower())
# Count the occurrences of each word
word_count = Counter(words)
print(word_count)



# 2. Write a Python program to remove a newline in Python
# String = "\nBest \nDeeptech \nPython \nTraining\n"

string = "\nBest \nDeeptech \nPython \nTraining\n"
cleaned_string = string.replace('\n', ' ').strip()
print(cleaned_string)


# 3. Write a Python program to reverse words in a string
# String = “Deeptech Python Training”

string = "Deeptech Python Training"
# Split the string into words, reverse the list, and join it back into a string
reversed_words = ' '.join(reversed(string.split()))
print(reversed_words)



# 4. Write a Python program to count and display the vowels of a given text

string = "Welcome to python Training"

vowels = "aeiouAEIOU"

vowel_count = sum(1 for char in string if char in vowels)
print(f"Total vowels are: {vowel_count}")


# 1. Write a Python program to Count all letters, digits, and special
# symbols from the given string
# Input = “P@#yn26at^&i5ve”
# Output: Chars = 8 Digits = 2 Symbol = 3

import string
input_str = "P@#yn26at^&i5ve"

# Initialize counts
letters = digits = symbols = 0

# Iterate through each character in the string
for char in input_str:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif char in string.punctuation:
        symbols += 1

print(f"Chars = {letters} Digits = {digits} Symbols = {symbols}")


# 2. Write a Python program to remove duplicate characters of a given string.
# Input = “String and String Function”
# Output: String and Function

input_str = "String and String Function"

# Split the input string into words
words = input_str.split()

# Remove duplicates while preserving order
seen_words = set()
result_words = []

for word in words:
    if word not in seen_words:
        seen_words.add(word)
        result_words.append(word)

# Join the words back into a string
output_str = ' '.join(result_words)

print(output_str)



# 3. Write a Python program to count Uppercase, Lowercase, special
# character and numeric values in a given string
# Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”
# Output:
# UpperCase : 5
# LowerCase : 18
# NumberCase : 5
# SpecialCase : 11

input_str = "Hell0 W0rld ! 123 * # welcome to pYtHoN"

uppercase = lowercase = digits = special = 0

for char in input_str:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        digits += 1
    elif not char.isspace():
        special += 1

print(f"UpperCase : {uppercase}")
print(f"LowerCase : {lowercase}")
print(f"NumberCase : {digits}")
print(f"SpecialCase : {special}")



# 4. Write a Python Count vowels in a string
# input= “Welcome to Python Assignment”

input_str = "Welcome to Python Assignment"

vowels = "aeiouAEIOU"

vowel_count = sum(1 for char in input_str if char in vowels)

print(f"Total vowels are: {vowel_count}")




