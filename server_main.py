import discord
from discord.ext import commands
import datetime
import os
from urllib import parse, request
import re
import json
import aiohttp
import aiofiles

bot = commands.Bot(command_prefix='=', description="El autismo evoluciona")
bot.remove_command("help")
for filename in os.listdir("./commands"):
    if filename.endswith(".py"):
        bot.load_extension(f"commands.{filename[:-3]}")


def theboss(ctx):
    return ctx.author.id==186538096580493312

@bot.command()
@commands.check(theboss)
async def matrix(ctx,extension):
    bot.unload_extension(f"commands.{extension}")
    bot.load_extension(f"commands.{extension}")
    await ctx.send("se recargo el modulo: "+ extension)

@bot.command()
@commands.check(theboss)
async def Matar(ctx,extension):
    bot.unload_extension(f"commands.{extension}")
    await ctx.send("Jodete alvaro: "+ extension)
    
@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    print(search_results)
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

@bot.command()
@commands.check(theboss)
async def limpia(ctx,numerin:int):
    await ctx.channel.purge(limit=numerin)

#eventos random AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="el de abajo es gay | =help", url="https://www.twitch.tv/infinitegachi?utm_source=SteamDB"))
    print("Mi body esta ready")

@bot.listen()
async def on_message(message):
       
    if "maldita sea conqui" in message.content.lower():
        await message.channel.send( "No <@142810852406460416> , El comunismo no funciona")
        await bot.process_commands(message)

    if "wololo" in message.content.lower():
        await message.channel.send("aeyoyo")
        await bot.process_commands(message)
        
    if "kevin" in message.content.lower():
        await message.channel.send("GodSpammer")
        await bot.process_commands(message)
    if "navidad" in message.content.lower():
        embed=discord.Embed(color=0x0397D5)
        embed.set_footer(text=" ﺟﻬﺎﺩ ")
        embed.set_image(url="https://i.imgur.com/ZC2sWcT.png")
        await message.channel.send(embed=embed)        
        await bot.process_commands(message)

    if "facista" in message.content.lower():
        embed=discord.Embed(color=0x0397D5)
        embed.set_footer(text="übermensch")
        embed.set_image(url="https://i.imgur.com/h9wfpHa.jpg")
        await message.channel.send(embed=embed)        
        await bot.process_commands(message)

    if "kazuma es homosexual" in message.content.lower():
        await message.channel.send("ese pana es alto gay")
        await bot.process_commands(message) 

    if "kazuma es furro" in message.content.lower():
        await message.channel.send("Es alto furro gay")
        await bot.process_commands(message)
        
bot.run(os.environ["tokkend"])


