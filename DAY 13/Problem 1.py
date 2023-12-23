# Problem #1
# Input is a range of numbers as string. Print only the numbers that are palindromes and also the 
# square of that number is also a palindrome.
# eg. 121 is a palindrome and 121 * 121 = 14641 is also a palindrome, so you can print 121
# 131 is a palindrome, but 131*131 = 17161 is not a palindrome,so you can't print it.
# eg input "10", "500"
# Make sure to identify which steps need to be a function, how to avoid unnecessary parsing 
# of numbers. Checking for palidrome or not, should be an efficient code.

def check_palindrome(first,last):
    for i in range (int(first),int(last)+1):
        temp = org_num = i
        rev = 0 
        while(i!=0):
            rem = i % 10
            rev = rev * 10 + rem
            i = int(i / 10)
        if(temp == rev):
            square = temp * temp
            temp = square
            rev = 0
            while(square!=0):
                rem = square % 10
                rev = rev * 10 + rem
                square = int(square / 10)
            if(temp==rev):
                print(org_num)
        else:
            continue
start = input("Enter Starting Number: ")
end = input("Enter Ending Number: ")
check_palindrome(start,end)
