# Problem #2
# Same as above,but print the list in descending order
# input = [1,2,3,3,3,4,4,7,7,9]
# output = [9,7,4,3,2,1,_,_,_,_]

newList = []
dupList = []
input_list = []
n=int(input("Enter number of elements: "))
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    input_list.append(element)
input_list.sort()
print("Input list = ",input_list)
input_list.sort(reverse=True)
for i in input_list:
    if i not in newList:
        newList.append(i)
    else:
        dupList.append(i)
for i in range(len(dupList)):
    newList.append('_')
print("Output List = ",newList)