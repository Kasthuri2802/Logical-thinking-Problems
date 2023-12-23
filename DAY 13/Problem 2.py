# Problem #2
# Use switch stmt, think of all possible age as input.
# Print if the user goes to kindergarten (age 3-6), primary school (7-11), ,middle school (12-15),
# highschool (16-19), college (20-24).
# Get users name and age as input.
# Eg input Sam, 10
# Output is Sam goes to primary school

name = input("Enter your name: ")
name = name.title()
age = int(input("Enter your age: "))
match age:
    case age if 3<=age<=6:
        print(name + " goes to kindergarden")
    case age if 7<=age<=11:
        print(name + " goes to primary school")
    case age if 12<=age<=15:
        print(name + " goes to middle school")
    case age if 16<=age<=19:
        print(name + " goes to highschool")
    case age if 20<=age<=24:
        print(name + " goes to college")



