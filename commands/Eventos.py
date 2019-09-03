import discord
from discord.ext import commands
import asyncio
poll_emojis = {0: ':zero:', 1: ':one:', 2: ':two:', 3: ':three:', 4: ':four:'}

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



        



def setup(bot):
    bot.add_cog(Events(bot))