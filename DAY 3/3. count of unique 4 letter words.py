""""
Problem #3
From the same file as above, read from the file, count the number of unique 4 letter words and it no of occurrences
for each word. Write this information at the end of file under the heading "Summary of 4 letter words"
"""
four_letter_words={}
words=[]
count=0
x=0

import string
def count_4_letter_words(passage):
    passage=passage.translate(str.maketrans("","",string.punctuation))
    words=passage.split()
    for word in words:
        if(len(word)==4):
            four_letter_words[word]=count
        if word in four_letter_words:
            count=count+1
            four_letter_words[word]=count
    print(four_letter_words)




try:
    file=open("E:\GitHub\Logical-thinking-Problems\DAY 3\input.txt","r")
    for passage in file:
        passage = passage.lower()
    count_4_letter_words(passage)
    
except:
    print("Something went wrong when opening the file")
# four={"king":1,"went":2,"deer":3}
# four["deer"]=four["deer"]+1
# print(four["deer"])
