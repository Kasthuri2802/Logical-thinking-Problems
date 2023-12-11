# Problem 3:
#   In the input, find the first A and last A, print all the letters between these two A. 
#   If there is no A or 2nd A is not found, find the first B after the first A (if there is a A) and last B and print all the letters between these two B. 
  
#   If there is no B or 2nd B is not found, find the first C after the first B (if there is a B) and last C and print all the letters between these two C. 


def letters_between_A(string):
    start_index_A = string.find("a")
    end_index_A = string.rfind("a")
    if (start_index_A == -1 and  end_index_A == -1) :
        letters_between_B(string)  
    elif(start_index_A == end_index_A):
        


    else:
        print(f"First 'A' is at index : {start_index_A}")
        print(f"Last 'A' is at index : {end_index_A}")
        print("Letters between first 'A' and last 'A' is : ",end="")
        for i in range(start_index_A+1,end_index_A):
            print(string[i],end=" ") 



input_string = input("Enter the string: ")
input_string = input_string.lower()
letters_between_A(input_string)