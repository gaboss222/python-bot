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
player1Id = '';
player2Id = '';

player1 = ':x:'
player2 = ':o:'

log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())
#logging.basicConfig(level=logging.INFO)

@bot.command(description='Play TicTacToe against another player (default).', pass_context=True)
async def play(ctx, *name2: str):
    """Play TicTacToe against another player."""

    global isPlaying
    global bot
    global player1Name
    global player1Id
    global player2Id
    global playPlayer1
    global player2Name
    player2Name = ''
    messageDisplay = ''

    if not isPlaying : #and len(name)==0:
        messageDisplay += startGame()
        isPlaying = True
        playPlayer1 = True
        player1Name = ctx.message.author.name
        player1Id = ctx.message.author.id
        player2Id = ''
        messageDisplay += '\nÀ <@!'+player1Id+'> de jouer.'

        #ICI --> Récupérer pseudo 2 (passé en paramète)
        if len(name2)>0:
            player2Name = name2[0]
    else:
        messageDisplay += '\nUne partie est en cours.'

    await bot.say(messageDisplay)

@bot.command(description='Play TicTacToe against the PC.',  pass_context=True)
async def playSolo(ctx):
    """Play TicTacToe against the PC."""

    global isPlaying
    global playPlayer1
    global player1Id
    global player1Name
    global playVSPC
    messageDisplay = ''

    if not isPlaying :
        messageDisplay += startGame()
        isPlaying = True
        playPlayer1 = True
        player1Name = ctx.message.author.name
        player1Id = ctx.message.author.id
        playVSPC = True
        messageDisplay += '\nÀ <@!'+player1Id+'> de jouer.'
    else:
        messageDisplay += '\nUne partie est en cours.'
    await bot.say(messageDisplay)

@bot.command(description='Stop the current game.',  pass_context=True)
async def stop(ctx):
    """Stop the current game."""
    global isPlaying
    if isPlaying:
        if ctx.message.author.name == player1Name or ctx.message.author.name == player2Name:
            isPlaying = False
            await bot.say('\nFin de la partie.')
    else:
        await bot.say('\nAucune partie en cours')

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
    global player1Id
    global player2Id
    global playVSPC
    boardFull = False
    messageDisplay = ''

    if isPlaying:
        if not winner:
            if not playVSPC:
                    if len(miniToe)>0 and isValid(miniToe[0]):
                            move = miniToe[0]
                            if playPlayer1:
                                if player1Name == ctx.message.author.name :
                                    if movePlayer(board, player1, move):
                                        messageDisplay += draw()
                                        if hasWon(board, player1):
                                            messageDisplay += '\n<@!'+player1Id+'> a gagné!'
                                            winner = True
                                        else:
                                            if isBoardFull(board):
                                                boardFull = True
                                            else:
                                                playPlayer1 = False
                                                if player2Name != '' :
                                                    if player2Id == '' :
                                                        messageDisplay += '\nÀ '+player2Name+' de jouer.'
                                                    else:
                                                        messageDisplay += '\nÀ <@!'+player2Id+'> de jouer.'
                                                else:
                                                    messageDisplay += '\nAu tour du deuxième joueur.'
                            else:
                                getPlayer2Info(ctx.message.author.name, ctx.message.author.id)
                                if player2Name == ctx.message.author.name :
                                    if player2Id == '':
                                        player2Id = ctx.message.author.id
                                    if movePlayer(board, player2, move):
                                        messageDisplay += draw()
                                        if hasWon(board, player2):
                                            messageDisplay += '\n<@!'+player2Id+'> a gagné!'
                                            winner = True
                                        else:
                                            if isBoardFull(board):
                                                boardFull = True
                                            else:
                                                playPlayer1 = True
                                                messageDisplay += '\nÀ <@!'+player1Id+'> de jouer.'
                    else:
                        messageDisplay += '\nEntrez un nombre de 1 à 9.'
            else:
                if len(miniToe)>0:
                            move = miniToe[0]
                            if movePlayer(board, player1, move):
                                messageDisplay += draw()
                                if hasWon(board, player1):
                                    messageDisplay += '\n<@!'+player1Id+'> a gagné!'
                                    winner = True
                                else:
                                    if isBoardFull(board):
                                        boardFull = True
                                    else:
                                        messageDisplay += '\nLe bot joue...'
                                        moveBot = getMoveBot()
                                        if movePlayer(board, player2, moveBot):
                                            messageDisplay += draw()
                                            if hasWon(board, player2):
                                                messageDisplay += "\nLe bot a gagné!"
                                                winner = True
                                            elif isBoardFull(board):
                                                boardFull = True
                                            else:
                                                messageDisplay += '\nÀ <@!'+player1Id+'> de jouer.'
                else:
                    messageDisplay += '\nEntrez un nombre de 1 à 9.'
    else:
        messageDisplay += "\nAucune partie en cours."

    if winner or boardFull:
        messageDisplay += '\nPartie terminée.'
        isPlaying = False
        playVSPC = False

    if messageDisplay != '':
        await bot.say(messageDisplay)


def getPlayer2Info(name, id):
    """Get info for player 2"""
    global player2Name
    global player2Id
    if player2Name == '':
        player2Name = name
        player2Id = id


def isValid(move):
    """Return true if input within [1;9]."""

    if move >= 1 and move <= 9:
        return True
    else:
        return False


def getMoveBot():
    """Move from the bot."""
    global player2
    #On test le move du bot sur une copy du board
    #Si le moove fait du bot un gagnant, retourne ce move (i)
    #Sinon, test si le player peut gagner au prochain move, et retourne ce dernier pour le contrer
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
    i = random.randint(1, 9)
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
        #    for i in range(3)):

        #any(all(x == player for x in board[i:i+3])
        #    for i in range(0, 9, 3))

        #any(all(x == player for x in board[s])
        #    for s in (slice(0,9,4), slice(2,7,2)))

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
            if b[i] == ':white_medium_square:':
                return False
        return True
        #return not ':white_medium_square:' in b


def isSpaceFree(b, position):
    """Return true if the place you want to place your pawn on is free."""

    return b[position] == ':white_medium_square:'

def draw():
    """Draw the board"""

    result = ''
    for i in range(1, 10):
        if i%3 == 0:
            result +=  board[i] + '\n'
        else:
            result += board[i]

    return '\n\n' + result

def startGame():
    """Start the game, randomly choose who will be first."""

    initBoard()
    return draw()

bot.run("MzE0NjYwOTMxMTIyNDk1NDg4.C_7aWg.gr69xOwZ54dBhSQ3y7cff89GsxQ")
