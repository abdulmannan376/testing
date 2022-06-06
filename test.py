#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#

# import libraries
# import unittest 
# it is used for testing purpose

# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# TODO: update the gameboard with the user input
"""
We have to pass 2 parameters over here
First one is the position from 1 to 9
Second one is the Mark either X player or O player
1. We need to check if that specific position is empty or not in the board array
2. If it is empty then we simple need to assign mark to that position in the board array
"""
def markBoard(position, mark):
    # return printBoard
    # while not validateMove(position):
    #     print('What is your move? Please input 1-9.')
    #     move = input('> ')
    #     print(markBoard(position, move))
    position = int(position)
    if board[position] == ' ':
        board[position] = mark


# TODO: print the game board as described at the top of this code skeleton
# Will not be tested in Part 1

"""
In this function we have to draw the updated board.
We have to follow following steps to do that:
1. We need to declare an empty array for drawing updated board
2. Run the loop over each and every index of that updated array
3. Check if board value in empty then fill it with the index number of the array itself (this line will execute only one time)
4. Otherwise assign the player turn/mark to the new updated drawboard array
5. Print the updated board
"""
def printBoard():

    drawBoard = {
        1: ' ',
        2: ' ',
        3: ' ',
        4: ' ',
        5: ' ',
        6: ' ',
        7: ' ',
        8: ' ',
        9: ' '
    }

    # keys() are build in python funciton which will refer to the key of array. (1-9)
    for x in drawBoard.keys():
        if board[x] == ' ':
            drawBoard[x] = x
        else:
            drawBoard[x] = board[x]

    print(
        
        '\n' +

        str(drawBoard[1]) + ' | ' + str(drawBoard[2]) + ' | ' + str(drawBoard[3]) + '\n' +

        '--------- \n' +

        str(drawBoard[4]) + ' | ' + str(drawBoard[5]) + ' | ' + str(drawBoard[6]) + '\n' +

        '--------- \n' +

        str(drawBoard[7]) + ' | ' + str(drawBoard[8]) + ' | ' + str(drawBoard[9]) + '\n' 

    )

    """
    There is an error because we are printing string and integers inside the print funciton in a same way
    either we need to convert integer to string or either we have to convert string to integer
    str() function will convert integer to string
    """


    # return '''
    # 1 | 2 | 3
    # ---------
    # 4 | 5 | 6
    # ---------
    # 7 | 8 | 9'''



# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied

"""
Here in this function we need to check the wrong and right input value
and return True in case of right input and will return false in case of wrong input
We will follow following steps to do that:
pre_requisite point: we need to convert position into integer
1. Check if entered input is from 1 to 9 values
2. Check if that specific position is empty in the origional board array
3. If it is empty then we need to return True (Valid move)
4. Else in all the cases we have to return Flase (in valid move)
"""
def validateMove(position):

    position = int(position)

    if position >= 1 and position <= 9:

        if board[position] == ' ':

            return True

    return False



    # return position in board == int

# TODO: list out all the combinations of winning, you will neeed this
# one of the winning combinations is already done for you
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]

]

# TODO: implement a logic to check if the previous winner just win
# This method should return with True or False
"""
This funciton is declared to check the winning player. If it wins or not
We need following steps to do that:
1. Run the loop for all the possible combinations in winCombinations array
2. we need to check these combinations with the origional board array one by one (actual logic)
3. Return True in case we find the correct combination (win)
4. Return False if we havn't find the correct combination
"""
def checkWin(player):

    for combination in winCombinations:

        if board[combination[0]] == player and  board[combination[1]] == player and  board[combination[2]] == player:

            return True

    return False





    # return False
    # for x in winCombinations:
    #     if all (y in position[move] for y in x):
    #         return True


# TODO: implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean

"""
This is a function where we are simply checking if our origional board array is full or not
so we need following steps to do that
1. Run the loop over each and every value of board array
2. Inside the loop we need to check if that specific value is empty or not
3. If it is empty, return False (because board array is not yet full)
4. Else return True (because our array is full)
"""

def checkFull():

    for x in board:

        if board[x] == ' ':

            return False # we are not finished yet

    return True # array is full


    # return True
    # for k, v in board:
    #     if v == int:
    #         return False



#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################


# Now we are going to write the execution statements so that we can call all the pre-written funcitons in our code to run the game
# our code will start executing from line # 209

gameEnded = False
currentTurnPlayer = 'X'

# entry point of the whole program
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User

"""
This is main entrance of the game
We have to execute this game in following steps:
1. Get input from user [done]
2. Check if input is not valid, then prompt again for valid input (validateMove) [done]
3. Update the value to the origional Board Array (markBoard) [done]
4. print the updated board (printBoard) [done]
5. In case of winner identifies we need to announce the winner (checkWin)   [done]
6. In case of array is full and no one wins, we need to stop the game (checkFull)   [done]
7. Otherwise we have to change the player's turn either From X to O or From O to X
"""


while not gameEnded:

    move = input(currentTurnPlayer + "'s turn, input: ")

    while not validateMove(move):

        print('Oops input is not valid!. Please enter another one')

        move = input(currentTurnPlayer + "'s turn, input: ")

    markBoard(move, currentTurnPlayer)

    printBoard()

    if checkWin(currentTurnPlayer):

        print('Congratulations, Winner is: '+ currentTurnPlayer + '\n Game ends')

        gameEnded = True

    elif checkFull():

        print('Game ties, no one wins, may be next time !!!  \n Game ends')

        gameEnded = True

    else:

        if currentTurnPlayer == 'O':
            currentTurnPlayer = 'X'
        else:
            currentTurnPlayer = 'O'



"""
We need to check 3 cases
1. winning condition for both X & O player  (It done)
2. Tie condition (where no one wins) (Its done)
3. Invaid or already existing input condition
"""






# Bonus Point: Implement the feature for the user to restart the game after a tie or game over
