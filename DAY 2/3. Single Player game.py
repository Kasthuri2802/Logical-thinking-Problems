# Problem #3
# Its is a single player game where the user starts with 0 points. User keeps rolling the 
# dice.If the rolled number is 0, game ends. If the rolled number is even, then 2 points are
#  added. If the number is odd, then if the number is 1,3 then the user has to jump. 
#  If the number is 5, then 3 points are added. The game ends when the user has 50 points.

import random

Points=0
while(Points<50):
    print()
    rolledNumber=random.randint(0,6)
    print("The number gets after rolling the dice is: ",rolledNumber)
    if(rolledNumber==0):
        print("Your Point is: ",Points)
        print("SORRY! You lost the game")
        break
    elif(rolledNumber%2==0):
        Points+=2
        print("Your Point is: ",Points)
    elif(rolledNumber==1 or rolledNumber==3):
        print("You need to jump")
        print("Your Point is: ",Points)
    else:
        Points+=3
        print("Your Point is: ",Points)
if(Points>=50):
    print("Your point is greater than or equal to 50. So, the game ends")