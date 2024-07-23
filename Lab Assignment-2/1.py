# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

print("Line 1")
print("Line 2")

try:
    print(100/0)    
    
except ZeroDivisionError as e:
    print(e)
        
print("Line 3")
print("Line 4")
