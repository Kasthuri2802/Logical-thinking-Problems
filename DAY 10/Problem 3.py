# Problem #3 
# Add two number represented in a list as reversed. print the sum also as a list in reverse order
# eg input list1 = [1,2,3] list2 = [5,6,7]
# answer= [6,8,0,1]
#  explanation (321 + 765 = 1086)

list1 = []
list2 = []
n1 = int(input("Enter number of elements for list1: "))
n2 = int(input("Enter number of elements for list2: "))
for i in range(n1):
    element = int(input(f"Enter element {i+1} of list1: "))
    list1.append(element)
for i in range(n2):
    element = int(input(f"Enter element {i+1} of list2: "))
    list2.append(element)
print("List1 = ",list1)
print("List2 = ",list2)
list1.reverse()
list2.reverse()
num1 = ""
num2 = ""
for i in list1:
    num1 += str(i)
# print(num1)
for i in list2:
    num2 += str(i)
# print(num2)
result = int(num1) + int(num2)
result = str(result)
output_list=[]
for i in range(len(result)):
    output_list.append(int(result[i]))
output_list.reverse()
print("Output List = ",output_list)

