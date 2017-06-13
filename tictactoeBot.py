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
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())
board = 0
player1 = ':x:'
player2 = ':o:'
#logging.basicConfig(level=logging.INFO)



@bot.command(description='Decide who to play')
async def playWithPlayer():
    """Play with playerName"""
    global isPlaying
    global playPlayer1
    if isPlaying is False : #and len(name)==0:
        await startGame()
        isPlaying = True
        playPlayer1 = True
        await bot.say('Joueur 1 : ')
    else:
        await bot.say('Une partie est en cours')
 
@bot.command(description='Decide who to play')
async def playWithPC():
    """Play with PC"""
    global isPlaying
    global playPlayer1
    global playVSPC
    if isPlaying is False :
        await startGame()
        isPlaying = True
        playPlayer1 = True
        playVSPC = True
        await bot.say('Joueur 1 : ')
    else:
        await bot.say('Une partie est en cours')
 
@bot.command(description='Stop the game')
async def stop():
    """ Stop the current game"""
    global isPlaying
    isPlaying = False

@bot.command(description='Play a game of tictactoe')
async def move(*miniToe : int):
    """Play a game of TicTacToe with the bot."""
    
    global isPlaying
    winner = False
    global player1
    global player2
    global playPlayer1
    global playVSPC
    boardFull = False
    if isPlaying:
        if not winner:
            if not playVSPC:
                    if len(miniToe)>0 and await isValid(miniToe[0]):          
                            move = miniToe[0]                      
                            if playPlayer1:
                                if await movePlayer(board, player1, move):
                                    await draw()
                                    if await hasWon(board, player1):
                                        await bot.say("Joueur 1 gagne")
                                        winner = True
                                    else:
                                        if await isBoardFull(board):
                                            boardFull = True
                                        else:
                                            playPlayer1 = False
                                            await bot.say('Joueur 2 :')
                            else:
                                if await movePlayer(board, player2, move):
                                    await draw()
                                    if await hasWon(board, player2):
                                        await bot.say("Joueur 2 gagne")
                                        winner = True
                                    else:
                                        if await isBoardFull(board):
                                            boardFull = True
                                        else:
                                            playPlayer1 = True
                                            await bot.say('Joueur 1 :')
                    else:
                        await bot.say('Entrez un nombre (1-9)')
            else:
                if len(miniToe)>0:
                            move = miniToe[0]
                            if await movePlayer(board, player1, move):
                                await draw()
                                if await hasWon(board, player1):
                                    await bot.say("Joueur 1 gagne")
                                    winner = True
                                else:
                                    if await isBoardFull(board):
                                        boardFull = True
                                    else:
                                        await bot.say('Au PC :')
                                        moveBot = await getMoveBot()
                                        if await movePlayer(board, player2, moveBot):
                                            await draw()
                                            if await hasWon(board, player2):
                                                await bot.say("PC Gagne")
                                                winner = True
                                            elif await isBoardFull(board):
                                                boardFull = True
                else:
                    await bot.say('Entrez un nombre (1-9)')
    else:
        await bot.say("Aucune partie en cours")     
        
    if winner or boardFull:
        await bot.say('Partie finie')
        isPlaying = False
        playVSPC = False

        
async def isValid(move):
    """Is valid ?"""
    if move >= 1 and move <= 9:
        return True
    else:
        return False
 

async def getMoveBot():
    """Move from the bot"""
    global player2
    #On test le moove du bot sur une copy du board
    #Si le moove fait du bot un gagnant, retourne ce moove (i)
    #Sinon, test si le player peut gagner au prochain moove, et retourne ce dernier pour le contrer
    #Sinon, centre, puis corners, puis random
    #IA reprise du site https://inventwithpython.com/chapter10.html (modifiée en fonction de mon code)
    for i in range(1,10):
        boardCopy = await getBoardCopy(board)
        if await isSpaceFree(boardCopy, i):
            if await movePlayer(boardCopy, player2, i):
                if await hasWon(boardCopy, player2):
                    return i
    for i in range(1, 10):
        boardCopy = await getBoardCopy(board)
        if await isSpaceFree(boardCopy, i):
            if await movePlayer(boardCopy, player1, i):
                if await hasWon(boardCopy, player1):
                    return i

    #Centre
    if await isSpaceFree(board, 5):
        return 5
    #Corners
    for i in range(1,3, 2):
        if await isSpaceFree(board, i):
            return i
    for i in range(7,9,2):
        if await isSpaceFree(board, i):
            return i   
    #Sinon, nombre random
    i = random.randint(1, 10)
    while not await isSpaceFree(boardCopy, i):
        i = i + 1
    return i  
   
    
    
async def getBoardCopy(b):
     # Make a duplicate of the board list and return it the duplicate.
     boardCopy = []

     for i in b:
         boardCopy.append(i)

     return boardCopy
 

async def movePlayer(b, player, move):
    """Place move on the board"""

    if await isValid(move) and (await isSpaceFree(b, move)):
        b[move] = player
        return True

    else:
        return False


async def hasWon(board, player):
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

          

async def initBoard():
    """Initialize the board"""

    global board
    board = [':white_medium_square:'] * 10

    
async def isBoardFull(b):
        """Return true if the board is full"""
        for i in range(1, 10):
            if await isSpaceFree(b, i):
                return False
        return True     
        
async def isSpaceFree(b, position):
    """Is the place is free ?"""

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

    await initBoard()
    await draw()
    await bot.say("Let's play!")


bot.run("MzE0NjYwOTMxMTIyNDk1NDg4.C_7aWg.gr69xOwZ54dBhSQ3y7cff89GsxQ")
