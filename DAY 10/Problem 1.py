# Problem #1
# You have a list of numbers in ascending order, but with duplicates.
# Remove the duplicated, append _ at the end for each duplicate removed 
# eg input = [1,2,3,3,3,4,4,7,7,9]
# output = [1,2,3,4,7,9,_,_,_,_]

newList=[]
dupList=[]
n = int(input("Enter number of elements: "))
input_list=[]
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    input_list.append(element)
input_list.sort()
print("Input List: ",input_list)
for i in input_list:
    if i not in newList:
        newList.append(i)
    else:
        dupList.append(i)
for i  in range(len(dupList)):
    newList.append('_')
print("OutputList: ",newList)
