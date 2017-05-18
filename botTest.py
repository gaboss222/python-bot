import discord
from discord.ext import commands
import random
import asyncio
import logging

from discord.client import log

description = '''Have fun! :-)'''
bot = commands.Bot(command_prefix='!', description=description)

#log.setLevel(logging.DEBUG)
#log.addHandler(logging.StreamHandler())
#logging.basicConfig(level=logging.INFO)


@bot.event
async def on_ready():
    await bot.say('Hello World!')

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

@bot.command(description='For when you are bored, the bot will play with you.')
async def play():
    """Play a game of TicTacToe with the bot"""
    await bot.say('I still don\'t know how to play this game, wait please.')


bot.run("MzE0NjYwOTMxMTIyNDk1NDg4.C_7aWg.gr69xOwZ54dBhSQ3y7cff89GsxQ")
