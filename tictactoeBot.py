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

log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())
#logging.basicConfig(level=logging.INFO)

@bot.command(description='For when you are bored, the bot will play with you.')
async def play(*miniToe : str):
    """Play a game of TicTacToe with the bot."""

    isPlaying = False
    winner = False
    playPlayer1 = True

    player1 = 'X'
    player2 = 'O'

    move = miniToe

    if isPlaying == False:

    	await startGame()

    	isPlaying = not isPlaying
    while not winner :
    	if playPlayer1:

    		await bot.say('Joueur 1 : ')
    	else:

    		await bot.say('Joueur 2 : ')

    		try:
    			if move >= 1 and move <= 9 and t.isSpaceFree(move):
    				if playPlayer1:
    					t.movePlayer(player1, move)
    					if t.win_condition(player1):
    						await bot.say('Joueur 1 a gagné !')
    						winner = True
    				else:
    					t.movePlayer(player2, move)
    					if t.win_condition(player2):
    						await bot.say('Joueur 2 a gagné !')
    						winner = True
    			else:
    				await bot.say('Entrez une position correcte')


async def startGame():
    """Start the game, randomly choose who will be first."""

    t.draw()
    await bot.say("Let's play!")


bot.run("MzE0NjYwOTMxMTIyNDk1NDg4.C_7aWg.gr69xOwZ54dBhSQ3y7cff89GsxQ")
