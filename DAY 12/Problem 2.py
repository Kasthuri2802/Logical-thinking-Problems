# Problem #2
# Input is an integer list and another integer k. Output is the k most frequently occuring numbers.
# output can be in any order.
# eg input = [1,1,1,2,2,3,5,5,5,5], k =2
# output [1,5] (top 2 most frequently occuring numbers)
# input = [4,5,4,5,4,5,3,3,3,7,8,1,1,1], k = 4
# output [4,5,3,1]



input_list = []
output=[]
n = int(input("Enter number of elements: "))
for i in range(n):
    element = int(input(f"Enter number {i+1}: "))
    input_list.append(element)
k = int(input("Enter K (most frequently occuring numbers): "))
dict = {}
for ele in input_list:
    if ele not in dict:
        dict[ele]=1
    else:
        dict[ele]+=1

sort_dict = sorted(dict.items(),key=lambda x:x[1],reverse=True)        # x = lambda a : a + 10   print(x(5))  Output=15
print(sort_dict)
result = [key[0] for key in sort_dict]
for i in range(k):
    output.append(result[i])
print(f"The {k} most frequently occuring numbers are = ",output)
        




    




    
    






