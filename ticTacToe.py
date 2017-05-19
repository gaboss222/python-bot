import random

def displayTable():
    '''Return a string wich display the table at the current state of the game.'''

    table =( "```   | 1 | 2 | 3 \n"+
                "---|---|---|---\n"+
                " A |   |   |   \n"+
                " B |   |   |   \n"+
                " C |   |   |   \n```")
    return table

def displayWinner():
    '''Return a string with the final state of the game (win, lose, draw).'''

    return "```Player wins!```"

def nextMove(line, column):
    '''Update the table, if it can not (case already used) it returns false, else true.'''

    return True #is okey!

def isGameInProgress():
    '''Return true if game in process. Game end when one win or if we have a draw'''

    return True
