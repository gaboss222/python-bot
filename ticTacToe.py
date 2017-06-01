import random

arr = [[' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' ']]
gameInProcess = False

def displayTable():
    '''Return a string wich display the table at the current state of the game.'''

    table =( "```   | 1 | 2 | 3 \n"+
                "---|---|---|---\n"+
                " A | {0} | {1} | {2} \n".format(arr[0][0], arr[0][1], arr[0][2])+
                " B | {0} | {1} | {2} \n".format(arr[1][0], arr[1][1], arr[1][2])+
                " C | {0} | {1} | {2} \n```".format(arr[2][0], arr[2][1], arr[2][2]))
    return table

def displayWinner():
    '''Return a string with the final state of the game (win, lose, draw).'''

    return "```Player wins!```"

def start():
    '''Start the game, init empty table.'''

    arr = [[' ', ' ', ' '],
           [' ', ' ', ' '],
           [' ', ' ', ' ']]
    gameInProcess = True


def nextMove(line, column):
    '''Update the table, if it can not (case already used) it returns false, else true.'''


    return True #is okey!

def isGameInProgress():
    '''Return true if game in process. Game end when one win or if we have a draw.'''

    return True
