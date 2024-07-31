# # 1. Write a Python program to sum all the items in a list.

# def sum_of_list(items):
#     total = 0
#     for item in items:
#         total += item
#     return total

# my_list = [1, 2, 3, 4, 5]
# print("The sum of the list is:", sum_of_list(my_list))


# # 2. Write a Python program to get the largest and smallest number from a list without builtin functions.

# def get_largest_and_smallest(numbers):
#     if not numbers:  # Check if the list is empty
#         return None, None

#     largest = numbers[0]
#     smallest = numbers[0]

#     for number in numbers[1:]:
#         if number > largest:
#             largest = number
#         if number < smallest:
#             smallest = number

#     return largest, smallest

# my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# largest, smallest = get_largest_and_smallest(my_list)
# print("The largest number is:", largest)
# print("The smallest number is:", smallest)


# # 3. Write a Python program to find duplicate values from a list and display those.

# def find_duplicates(items):
#     seen = set()
#     duplicates = set()
    
#     for item in items:
#         if item in seen:
#             duplicates.add(item)
#         else:
#             seen.add(item)
    
#     return list(duplicates)

# my_list = [1, 2, 2, 3, 4, 4, 5]
# duplicates = find_duplicates(my_list)
# print("Duplicate values:", duplicates)


# # 4. Write a Python program to split a given list into two parts where the length of the first
# # part of the list is given.
# # Original list:# [1, 1, 2, 3, 4, 4, 5, 1]
# # Length of the first part of the list: 3
# # Splitted the said list into two parts:
# # ([1, 1, 2], [3, 4, 4, 5, 1])

# def split_list(lst, split_index):
#     if split_index > len(lst):
#         return lst, []
#     return lst[:split_index], lst[split_index:]

# original_list = [1, 1, 2, 3, 4, 4, 5, 1]
# length_of_first_part = 3
# first_part, second_part = split_list(original_list, length_of_first_part)
# print("Splitted list:", (first_part, second_part))



# # 5. Write a Python program to traverse a given list in reverse order, and print the
# # elements with the original index.
# # Original list:
# # ['red', 'green', 'white', 'black']
# # Traverse the said list in reverse order:
# # black
# # white
# # green
# # red

# def traverse_reverse_with_index(lst):
#     for index in range(len(lst) - 1, -1, -1):
#         print(f"Index {index}: {lst[index]}")

# original_list = ['red', 'green', 'white', 'black']
# print("Traverse the list in reverse order:")
# traverse_reverse_with_index(original_list)



# # 1. Write a Python program and calculate the mean of the below dictionary.
# #  test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}
# # # Output: 6.2

# def calculate_mean(test_dict):
#     values = test_dict.values()
#     mean = sum(values) / len(values)
#     return mean

# test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}
# mean = calculate_mean(test_dict)
# print("Mean of the dictionary values:", mean)



# 2.Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def concatenate_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

# Example usage
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = concatenate_dicts(dic1, dic2, dic3)
print("Concatenated dictionary:", result)







