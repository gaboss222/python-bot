from discord.ext import commands
from discord.client import log
import discord
import random
import asyncio
import logging
import tictactoe2 as t

"""A bot capable of playing ticTacToe and do many other useless things, enjoy."""

description = """Python bot project by Florian Fasmeyer & Gabriel Mc.Gaben."""
bot = commands.Bot(command_prefix='!', description=description)
failedAttempt = 0
isPlaying = False #set to default False
board = t.draw()

log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())
#logging.basicConfig(level=logging.INFO)

@bot.command(name='bot')
async def _bot():
    """Is the bot cool?"""

    await bot.say('Yes, the bot is cool.')

@bot.command(description='Play a game of TicTacToe with the bot.')
async def play(*miniToe : str):
    """Play a game of TicTacToe with the bot."""

    isPlaying = False
    winner = False
    playPlayer1 = True

    player1 = 'X'
    player2 = 'O'

    if len(miniToe)>0:
        move = miniToe
    else:
        await startGame()

    if isPlaying == False:   
        isPlaying = not isPlaying
        
    if playPlayer1:

        await bot.say('Joueur 1 : ')
    else:

        await bot.say('Joueur 2 : ')
        
    if isValid(move):
        if playPlayer1:
            movePlayer(player1, move)
            if t.hasWon(player1):
                await bot.say("Joueur 1 gagne")
                winner = True
        else:
            movePlayer(player1, move)
            if t.hasWon(player2):
                await bot.say("Joueur 2 gagne")
                winner = True
      
    if winner:
        await bot.say("GAGNANT")
        
    playPlayer1 = not playPlayer1
   

async def movePlayer(player, move):
    """Place move on the board"""
    board[move] = player
    pass
   
async def isValid(move):
    """Move valid"""
    
    if move >= 1 and move <= 9 and t.isSpaceFree(move):
        return True
    else:      
        await bot.say("Move incorrect")
        return False
    move = miniToe

    if isPlaying == False:

    	await startGame()

    	isPlaying = not isPlaying
    while not winner :
    	if playPlayer1:

    		await bot.say('Joueur 1 : ')
    	else:

    		await bot.say('Joueur 2 : ')


async def startGame():
    """Start the game, randomly choose who will be first."""

    await bot.say("Let's play!")
    await bot.say(t.draw())

bot.run("MzE0NjYwOTMxMTIyNDk1NDg4.C_7aWg.gr69xOwZ54dBhSQ3y7cff89GsxQ")
