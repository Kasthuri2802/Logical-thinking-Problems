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

def are_Pairs(open,close):
    if open=='(' and close==')':
        return True
    if open=='{' and close=='}':
        return True
    if open=='[' and close==']':
        return True
    return False

def check_balance(A):
    stack=[]
    for i in A:
        if i=='(' or i=='{' or i=='[':
            stack.append(i)
        elif i==')' or i=='}' or i==']':
            if are_Pairs(stack[-1],i):
                stack.pop()
            else:
                return False
    if len(stack)==0:
        return True
    else:
        return False
            
input_string=input("Enter the input: ")
if(check_balance(input_string)):
    print("Given String is Balanced") 
else:
    print("Given String is not Balanced") 


        