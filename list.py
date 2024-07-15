#list of 10 element
firstList = [20,30,"hello",45.90,'good','Morning',23,-30,'fine','good']
#Display complete list
print(firstList)

#display list without any format
print(*firstList)

#display element using For loop
for x in firstList:
    print(x)

#display the length of the list
print ("No of element : " ,len(firstList))

#forward indexing
print("----- Forward indexing")
for x in range(len(firstList)):
   print(firstList[x]) 

#Backword indexing
print("-----Backword indexing-------")
for x in range(-len(firstList),0,+1):
    print(firstList[x])

#insertion in list

#insertion at the end
firstList.append(10)
print("after inserting the end ",firstList)   

#To insert multiple element
# x = (input("enter the element : "))
# firstList.extend(x)
# print("after inserting",x, "the end ",firstList)

#insert element nth position
firstList.insert(4,34)
print("after inserting the nth position ",firstList)  

#question
#to insert all the element of anyother sequence datatype 
# into a given list at specific position as separate element

