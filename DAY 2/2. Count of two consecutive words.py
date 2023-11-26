# Problem #2
# Write a program that reads a passage or string and counts the occurrences of two consecutive words 
# that are the same without any other specific word in between.
#  For example, count the occurrences of "apple apple" but not "apple orange apple."

def count_consecutive_words(text):      #fuction to count the occurrences of two consecutive words
        text=text.lower()                #to convert the input text into lower case
        words = text.split()             #split the sentence as a word 
        count=0                          #for counting the two consecutive words 
        for i in range(len(words)-1):    #loop through each words in the list
            if(words[i]==words[i+1]):    # to check the consecutive words is same or not
                count+=1                 #if consecutive words is same increase the count by 1
        return count

inputSentence = "apple Orange orange apple grapes apple apple"  
result= count_consecutive_words(inputSentence)
print("Number of consecutive word occurrence is: ",result)
    

