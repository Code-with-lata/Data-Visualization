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



# # 2.Write a Python script to concatenate the following dictionaries to create a new one.
# # Sample Dictionary :
# # dic1={1:10, 2:20}
# # dic2={3:30, 4:40}
# # dic3={5:50,6:60}
# # Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# def concatenate_dicts(*dicts):
#     result = {}
#     for d in dicts:
#         result.update(d)
#     return result

# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# result = concatenate_dicts(dic1, dic2, dic3)
# print("Concatenated dictionary:", result)



# # 3.Write a Python program to get the key, value and item in a dictionary.
# # input:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# # Output:
# # Key 	Value
# # 1	10
# # 2	20
# # 3	30
# # 4	40
# # 5	50
# # 6	60

# def print_dict_info(dict_num):
#     print("Key\tValue")
#     for key, value in dict_num.items():
#         print(f"{key}\t{value}")

# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print_dict_info(dict_num)



# # 4.Write a Python program to get the key, value and item in a dictionary.
# # Input: input_dict = {1: 10, 2: 20, 3:None, 4: 40, 5: None, 6: 60}
# # Output:
# # dict with empty items Dropped :
# # {1:10,2:40,4:40,6:60}

# def remove_none_values(input_dict):
#     cleaned_dict = {k: v for k, v in input_dict.items() if v is not None}
#     return cleaned_dict

# input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}
# cleaned_dict = remove_none_values(input_dict)
# print("Dict with empty items dropped:", cleaned_dict)



# # 1. Write a Python program to find the number of times 4 appears in the tuple.
# # Input:
# # tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 )
# # Output: 3

# def count_occurrences(tuplex, value):
#     return tuplex.count(value)

# tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)
# count_4 = count_occurrences(tuplex, 4)
# print("Number of times 4 appears:", count_4)




# # 2.Write a Python program to convert a list to a tuple.
# # Input: listx = [5, 10, 7, 4, 15, 3]
# # Output: (5, 10, 7, 4, 15, 3)

# def list_to_tuple(lst):
#     return tuple(lst)

# listx = [5, 10, 7, 4, 15, 3]
# converted_tuple = list_to_tuple(listx)
# print("Converted tuple:", converted_tuple)



# # 3. Write a Python program to calculate the sum of the numbers in a given tuple.
# # Input: tuples_list = [(1, 2), (3, 4), (5, 6)]
# # Output: sum of tuple is : 21
 
# def sum_of_tuples(tuples_list):
#     return sum(sum(t) for t in tuples_list)

# tuples_list = [(1, 2), (3, 4), (5, 6)]
# total_sum = sum_of_tuples(tuples_list)
# print("Sum of tuple is:", total_sum)



# # 4.Write a python program and iterate the given tuples
# # Input:
# # employee1 = ("John Doe", 101, "Human Resources", 60000)
# # employee2 = ("Alice Smith", 102, "Marketing", 55000)
# # employee3 = ("Bob Johnson", 103, "Engineering", 75000)
# # Output:
# # Employee Records :
# # Name : John Doe
# # Employee ID : 101
# # Department : Human Resources
# # Salary	:  60000

# # Name : Alice Smith
# # Employee ID : 102
# # Department :Marketing
# # Salary	:  55000

# # Name : Bob Johnson
# # Employee ID : 103
# # Department : Engineering
# # Salary	:  75000

# def print_employee_records(employee_list):
#     print("Employee Records :\n")
#     for employee in employee_list:
#         name, emp_id, department, salary = employee
#         print(f"Name : {name}")
#         print(f"Employee ID : {emp_id}")
#         print(f"Department : {department}")
#         print(f"Salary : {salary}\n")

# employee1 = ("John Doe", 101, "Human Resources", 60000)
# employee2 = ("Alice Smith", 102, "Marketing", 55000)
# employee3 = ("Bob Johnson", 103, "Engineering", 75000)

# employees = [employee1, employee2, employee3]
# print_employee_records(employees)



# # 1. Write a Python program to Get Only unique items from two sets.
# # Input:
# # set1 = {10, 20, 30, 40, 50}
# # set2 = {30, 40, 50, 60, 70}
# # Output: {70, 40, 10, 50, 20, 60, 30}

# def unique_items_from_two_sets(set1, set2):
#     return set1.union(set2)

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# unique_items = unique_items_from_two_sets(set1, set2)
# print("Unique items from both sets:", unique_items)




# # 2. Write a Python program to Return a set of elements present in Set A or B, but
# # not both.
# # Input:
# # set1 = {10, 20, 30, 40, 50}
# # set2 = {30, 40, 50, 60, 70}
# # Output: {20, 70, 10, 60}

# def symmetric_difference(set1, set2):
#     return set1.symmetric_difference(set2)

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# result = symmetric_difference(set1, set2)
# print("Elements present in Set A or B, but not both:", result)



# # 3. Write a Python program to Check if two sets have any elements in common. If
# # yes, display the common elements.
# # Input:
# # set1 = {10, 20, 30, 40, 50}
# # set2 = {60, 70, 80, 90, 10}
# # Output: {10}
# def common_elements(set1, set2):
#     return set1.intersection(set2)

# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
# common = common_elements(set1, set2)
# print("Common elements:", common)




# 3. Write a Python program to Remove items from set1 that are not common to
# both set1 and set2.
# Input:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Output: {40, 50, 30}

def retain_common_items(set1, set2):
    return set1.intersection(set2)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
result = retain_common_items(set1, set2)
print("Items in set1 that are also in set2:", result)












