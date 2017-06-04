from discord.ext import commands
from discord.client import log
import discord
import random
import asyncio
import logging
import ticTacToe as t

"""A bot capable of playing ticTacToe and do many other useless things, enjoy."""

description = """Python bot project by Florian Fasmeyer & Gabriel Mc.Gaben."""
bot = commands.Bot(command_prefix='!', description=description)
failedAttempt = 0
isPlaying = False #set to default False

log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())
#logging.basicConfig(level=logging.INFO)

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""

    await bot.say(left + right)

@bot.command()
async def sub(left : int, right : int):
    """Subs one nuber to another."""

    await bot.say(left - right)

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

    temp = miniToe
    global failedAttempt
    global isPlaying
    if(len(temp)>0):

        temp = temp[0]
    if(not isPlaying):

        await startGame()
        isPlaying = True
    elif(len(temp)==2 and temp[0] in {"a","b","c"} and temp[1] in {"1","2","3"}):

        dict = {'a': '0', 'b': '1', 'c': '2'}
        failedAttempt = 0
        line = dict[temp[0]]
        column = str(int(temp[1])-1)
        await nextMove(line, column)
    else:

        if(failedAttempt>0):

            await bot.say("Input a position (line, column).\n"+
                          "From [1-3] and [A-B].\n"
                          "Example: \"a1\"")
        else:

            await bot.say("What's your move? [line, column]")
            failedAttempt+=1

async def startGame():
    """Start the game, randomly choose who will be first."""

    t.start()
    await bot.say("Let's play!")
    await bot.say(t.displayTable())

async def nextMove(line, column):
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

    global isPlaying
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
