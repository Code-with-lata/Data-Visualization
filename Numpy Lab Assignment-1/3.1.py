# Write a numpy program to create an array of 10 zero,10 once,10 fives.

import numpy as np
arr = np.zeros((10)) 
# 10 zeros
print("Print 10 zeros in array :",arr)

arr = np.zeros((10)) +1
# 10 ones
print("Print 10 ones in array :",arr)

arr = np.zeros((10)) +5
# 10 five
print("Print 10 fives in array :",arr)