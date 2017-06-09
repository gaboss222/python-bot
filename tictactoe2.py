
board = [' '] * 10

winner = False
playPlayer1 = True

def draw() :
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def isSpaceFree(position):
    return board[position] == ' '


def movePlayer(player, move):
    if move >= 1 and move <= 9 and isSpaceFree(move):
        board[move] = player
    else:
        print("Entrez une position correcte")

def win_condition(player):
        '''Def the win condition'''

        for i in range(1,4):            
            #vérification des colonnes
            if(board[i] == board[(i+3)] and board[i] == board[(i+6)] == player):
                return True

            #vérification des lignes
        for i in range(1,8,3):
            if(board[i] == board[(i+1)] and board[i] == board[(i+2)] == player):
                return True
            

        #vérification des diagonales
        if(board[1] == board[5] == player and board[5] == board[9] or
           board[3] == board[5] == player and board[5] == board[7]):
            return True
        

while not winner :
    draw()

    player1 = 'X'
    player2 = 'O'
    if playPlayer1 :
        print( "Joueur 1 : ")
    else :
        print( "Joueur 2 : ")

    try:
        move = int(input(">> "))
    except:
        print("Entrez un nombre correct")
        continue
    if playPlayer1:
        movePlayer(player1, move)
        if win_condition(player1):
            print("Joueur 1 a gagné")
            winner = True
            draw()
    else:
        movePlayer(player2, move)
        if win_condition(player2):
            print("Joueur 2 a gagné")
            winner = True
            draw()
                  
    playPlayer1 = not playPlayer1
