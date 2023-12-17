# Problem #1
# You have list of unique words. you input is a string with no spaces. Return true if the letters in the 
# input string can be seperated into words that are in the list.
# eg list = ["we", "students", "are" ]
# input = "wearestudents"
# output = true
# eg 2 List = ["we", "doctor","and", "nurse", "are"]
# input = "wearenurseandoctor"
# output = False 
# input = "wearenurseanddoctor"
# output = true

words_list = ["we", "students", "are" ]
sep_list = []
i=0
input_string = input("Enter string: ")
word = ""
while(i<=len(input_string)):
    word = "".join((input_string[i],input_string[i+1]))
    if word in words_list:
        sep_list.append(word)
        i=i+1
    else:
        i=i+1
        word = "".join((word,input_string[i+1]))
        if word in words_list:
            sep_list.append(word)
            i=i+2
        
    
   
        
    

