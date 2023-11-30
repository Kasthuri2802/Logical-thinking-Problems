# Problem #2
# Read a passage from a file. 
# Count the number of times the word 'the' followed by another 'the' without 'a' in between.

# Eg The king went to the forest with the wife and a servent. The king shot a deer. The king went to the forest again the next day.

# answer is 4 (The king, the forest, The King the next).

try:
    file=open("E:\GitHub\Logical-thinking-Problems\DAY 3\input.txt","r")
    for line in file:
        words = line.split()
    print(words)
    for word in range(len(words)-1):
        word = word.lower()
        # if(word=="the"):

            

    
except:
    print("Something went wrong when opening the file")
