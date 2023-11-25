# Problem #2
# you have a list of student names and another list with their marks in CS. 
# hard code the values. no need to get it as input
# Pass mark is 50.
# Print a new list with all the students with pass marks along with their mark in the format name:mark.
# Also print the number of students who failed.

studentsName=["kasthuri","jothika","praveen","jegan","vishali","santhosh","madhu"] #list of students name
CSMark=["45","38","20","80","90","85","60"] #list of CS marks
newList=[] #list for storing the result
noOfFailures=0 #variable to find the number of failed students
for x in range(len(CSMark)): #to loop through the CS mark list
    if(int(CSMark[x])>=50): #checking for the pass mark
        new = studentsName[x] + " : " + CSMark[x]  #store the result as in given format i.e) name:mark
        newList.append(new) #adding result to the newlist 
    else:
        noOfFailures+=1  #for calculating the number of failed students
print(newList)  
print("Number of students who failed are: ",noOfFailures)




    