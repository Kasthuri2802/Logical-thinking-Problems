# Problem 1
# In the input, find the first A and last A, print all the letters between these two A.


def letters_between_A(string):
    
    start_index = string.find("a")
    end_index = string.rfind("a")
    print(f"First 'A' is at index : {start_index}")
    print(f"Last 'A' is at index : {end_index}")
    print("Letters between first 'A' and last 'A' is : ",end="")
    for i in range(start_index+1,end_index):
        print(string[i],end=" ") 


input_string = input("Enter the string: ")
input_string = input_string.lower()
letters_between_A(input_string)
