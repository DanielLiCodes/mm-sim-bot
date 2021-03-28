import discord
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from discord.ext.commands.cooldowns import BucketType
from discord.ext.commands.errors import CommandInvokeError
import collections
import re
import datetime
import aiohttp
import asyncio



class Member_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.can_claim = True
        self.WISH_LIST = ['keycult', 'chimera65', 'ori', 'kyuu', 'satisfaction', 'iron165', 'iron180', 'singa', 'tgr']

    

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id != 824151343173337108:
            return
        
        if self.can_claim:
            if message.embeds != None:
                for x in message.embeds:
                    print(x.description.lower())
                    print(x.title.lower())
                    print(x.fields)
                    if 'keyboard' in str(x.description.lower()) and 'Number' in str(x.fields):
                        await asyncio.sleep(1.7)
                        await message.add_reaction('👍') 
                        print(f'TRIED TO SNAG {x.title}')
                        self.can_claim = False
                        await asyncio.sleep(3650)
                        self.can_claim = True
                    elif 'gmk' in str(x.title.lower()) and 'Number' in str(x.fields):
                        await asyncio.sleep(1.7)
                        await message.add_reaction('👍') 
                        print(f'TRIED TO SNAG {x.title}')
                        self.can_claim = False
                        await asyncio.sleep(3650)
                        self.can_claim = True
        if message.embeds != None:
            for x in message.embeds:
                if any(x.title.split(' ')[0].lower() in s for s in self.WISH_LIST) and 'Number' in str(x.fields):
                    if 'sa' == x.tittle.split(' ')[0].lower():
                        return
                    await asyncio.sleep(1.7)
                    await message.add_reaction('👍')
                    print(f'TRIED TO SNAG {x.title}')

    @commands.command(name = 'canClaim')
    async def canClaim(self, ctx):
        """check status"""
        await ctx.send(self.can_claim)


    @commands.command(name = 'start')
    async def start(self, ctx):
        """start the opperation"""
        if ctx.author.id != 335892125159784450 and ctx.author.id != 262294923607277569:
            return await ctx.send("you aren't me! :middle_finger:")
        print('in')
        await ctx.send('%chance')
        await asyncio.sleep(5)
        counter = 0
        while self.can_claim and counter < 5:
            await ctx.send('%r')
            await asyncio.sleep(5)
            counter+=1
        while True:
            now = datetime.datetime.utcnow()
            time_for_thing_to_happen = now + datetime.timedelta(minutes=61)
            await discord.utils.sleep_until(time_for_thing_to_happen)
            await ctx.send('%chance')
            await asyncio.sleep(5)
            counter = 0
            while self.can_claim and counter < 5:
                await ctx.send('%r')
                await asyncio.sleep(5)
                counter+=1

def setup(bot):
    print('loaded')
    bot.add_cog(Member_Commands(bot))