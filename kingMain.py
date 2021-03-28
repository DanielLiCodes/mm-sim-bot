import discord
from discord.ext import commands
import random
from random import randint
import asyncio
import sys
import traceback
import requests
import aiohttp
import os
import shelve
import math
import datetime
from discord.ext.commands.cooldowns import BucketType
from discord.ext import tasks, commands


def get_prefix(bot, message):
    """Get the prefixes for the bot"""

    prefixes = ['p'] #change this to whatever you want
    if not message.guild:
        return 'p'
    return commands.when_mentioned_or(*prefixes)(bot, message)


initial_extensions = ['cogs.members']

bot = commands.Bot(command_prefix=get_prefix, description='insert desc here', self_bot=True)

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


@bot.event
async def on_ready():
    """does on ready"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print("in B)")

bot.run('enter user token here', bot=False)
