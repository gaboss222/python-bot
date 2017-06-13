from discord.ext import commands
from discord.client import log
import discord
import random
import asyncio
import logging

"""A bot capable of playing ticTacToe and do many other useless things, enjoy."""

description = """Python bot project by Florian Fasmeyer & Gabriel Grigri."""
bot = commands.Bot(command_prefix='!', description=description)
failedAttempt = 0
playPlayer1 = True
isPlaying = False
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())
board = 0
playerName = ""
#logging.basicConfig(level=logging.INFO)

   

@bot.command(description='Decide who to play')
async def playWith():
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
    
@bot.command(description='Play a game of tictactoe')   
async def move(*miniToe : int):
    """Play a game of TicTacToe with the bot."""
    global isPlaying
    winner = False
    player1 = ':x:'
    player2 = ':o:'
    global playPlayer1
    
    if isPlaying:
        if len(miniToe)>0:          
                move = miniToe[0]                    
                    
                if playPlayer1:
                    if await movePlayer(player1, move):                
                        if await hasWon(player1):
                            await bot.say("Joueur 1 gagne")
                            winner = True
                        else: 
                            playPlayer1 = False
                            await bot.say('Joueur 2 :')
                    else:
                        playPlayer1 = True
                else:
                    if await movePlayer(player2, move):
                        if await hasWon(player2):
                            await bot.say("Joueur 2 gagne")
                            winner = True
                        else:
                            playPlayer1 = True
                            await bot.say('Joueur 1 :')
                    else:
                        playPlayer1 = False
    else:
        await bot.say("Aucune partie en cours")
    if winner:
        isPlaying = False       
   
 

async def movePlayer(player, move):
    """Place move on the board"""

    if move >= 1 and move <= 9 and (await isSpaceFree(move) == True):
        board[move] = player
        await draw()
        return True
        
    else:
        await bot.say('Entrez une position correcte (1-9)')
        return False


async def hasWon(player):
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
 
async def isSpaceFree(position):
    """Is the place is free ?"""

    return board[position] == ':white_medium_square:'
  
  
async def draw():
    """Draw the board"""
    
    result = ''
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
