import random

turnCounter = 0
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

    global arr
    arr = [[' ', ' ', ' '],
           [' ', ' ', ' '],
           [' ', ' ', ' ']]


def nextMove(line, column):
    '''Update the table, if it can not (case already used) it returns false, else true.'''

    if(arr[line][column] != "X" and arr[line][column] != "O"):

        arr[line][column] = "X"
        turnCounter+=1
        return True
    else:
        return False

def winCondition():
    '''Return " " if no winner, return X or O if one wins.'''

    #Line check
    for i in range(3):
        gameEnd = True
        temp = arr[i][0]
        if(temp != " "):
            for j in range(1,3):
                if(arr[i][j] != temp):
                    gameEnd = False
                    break
            if(gameEnd):
                return temp

    #column check
    for  i in range(3):
        gameEnd = True
        temp = arr[0][i]
        if(temp != " "):
            for j in range(1,3):
                if(arr[j][i] != temp):
                    gameEnd = False
                    break
            if(gameEnd):
                return temp
    #diagonals
    temp = arr[0][0]
    if(temp != " "):
        if(temp == arr[1][1] and temp == arr[2][2]):
            return temp

    temp = arr[0][2]
    if(temp != " "):
        if(temp == arr[1][1] and temp == arr[2][0]):
            return temp
    #filled
    if(turnCounter == 9):
        return "-"

    return " "
