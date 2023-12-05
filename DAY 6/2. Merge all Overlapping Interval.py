"""
Program 2
Given a collection of two numbers that specify an interval, merge all overlapping intervals. 
For example, 
Input [[1,3],[2,6],[8,10],[15,20],[16,25] ]
Output [[1,6],[8,10],[15,25]].

 """
# overlapping intervals
# [[1,3],[2,6]] --> [1,3] = 1,2,3 ; [2,6] = 2,3,4,5,6
# [[1,3],[2,6]] = [1,2,3,4,5,6] = [1,6]

outer_list=[]
n=int(input("Enter number of intervals: "))
for i in range(n):
    inner_list=[]
    for j in range(2):
        x=int(input("Enter number: "))
        inner_list.append(x)
    outer_list.append(inner_list)
for i in range(len(outer_list)):
    for j in range(len(inner_list)):
        
