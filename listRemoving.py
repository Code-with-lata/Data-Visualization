firstList = [20,30,"hello",45.90,'good','Morning',23,-30,'fine','good']
print(firstList)

#removing element from specified position
firstList.pop(7)
print(firstList)

#if index is not specified then last element is deleted of the list
firstList.pop()
print(firstList)
firstList.pop() 
print(firstList)
print(firstList.pop(6))

#Removing an element
firstList.remove("good")
print(firstList)

#Deleting elements in given range
del firstList[4:8:1]
print(firstList)

#To remove all the element
firstList.clear()
print(firstList)

 