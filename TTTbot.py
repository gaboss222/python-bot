import discord
from discord.ext import commands
import random
import asyncio
import logging
import string

from discord.client import log

description = """Python bot project by Florian Fasmeyer & Gabriel Mc.Gaben."""
bot = commands.Bot(command_prefix='!', description=description)
failedAttempt = 0

log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())
#logging.basicConfig(level=logging.INFO)

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command(description='For when you wanna settle the score some other way.')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')

@bot.command()
async def enought():
    """When you had enought!"""
    await bot.say('https://i.ytimg.com/vi/Yx0qSdfvF7Y/maxresdefault.jpg')
    await bot.say('When you had enought! :-(')

@bot.command(description='For when you are bored, the bot will play with you.')
async def play(miniToe : str):
    """Play a game of TicTacToe with the bot."""
    #This funcion manage the in/out of the game

    temp = miniToe
    global failedAttempt

    if(len(temp)==2 and temp[0] in {"a","b","c"} and temp[1] in {"1","2","3"}):

        await bot.say("You played "+ temp[0] + temp[1] +".")
        failedAttempt = 0

        #Use thoses variables to encode the game! :-)
        line = temp[0]
        column = int(temp[1])
    else:

        if(failedAttempt>0):

            await bot.say("Input a position [line, column].\n"+
                          "Example: \"a1\"")
        else:

            await bot.say("What's your move? [line, column]")
            failedAttempt+=1

async def gameFunction(line, column):
    """Hold all variables and call functions from ticTacToe.py."""
    pass

bot.run("MzE0NjYwOTMxMTIyNDk1NDg4.C_7aWg.gr69xOwZ54dBhSQ3y7cff89GsxQ")
