# Problem #2
# You have 6 x 6 game board where each cell is shown as a *
# This is a two player dice game. The die has numbers 1 to 6.
# Each player rolls the dice twice. First roll is row number, second roll is col number.
# After the player rolls the dice, in the (row,col) enter the player's initial. 
# If the player  A rolls the dice and  if  player B already has their initial in the same row,col
# add a point to A and change the initial to A. 

# Player who gets 5 points first wins the game.
# Print the board each time after the user rolls and also print the current score.
# Use functions 


import random  #random module to get dice numbers

# Game of Player A

def gameOfPlayerA():
    print()
    print("*********** Dice rolled by Player A **********")
    print()
    rowNumber_A = random.randint(1,6)  # for getting the row number
    print("Number gets after first roll is (RowNumber): ",rowNumber_A)
    colNumber_A = random.randint(1,6)  # for getting the column number
    print("Number gets after second roll is (ColumnNumber): ",colNumber_A)
    print()
    for row in range(1,7):      # to print the 6*6 game board
        for col in range(1,7):
            if(row==rowNumber_A and col==colNumber_A):  # to print the initial in the respective row and column
                print("A",end=" ")
            else:
                print("*",end=" ")
        print()
    print()
    continuePlaying = input("Press 'Y' to continue the game and Press 'N' to exit the game: ") # for asking the player to continue the game or not
    if (continuePlaying=='y' or continuePlaying=='Y'): # if YES player B plays the game
        gameOfPlayerB()
    else:  # Else game gets ended
        exit

# Game of Player B

def gameOfPlayerB():
    print()
    print("********** Dice rolled by Player B ***********")
    print()
    rowNumber_B = random.randint(1,6)   # for getting the row number
    print("Number gets after first roll is (RowNumber): ",rowNumber_B)
    colNumber_B = random.randint(1,6)   # for getting the col number 
    print("Number gets after second roll is (ColumnNumber): ",colNumber_B)
    print()
    for row in range(1,7):       # to print the 6*6 game board
        for col in range(1,7):
            if(row==rowNumber_B and col==colNumber_B):   # to print the initial in the respective row and column
                print("B",end=" ")
            else:
                print("*",end=" ")
        print()
    print()
    continuePlaying = input("Press 'Y' to continue the game and Press 'N' to exit the game: ") # for asking the player to continue the game or not
    if (continuePlaying=='y' or continuePlaying=='Y'): # if YES player A plays the game
        gameOfPlayerA()
    else:                        # Else game gets ended
        exit


# for initial Play

player=input("Are you 'Player A' or 'Player B': ")  
if(player == 'a' or player == 'A'):
    gameOfPlayerA()
elif(player == 'b' or player == 'B'):
    gameOfPlayerB()



