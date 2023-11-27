# Problem 1
# Print the following pattern
#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1

# Observe how the nunmbers in the triangle are calculated. 
# Do it in two steps. Work on the generating the numbers first in right angle triangle
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

# And then work on the final output using proper indendation

# noOfRows=int(input("Enter number of rows: "))
# for row in range(noOfRows):
#     for col in range(row+1):
#         if(col==0 or row==0):
#             p=1
#             print(p ,end=" ")
#         else:
#             p=int((p*(row-col+1))/col)
#             print(p,end=" ")
#     print()
# Enter number of rows: 5
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

noOfRows=int(input("Enter number of rows: "))
for row in range(noOfRows):
    for space in range(row,noOfRows):
        print(" ",end="")
    for col in range(row+1):
        if(col==0 or row==0):
            p=1
            print(p,end=" ")
        else:
            p=int((p*(row-col+1))/col)
            print(p,end=" ")
    print()