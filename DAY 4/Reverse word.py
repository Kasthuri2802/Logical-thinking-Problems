# Problem #1
# write a program that reads a passage and reverses the order of 
# letters in each word while keeping the word order intact. Use function.
# Eg- input - I am Sayur
# Output I ma ruyaS

# a="kasthuri"
# print(a[::-1])

# function to reverse a string
def reverse(x):
    return x[::-1]

# function to open a file
def fileOpen():
    return open("E:\GitHub\Logical-thinking-Problems\DAY 4\input file.txt","r")

# main function  
file= fileOpen()
for line in file:   #iterate through each line in a file
    words=line.split()  #store each words in a line as list
    # print(words)
    for word in words:    #iterate through each word in a list
        print(reverse(word),end=" ")
    print()
