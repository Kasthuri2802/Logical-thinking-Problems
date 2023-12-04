""""
Problem #3
From the same file as above, read from the file, count the number of unique 4 letter words and it no of occurrences
for each word. Write this information at the end of file under the heading "Summary of 4 letter words"
"""
four_letter_words={}
words=[]
import string
def count_4_letter_words(passage):
    passage=passage.translate(str.maketrans("","",string.punctuation))
    words=passage.split()
    for word in words:
        if(len(word)==4):
            if word not in four_letter_words:
                four_letter_words[word]=1
            elif word in four_letter_words:
                four_letter_words[word]=four_letter_words[word]+1
    return four_letter_words
try:
    file=open("E:\GitHub\Logical-thinking-Problems\DAY 3\input.txt","r")
    for passage in file:
        passage = passage.lower()
    print(count_4_letter_words(passage))
    file.close()
    
    # four_letter_words="i am writing in the file"
    print(four_letter_words)

    file=open("E:\GitHub\Logical-thinking-Problems\DAY 3\input.txt","a")
    heading="Summary of 4 letter words"
    # result=print(four_letter_words)
    file.write(heading)
    file.write(four_letter_words)
    file.close()
    
    file=open("E:\GitHub\Logical-thinking-Problems\DAY 3\input.txt","r")
    print(file.read())
    file.close()


except:
    print("Something went wrong when opening the file")
   
# four={"king":1,"went":2,"deer":3}
# four["deer"]=four["deer"]+1
# print(four["deer"])
