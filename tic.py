#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#

# import libraries
# from turtle import position
from email.headerregistry import HeaderRegistry
import unittest

# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# TODO: update the gameboard with the user input
"""
We have to pass two parametes over here
First one is the position from 1 to 9
Second parameter is the Mark eith X, O (player)
We need to do the following in this function:
1. We have to check if that specific position is empty or not in the origional baord array
2. If it is empty then we need to fill it with the mark
"""
def markBoard(position, mark):
    if board[position] == ' ':
        board[position] = mark # board at the position is = to marker



# TODO: print the game board as described at the top of this code skeleton
# Will not be tested in Part 1

"""
Here we need to draw the updated board. Not just the board itself.
Because board value are changing after each player's turn
We have to follow following steps:
1. Declare an empty array for drawing the updated baord
2. Run the loop over each and every value of that drawbaord array
3. Check if board value is empty then fill it with the index numebr array itslef (may be this line executes only once)
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
    # keys() are build in python function through which you can read all the keys of the array
    for x in drawBoard.keys():
        if board[x] == ' ':
            drawBoard[x] = x # we are simply changing space to numbers
        else:
            drawBoard[x] = board[x]

    """
    We are print two types of variable over Here
    Intege and string so idea behind is either we need to convert string to integer
    or either we need to convert integer to string
    str() function is another build in python function which will convert any values to string
    """
    
    print(
        '\n' +

        str(drawBoard[1]) + ' | ' + str(drawBoard[2]) + ' | ' + str(drawBoard[3]) + '\n' +

        '---------- \n' +

        str(drawBoard[4]) + ' | ' + str(drawBoard[5]) + ' | ' + str(drawBoard[6]) + '\n' +

        '---------- \n' +

        str(drawBoard[7]) + ' | ' + str(drawBoard[8]) + ' | ' + str(drawBoard[9]) + '\n'

    )




    # print(board['1'] + '|' + board['2'] + '|' + board['3'])
    # print('-----')
    # print(board['4'] + '|' + board['5'] + '|' + board['6'])
    # print('-----')
    # print(board['7'] + '|' + board['8'] + '|' + board['9'])

#Possible to use return board?

# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied

"""
Here in this function we need to check the wrong and right input value
and return True in case of valid input value
and return False in case of in-valid input value
We can do that by following steps:
Prerequisite_step: We need to convert out position to Integer
1. Check if entered input is from 1 to 9 (we need to ensure this thing)
2. Check if that specific position  is empty in the origional baord array or not 
3. If it is empty then we need to return True (because its our valid move)
4. Else in all the cases we have to return False
"""
def validateMove(position):
    position = int(position)
    if position >= 1 and position <= 9:
        if board[position] == ' ':
            return True

    return False




    # if board[position] == 'X' or 'O':
    #     return True
    # else:
    #     return False

# TODO: list out all the combinations of winning, you will need this
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

# These values are for the first iteration of the loop:

# combinations[0] = 4

# combinations[1] = 5

# combinations[3] = 6

# TODO: implement a logic to check if the previous winner just win
# This method should return with True or False

"""
We are writing this fucntion to check if current player wins or not
So we need folowing steps to do that:
1. Run the loop for all the possible combinations in winCombinations array
2. We need to check these combinations with the origional board updated array one by one (check for each and every value) //
point number is 2 is our main logic over here
3. Return True in case we will find the correct winning combination
4. Return False if we havn't find the correct one
"""
def checkWin(player):

    for combinations in winCombinations:
        if board[combinations[0]] == player and  board[combinations[1]] == player and  board[combinations[2]] == player:
            return True
            
    return False


    # for i in board:
    #     if (position[board[i][1]] == player and
    #         position[board[i][2]] == player and
    #         position[board[i][3]] == player):
    #         return True
    # return False


# TODO: implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean

"""
In this function we are simply checking if our origional board array is already full or not
So for this we have following steps:
1. Run the loop over each and every index value of origional board array
2. Check if that specific value is empty or not
3. If it is empty then we need to return false (because our board array is not yet full)
4. Otherwise we have to return True (because our array is full now)
"""

def checkFull():

    for x in board:
        if board[x] == ' ':
            return False # not yet full. We are not yet finished

    return True # array is  full now


#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################

# Our program will start execution from line number 201
gameEnded = False

#  this gameEnded variable is some thing which we are using for termination of for loop
# We are going to terminate the loop if value of this variable is true
currentTurnPlayer = 'X'
# This currentTurnPlayer variable states that we are assigning first turn to X player
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
We have to execute this game in following steps one by one
1. Get input from user
2. Check if that input is not valid then prompt again for the valid input (validateMove function)
3. Update the value of origional baord array, (for this we have markBoard)
4. Print the updated board (printBoard)
5. In case of winner identifies we need to announce the winner and end the game (checkWin function)
6. In case of array is full and no one wins. We need to stop the game (checkFull function)
7. Otherwise we need to change the player's Turn From X to O, and O to X (player)
"""
while not gameEnded:
    move = input(currentTurnPlayer + "'s turn, input: ")

    while not (validateMove(move)):
        print('Oops, wrong input, Please try again!!! ')
        move = input(currentTurnPlayer + "'s turn, input: ")

    markBoard(int(move), currentTurnPlayer)
    printBoard()

    # So now we are going to announce the winner

    if (checkWin(currentTurnPlayer)):
        print("Congratulation, Winner is= " + currentTurnPlayer + '\n Game ends')
        gameEnded = True

    elif checkFull():
        print("Sorry no one wins, Game Tie. Better luck next time")
        gameEnded = True
    # Here we are going to change the Turn of the player

    else:

        if (currentTurnPlayer == 'X'):

            currentTurnPlayer = 'O'

        else:

            currentTurnPlayer = 'X'





