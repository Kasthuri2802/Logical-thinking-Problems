# Problem #1
# Generate the following output using for loop. Go until g.
# a
# aba
# abacaba
# abacabadabacaba
# abacabadabacabaeabacabadabacaba

# look at the output and find the pattern. Hint - add next letter in the alphabet in each row

n=int(input("enter number of rows: "))
m=0
for i in range(n):
    num=97
    m=2*m+1
    for j in range(m):
        print(chr(num),end=" ")
        num+=1
    print()
   