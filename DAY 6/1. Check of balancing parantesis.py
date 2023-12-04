""""
Program #1
Write a program to check if a given string of parentheses, brackets, and braces is balanced. 
For instance, "({[]})" is balanced, but "({[)})" is not
Input - (Abc[i]) or (Abc[2])
Output true
Input ((Abc[i]) or (Abc[2])) 
Output true
Input ((Abc[i]) or Abc[2)])
Output False

"""

def check_balance(input):
    open=[]
    close=[]
    for i in input:
        # print(i)
        if(i=="(" or i=="[" or i=="{"):
            open.append(i)
        elif(i==")" or i=="]" or i=="}"):
            close.append(i)
    print(open)
    print(close)
    if(len(open)==len(close)):
        return True
    else:
        return False
    
input_string=input("Enter the input: ")
print(check_balance(input_string))    

        