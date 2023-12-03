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

import random
player_A_points=0
player_B_points=0
player_points=0
#function to print the game board

def print_gameBoard(game_board):
    for row in game_board:
        print(' '.join(row))
    print()

#function for rolling the dice

def rolling_dice():
    return random.randint(1,6)

# function to add points and  add initial of the player

def player_turn(PlayerName):
    row=rolling_dice()-1
    col=rolling_dice()-1
    if(game_board[row][col] != PlayerName and game_board[row][col] != "*" ):
        player_points=1
    game_board[row][col]=PlayerName
    return player_points


user_input=input("Are you a 'Player A' or 'Player B'(Type a or b): ")
user_input=user_input.upper()
game_board=[]
for row in range(1,7):
    column=[]
    for col in range(1,7):
        column.append("*")
    game_board.append(column)
print_gameBoard(game_board)



while(player_A_points<5 and player_B_points<5):
    if (player_turn(user_input) == 1):
        if(user_input=='A'):
           player_A_points+=1
        else:
            player_B_points+=1
    if(player_A_points==5 or player_B_points==5):
        break
print(player_A_points)
print(player_B_points)
