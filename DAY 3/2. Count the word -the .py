# Problem #2
# Read a passage from a file. 
# Count the number of times the word 'the' followed by another 'the' without 'a' in between.

# Eg The king went to the forest with the wife and a servent. The king shot a deer. The king went to the forest again the next day.

# answer is 4 (The king, the forest, The King the next)
count=0
i=0
try:
    file=open("E:\GitHub\Logical-thinking-Problems\DAY 3\input.txt","r")
    for line in file:
        line=line.lower()
        words = line.split()
        
    for i in range(len(words)):
        if(words[i]=="the"):
            if(words[i+1])
        
           
    
            
            

            
           
   
    
        
except:
    print("Something went wrong when opening the file")