"""
Now We are going to test this code for 3 cases
1. Winning [checked]
2. Tie game (where no one wins)  [checked]
3. For wrong input (that wrong input may be the duplicate input or it might be the number above 9)
"""


"""
All the functions which we have written above are useless if we cannot call them inside our 
main executable code
"""

# Main Program, a Tester for your functions
# It does not cover the printBoard() function.

"""
tc = unittest.TestCase()

# Test validateMove()
tc.assertEqual(validateMove(0), False, "validateMove() didn't work as expected with input : 0")
tc.assertEqual(validateMove(10), False, "validateMove() didn't work as expected with input : 10")
tc.assertEqual(validateMove('1'), True, "validateMove() didn't work as expected with input : 1")
tc.assertEqual(validateMove('5'), True, "validateMove() didn't work as expected with input : 5")
tc.assertEqual(validateMove('9'), True, "validateMove() didn't work as expected with input : 9")

testBoard = {
    1: 'X', 2: 'O', 3: 'X',
    4: 'O', 5: 'X', 6: 'O',
    7: ' ', 8: ' ', 9: ' '
}

# Test markBoard()
markBoard(1, 'X')
markBoard(2, 'O')
markBoard(3, 'X')
markBoard(4, 'O')
markBoard(5, 'X')
markBoard(6, 'O')

tc.assertDictEqual(board, testBoard, "markBoard() didn't work as expected")

tc.assertEqual(validateMove('1'), False, "validateMove() didn't work as expected with duplicated input : 1")

# Test checkWin()
tc.assertEqual(checkWin('X'), False, "checkWin() didn't work as expected with input : 'X'")
testBoard[7] = 'X'
markBoard(7, 'X')
tc.assertDictEqual(board, testBoard, "markBoard() didn't work as expected with input (7, 'X')")
tc.assertEqual(checkWin('X'), True, "checkWin() didn't work as expected with input : 'X'")


board = {
    1: 'X', 2: ' ', 3: ' ',
    4: 'O', 5: 'X', 6: ' ',
    7: 'O', 8: ' ', 9: 'X'
}
tc.assertEqual(checkWin('X'), True, "checkWin() didn't work as expected with input : 'X'")
tc.assertEqual(checkWin('O'), False, "checkWin() didn't work as expected with input : 'O'")

board = {
    1: 'O', 2: ' ', 3: ' ',
    4: 'X', 5: 'O', 6: ' ',
    7: 'X', 8: 'X', 9: 'O'
}
tc.assertEqual(checkWin('O'), True, "checkWin() didn't work as expected with input : 'O'")
tc.assertEqual(checkWin('X'), False, "checkWin() didn't work as expected with input : 'X'")

board = {
    1: 'X', 2: 'O', 3: 'O',
    4: 'X', 5: ' ', 6: ' ',
    7: 'X', 8: ' ', 9: ' '
}
tc.assertEqual(checkWin('X'), True, "checkWin() didn't work as expected with input : 'X'")
tc.assertEqual(checkWin('O'), False, "checkWin() didn't work as expected with input : 'O'")

board = {
    1: 'X', 2: 'O', 3: 'X',
    4: 'X', 5: 'O', 6: ' ',
    7: ' ', 8: 'O', 9: ' '
}
tc.assertEqual(checkWin('O'), True, "checkWin() didn't work as expected with input : 'O'")
tc.assertEqual(checkWin('X'), False, "checkWin() didn't work as expected with input : 'X'")

board = {
    1: 'X', 2: 'X', 3: 'X',
    4: 'O', 5: 'O', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}
tc.assertEqual(checkWin('X'), True, "checkWin() didn't work as expected with input : 'X'")
tc.assertEqual(checkWin('O'), False, "checkWin() didn't work as expected with input : 'O'")

board = {
    1: 'X', 2: 'X', 3: ' ',
    4: 'O', 5: 'O', 6: 'O',
    7: 'X', 8: ' ', 9: ' '
}
tc.assertEqual(checkWin('O'), True, "checkWin() didn't work as expected with input : 'O'")
tc.assertEqual(checkWin('X'), False, "checkWin() didn't work as expected with input : 'X'")


# Test checkFull()
tc.assertEqual(checkFull(), False, "checkFull() didn't work as expected")
board = {
    1: 'O', 2: 'X', 3: 'O',
    4: 'O', 5: 'X', 6: 'X',
    7: 'X', 8: 'O', 9: 'X'
}
tc.assertEqual(checkFull(), True, "checkFull() didn't work as expected")

print("All tests passed! Congratulations!")


"""