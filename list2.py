#creat a list of any 20 element and display element using forward index in reverse order

List = [20,30,"hello",45.90,'good','Morning',23,-30,'fine','good','cool',45,67,89,4,34,23,23,56,78]
for x in range(len(List)-1,-1,-1):
    print(List[x])

#----Another form -----
for x in range(len(List)):
    print(List[len(List)-x-1])


#    