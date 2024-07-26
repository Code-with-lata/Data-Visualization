# Convert the below list into a numpy array then display the array then display the first and last index and than multiply each element by 2 and 
# display the result 

import numpy as np

# input data
my_list = [1,2,3,4]

my_array = np.array(my_list)

print(my_array)

print("First element:", my_array[0])
print("Last element:", my_array[-1])

# Multiply each element by 2
multiplied_array = my_array * 2

print("updated array :",multiplied_array)
