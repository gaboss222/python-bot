from discord.ext import commands
from discord.client import log
import discord
import random
import asyncio
import logging

"""A bot capable of playing ticTacToe and do many other useless things, enjoy."""

description = """Python bot project by Florian Fasmeyer & Gabriel Mc.Gaben."""
bot = commands.Bot(command_prefix='!', description=description)
failedAttempt = 0
board = [':white_medium_square:'] * 10
playPlayer1 = True

log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())
#logging.basicConfig(level=logging.INFO)

@bot.command(name='bot')
async def _bot():
    """Is the bot cool?"""

    await bot.say('Yes, the bot is cool.')

@bot.command(description='Play a game of TicTacToe with the bot.')
async def play(*miniToe : int):
    """Play a game of TicTacToe with the bot."""
    isPlaying = False
    winner = False
    player1 = ':x:'
    player2 = ':o:'
    playPlayer1 = True
    
    if len(miniToe)==0 and not isPlaying:
        await startGame()
        isPlaying = True
    
    if isPlaying:
        if playPlayer1:
            await bot.say('Joueur 1 : ')
        else:
            await bot.say('Joueur 2: ')
            
    
        
    elif len(miniToe)>0:          
            move = miniToe[0]         
           
                
            if playPlayer1:
                await movePlayer(player1, move)
                if await hasWon(player1):
                    await bot.say("Joueur 1 gagne")
                    winner = True
            elif playPlayer2:
                await movePlayer(player2, move)
                if await hasWon(player2):
                    await bot.say("Joueur 2 gagne")
                    winner = True
                    
            
    playPlayer1 = not playPlayer1
    
    if winner:
        isPlaying = False
        await bot.say("GAGNANT")
        board = [':white_medium_square:'] * 10       
   
 

async def movePlayer(player, move):
    """Place move on the board"""

    if move >= 1 and move <= 9 and (await isSpaceFree(move) == True):
        board[move] = player
        await draw()
        
    else:
        await bot.say('Entrez une position correcte (1-9)')


async def hasWon(player):
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
 

async def isSpaceFree(position):
    """Is the place is free ?"""

    return board[position] == ':white_medium_square:'
  
  
async def draw():
    """Draw the board"""
    await bot.say(board[1] + board[2] +board[3] + '\n' + board[4] + board[5] + board[6] + '\n' + board[7] +board[8] +board[9])
 
async def startGame():
    """Start the game, randomly choose who will be first."""

    await draw()
    await bot.say("Let's play!")
   

bot.run("MzE0NjYwOTMxMTIyNDk1NDg4.C_7aWg.gr69xOwZ54dBhSQ3y7cff89GsxQ")
