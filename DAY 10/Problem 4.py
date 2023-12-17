# Problem #4
# Input is an array of strings of an arithmetic expression. Calculate the value.
# eg - input ["1", "2", "+", "5", "*"]
# output =  15
# explanation (1 + 2) * 5 = 15

# input ["10", "2", "3", "+","-", "5", "*"]
# output =  25
# explanation (10 - ( 2 + 3)) * 5 = 25
# Hint : Use the concept of stack. Push and pop. 
# Parse the input list one element at a time. Convert to integer, push it to a stack. Whenever you see an
# operator, pop two elements from the stack, apply the operation and push the result back.

# input_list=[]
# stack=[]
# operator = '[+-*/%**//]'
# input_string=input("Enter an input: ")
# input_string.split()
# for i in range(len(input_string)):
#     input_list.append(input_string[i])
# print(input_list)
# for item in input_string:
#     if item in operator:
#         if item == '+' :
#             a = stack.pop()
#             b = stack.pop()
#             stack.append(a+b)
#             continue
#         if item == '-' :
#             a = stack.pop()
#             b = stack.pop()
#             stack.append(a-b)
#             continue
#         if item == '*' :
#             a = stack.pop()
#             b = stack.pop()
#             stack.append(a*b)
#             continue
#         if item == '/' :
#             a = stack.pop()
#             b = stack.pop()
#             stack.append(a/b)
#             continue
#     else:
#         stack.append(int(item))
# print(stack)

# # Get input as a string
# input_string = input("Enter elements separated by spaces: ")

# # Use strip() to remove leading and trailing whitespaces
# stripped_input = input_string.strip()

# # Split the stripped input string into an array
# input_array = stripped_input.split()

# # Display the array
# print("Input Array:", input_array)

    
    
    
        
