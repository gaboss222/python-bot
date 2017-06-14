from discord.ext import commands
from discord.client import log
import discord
import random
import asyncio
import logging

"""A bot capable of playing ticTacToe and do many other useless things, enjoy."""

description = """Python bot project by Florian Fasmeyer & Gabriel Grigri."""
bot = commands.Bot(command_prefix='!', description=description)

playPlayer1 = False
isPlaying = False
playVSPC = False

board = 0
player1Name = '';
player2Name = '';

player1 = ':x:'
player2 = ':o:'

log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())
#logging.basicConfig(level=logging.INFO)

@bot.command(description='Play TicTacToe against another player (default).', pass_context=True)
async def play(ctx, name2: str, *name2bis: str):
    """Play TicTacToe against another player."""

    global isPlaying
    global bot
    global player1Name
    global playPlayer1
    global player2Name

    if not isPlaying : #and len(name)==0:
        await startGame()
        isPlaying = True
        playPlayer1 = True
        player1Name = ctx.message.author.name
        #ICI --> Récupérer pseudo 2 (passé en paramète)
        if len(name2bis)>0:
            player2Name = name2 + name2bis
        else:
            player2Name = name2
        await bot.say('À '+player1Name+' de jouer.')
    else:
        await bot.say('Une partie est en cours.')

@bot.command(description='Play TicTacToe against the PC.',  pass_context=True)
async def playSolo(ctx):
    """Play TicTacToe against the PC."""

    global isPlaying
    global playPlayer1
    global player1Name
    global playVSPC
    if not isPlaying :
        await startGame()
        isPlaying = True
        playPlayer1 = True
        player2Name = ''
        player1Name = ctx.message.author.name
        playVSPC = True
        await bot.say('À '+player1Name+' de jouer.')
    else:
        await bot.say('Une partie est en cours.')

@bot.command(description='Stop the current game.')
async def stop():
    """Stop the current game."""
    global isPlaying
    isPlaying = False
    await bot.say('Fin de la partie.')

@bot.command(pass_context=True, description='Make a move on the TicTacToe board (after starting a game).')
async def move(ctx, *miniToe : int):
    """Make a move on the TicTacToe board (after starting a game)."""

    global isPlaying
    winner = False
    global player1
    global player2
    global playPlayer1
    global player1Name
    global player2Name
    global playVSPC
    boardFull = False

    if isPlaying:
        if not winner:
            if not playVSPC:
                    if len(miniToe)>0 and isValid(miniToe[0]):
                            move = miniToe[0]

                            if playPlayer1:
                                if player1Name == ctx.message.author.name :
                                    if movePlayer(board, player1, move):
                                        await draw()
                                        if hasWon(board, player1):
                                            await bot.say(player1Name+' a gagné!')
                                            winner = True
                                        else:
                                            if isBoardFull(board):
                                                boardFull = True
                                            else:
                                                playPlayer1 = False
                                                if player2Name != '' :
                                                    await bot.say('À '+player2Name+' de jouer.')
                                                else:
                                                    await bot.say('Au tour du deuxième joueur.')
                            else:
                            #Si le pseudo 2 = autheur du message, et auteur du msg != player1, alors player 2 joue 
                                if player2Name == ctx.message.author.name and ctx.message.author.name != player1Name :
                                    if movePlayer(board, player2, move):
                                        await draw()
                                        if hasWon(board, player2):
                                            await bot.say(player2Name+' a gagné!')
                                            winner = True
                                        else:
                                            if isBoardFull(board):
                                                boardFull = True
                                            else:
                                                playPlayer1 = True
                                                await bot.say('À '+player1Name+' de jouer.')
                                else:
                                    await bot.say('YOU SHALL NOT PASS')
                    else:
                        await bot.say('Entrez un nombre de 1 à 9.')
            else:
                if len(miniToe)>0:
                            move = miniToe[0]
                            if movePlayer(board, player1, move):
                                await draw()
                                if hasWon(board, player1):
                                    await bot.say(player1Name+' a gagné!')
                                    winner = True
                                else:
                                    if isBoardFull(board):
                                        boardFull = True
                                    else:
                                        await bot.say('À PC de jouer.')
                                        moveBot = await getMoveBot()
                                        if movePlayer(board, player2, moveBot):
                                            await draw()
                                            if hasWon(board, player2):
                                                await bot.say("PC a gagné!")
                                                winner = True
                                            elif isBoardFull(board):
                                                boardFull = True
                else:
                    await bot.say('Entrez un nombre de 1 à 9.')
    else:
        await bot.say("Aucune partie en cours.")

    if winner or boardFull:
        isPlaying = False
        playVSPC = False

def isValid(move):
    """Return true if input within [1;9]."""

    if move >= 1 and move <= 9:
        return True
    else:
        return False


async def getMoveBot():
    """Move from the bot."""
    global player2
    #On test le move du bot sur une copy du board
    #Si le moove fait du bot un gagnant, retourne ce moove (i)
    #Sinon, test si le player peut gagner au prochain moove, et retourne ce dernier pour le contrer
    #Sinon, centre, puis corners, puis random
    #IA reprise du site https://inventwithpython.com/chapter10.html (modifiée en fonction de mon code)
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            if movePlayer(boardCopy, player2, i):
                if hasWon(boardCopy, player2):
                    return i
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            if movePlayer(boardCopy, player1, i):
                if hasWon(boardCopy, player1):
                    return i

    #Centre
    if isSpaceFree(board, 5):
        return 5
    #Corners
    for i in range(1,3, 2):
        if isSpaceFree(board, i):
            return i
    for i in range(7,9,2):

        if isSpaceFree(board, i):
            return i

    #Sinon, nombre random
    i = random.randint(1, 10)
    while not isSpaceFree(boardCopy, i):
        i = i + 1

    return i



def getBoardCopy(b):

     # Make a duplicate of the board list and return it the duplicate.
     boardCopy = []

     for i in b:
         boardCopy.append(i)

     return boardCopy

def movePlayer(b, player, move):
    """Place move on the board."""

    if isValid(move) and (isSpaceFree(b, move)):
        b[move] = player
        return True

    else:
        return False


def hasWon(board, player):
        '''Def the win condition'''


        #any(all(x == player for x in board[i::3])
        #    for i in range(3))

        #any(all(x == player for x in board[i:i+3])
        #    for i in range(0, 9, 3))

        #any(all(x == player for x in board[s])
        #    for s in (slice(0,9,4), slice(2,7,2))

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



def initBoard():
    """Initialize the board"""

    global board
    board = [':white_medium_square:'] * 10

def isBoardFull(b):
        """Return true if the board is full."""
        for i in range(1, 10):
            return False
        return True
        #return ':white_medium_square:' in b

        
def isSpaceFree(b, position):
    """Return true if the place you want to place your pawn on is free."""

    return b[position] == ':white_medium_square:'

async def draw():
    """Draw the board"""

    result = '\n'
    for i in range(1, 10):
        if i%3 == 0:
            result +=  board[i] + '\n'
        else:
            result += board[i]

    await bot.say('\n' + result)
    #await bot.say('\n' + board[1] + board[2] +board[3] + '\n' + board[4] + board[5] + board[6] + '\n' + board[7] +board[8] +board[9])

async def startGame():
    """Start the game, randomly choose who will be first."""

    initBoard()
    await draw()

bot.run("MzE0NjYwOTMxMTIyNDk1NDg4.C_7aWg.gr69xOwZ54dBhSQ3y7cff89GsxQ")
