# problem #5
# In your college Python is taught in 3 different departments by the same professor. 
# For each dept, get the no of students stutying Python and their marks in the final exam 
# Get the input as comma seperated string

# Find the top 3 marks in each class
# Find the top 3 marks if all classes are combined.
# Find the avg mark of students with passing mark in each class and the classes combined.
# Find which class has the best average mark and least number of failed students.



# number of students and marks obtained in ECE dept

noOfStd_Ece = int(input("Number of Students in ECE: ")) 
EceMarks=[int(x) for x in input("Final Exam marks of ECE Students: ").split(',')]

# number of students and marks obtained in CSE dept

noOfStd_Cse = int(input("Number of Students in CSE: ")) 
CseMarks=[int(x) for x in input("Final Exam marks of CSE Students: ").split(',')]

# number of students and marks obtained in IT dept

noOfStd_IT= int(input("Number of Students in IT: ")) 
ITMarks=[int(x) for x in input("Final Exam marks of IT Students: ").split(',')]

# Find the top 3 marks in each class

EceMarks.sort(reverse = True)
CseMarks.sort(reverse = True)
ITMarks.sort(reverse = True)
print("Top 3 marks in ECE : ",end=" ")
for x in range(3):
    print(EceMarks[x],end=" ")
print()
print("Top 3 marks in CSE : ",end=" ")
for x in range(3):
    print(CseMarks[x],end=" ")
print()
print("Top 3 marks in IT : ",end=" ")
for x in range(3):
    print(ITMarks[x],end=" ")
print()

# Find the top 3 marks if all classes are combined.

allClass = EceMarks + CseMarks + ITMarks
print(allClass)
allClass.sort(reverse=True)








