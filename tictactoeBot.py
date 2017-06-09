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

@bot.command(description='For when you wanna settle the score some other way.')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')

    channel = bot.get_channel(id='314664198971850752')
    await bot.send_file(destination=channel, fp='./assets/dice.png', filename='dice.png')

@bot.command()
async def enought():
    """When you had enought."""

    await bot.say('https://i.ytimg.com/vi/Yx0qSdfvF7Y/maxresdefault.jpg')
    await bot.say('When you had enought! :-(')

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

async def nextMove(player, move):
    """Send the next move to ticTacToe.py."""

    if(t.nextMove(int(line), int(column))):

        await bot.say(t.displayTable())
        stopGame = await win()
        if(not stopGame):
            t.botPlay()
            await bot.say(t.displayTable())
            await win()
    else:
        await bot.say("Sorry, you can not do that!")
        await bot.say(t.displayTable())

async def win():
    """Check if we have a winner. Return True if game end."""

    result = t.winCondition()
    if(result == "X"):

        await bot.say("You win! :-)")
        isPlaying = False
        return True
    elif(result == "O"):

        await bot.say("You lose! :-(")
        isPlaying = False
        return True
    elif(result == "-"):

        await bot.say("Draw!")
        isPlaying = False
        return True
    return False

bot.run("MzE0NjYwOTMxMTIyNDk1NDg4.C_7aWg.gr69xOwZ54dBhSQ3y7cff89GsxQ")
