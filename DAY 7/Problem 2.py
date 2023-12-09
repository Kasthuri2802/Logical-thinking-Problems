# Problem 2:
#   In the input, find the first A and last A, print all the letters between these two A. 
#   If there is no A or 2nd A is not found, find the first B  and last B and print all the letters between these two B. 
#   If there is no B or 2nd B is not found, find the first C and last C and print all the letters between these two C. 


def letters_between_A(string):
    start_index_A = string.find("a")
    end_index_A = string.rfind("a")
    if (start_index_A == end_index_A):
        letters_between_B(string)    
    else:
        print(f"First 'A' is at index : {start_index_A}")
        print(f"Last 'A' is at index : {end_index_A}")
        print("Letters between first 'A' and last 'A' is : ",end="")
        for i in range(start_index_A+1,end_index_A):
            print(string[i],end=" ") 
        

def letters_between_B(X):
    start_index_B = X.find("b")
    end_index_B = X.rfind("b")
    if (start_index_B == end_index_B):
        letters_between_C(X)    
    else:
        print(f"First 'B' is at index : {start_index_B}")
        print(f"Last 'B' is at index : {end_index_B}")
        print("Letters between first 'B' and last 'B' is : ",end="")
        for i in range(start_index_B+1,end_index_B):
            print(X[i],end=" ") 
        

def letters_between_C(Y):
    
    start_index_C = Y.find("c")
    end_index_C = Y.rfind("c")
    print(f"First 'C' is at index : {start_index_C}")
    print(f"Last 'C' is at index : {end_index_C}")
    print("Letters between first 'C' and last 'C' is : ",end="")
    for i in range(start_index_C+1,end_index_C):
        print(Y[i],end=" ")
   


input_string = input("Enter the string: ")
input_string = input_string.lower()
letters_between_A(input_string)
