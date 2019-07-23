import discord
from discord.ext import commands
import json
from urllib import parse, request
import aiohttp
import requests
from random import randint
import os
vainita=["Epa no busques vaina de koishi","cuidado lo que buscas lince","aqui esta tu contenido","ya llego lo delicioso !!!","cuidado cuando te tocas la marmota","pendiente de ese ganzo","pilas y esnucas  al ganzo","mira mira se te va a morir la nutria"]
class comando(commands.Cog):
	
	def __init__(self, bot):
		self.bot=bot


	@commands.command()
	async def dolla(self,ctx):    
	    culo=ctx.message.content.replace("=dolla","")
	    response = requests.get("http://s3.amazonaws.com/dolartoday/data.json")
	    todos = json.loads(response.text)
	    if culo != "":
	                 embed=discord.Embed(title="El valor del US DOLLAH", description="La cantidad de {} dolares es :".format(culo), color=0xec3c00)
	                 embed.set_author(name="En dolar toddy", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTvrFytZTMQnW6cD-85691yjeNYHetZ3aXe1Ts3sYzLzptQXXx")
	                 embed.add_field(name=str(float(todos["USD"]['dolartoday'])*float(culo)), value="99999999shekels/seg", inline=True)
	                 embed.set_thumbnail(url="https://i2.kym-cdn.com/photos/images/original/000/561/330/010.jpg")
	                 await ctx.send(embed=embed)


	    else:
	          embed=discord.Embed(title="El valor del US DOLLAH", description="La cantidad de (1) unidad de DOLLAH es :".format(culo), color=0xec3c00)
	          embed.set_author(name="En dolar toddy", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTvrFytZTMQnW6cD-85691yjeNYHetZ3aXe1Ts3sYzLzptQXXx")
	          embed.add_field(name=str(float(todos["USD"]['dolartoday'])), value="99999999shekels/seg", inline=True)
	          embed.set_thumbnail(url="https://i2.kym-cdn.com/photos/images/original/000/561/330/010.jpg")
	          await ctx.send(embed=embed)

	@commands.command()
	async def duro(self,ctx):    
	    culo=ctx.message.content.replace("=duro","")
	    response = requests.get("http://s3.amazonaws.com/dolartoday/data.json")
	    todos = json.loads(response.text)
	    if culo != "":
	                 embed=discord.Embed(title="El valor del EURO DURO", description="La cantidad de {} euros es :".format(culo), color=0xec3c00)
	                 embed.set_author(name="En dolar toddy", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTvrFytZTMQnW6cD-85691yjeNYHetZ3aXe1Ts3sYzLzptQXXx")
	                 embed.add_field(name=str(float(todos["EUR"]['dolartoday'])*float(culo)), value="99999999shekels/seg", inline=True)
	                 embed.set_thumbnail(url="https://memearchive.files.wordpress.com/2016/10/cb_64x9usaepnu4.png")
	                 await ctx.send(embed=embed)

	    else:
	         embed=discord.Embed(title="El valor del EURO DURO", description="La cantidad de (1) unidad de duro es: ", color=0xec3c00)
	         embed.set_author(name="En dolar toddy", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTvrFytZTMQnW6cD-85691yjeNYHetZ3aXe1Ts3sYzLzptQXXx")
	         embed.add_field(name=str(todos["EUR"]['dolartoday']), value="99999999shekels/seg", inline=True)
	         embed.set_thumbnail(url="https://memearchive.files.wordpress.com/2016/10/cb_64x9usaepnu4.png")
	         await ctx.send(embed=embed)

	@commands.command()
	async def g(self,ctx,*,lurk):
	    query_string = parse.urlencode({"": lurk})
	    async with aiohttp.ClientSession() as session:
	    	async with session.get("https://gelbooru.com/index.php?page=dapi&s=post&q=index&limit=100&pid=0&tags{}&json=1&api_key={}".format(query_string,os.environ["apigel"])) as r:
	    		if r.status == 200:
	    			js = await r.json()
	    			ran=randint(0,50)
	    			embed=discord.Embed(title="[Click pa ve donde]", url="https://gelbooru.com/index.php?page=post&s=view&id={}".format(js[ran]["id"]), description=js[ran]["owner"], color=0xe90309)
	    			embed.set_author(name="La fotico mi pana", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTvrFytZTMQnW6cD-85691yjeNYHetZ3aXe1Ts3sYzLzptQXXx")
	    			embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1118350008003301381/3gG6lQMl.png")
	    			embed.set_footer(text=vainita[randint(0,7)])
	    			embed.set_image(url=js[ran]["file_url"])
	    			embed.add_field(name="La tag es " +query_string, value="numero e imagen {}".format(ran), inline=True)
	    			await ctx.send(embed=embed)	                	


	@commands.command()
	async def nhentai(self,ctx,*,busca):
	    cant= randint(0,24)
	    query_string = parse.urlencode({"": busca})
	    async with aiohttp.ClientSession() as session:
	        async with session.get("https://nhentai.net/api/galleries/search?query"+query_string) as r:
	            if r.status == 200:
	                js = await r.json()
	                print(js["result"][0]["id"])
	                embed=discord.Embed(title="[Click pa ve donde]", url="https://nhentai.net/g/{}/".format(js["result"][cant]["id"]), description=js["result"][cant]["title"]["english"], color=0xe90309)
	                embed.set_author(name="El dounjinshi mi pana", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTvrFytZTMQnW6cD-85691yjeNYHetZ3aXe1Ts3sYzLzptQXXx")
	                embed.set_thumbnail(url="https://i.imgur.com/TrDF6Ct.jpg")
	                embed.set_footer(text="sorry bro cant into loli cristian server")
	                embed.set_image(url="https://i.nhentai.net/galleries/{}/1.jpg".format(js["result"][cant]["media_id"]))
	                embed.add_field(name="la tag es " +busca, value="numero e dounjinshi {}".format(cant), inline=True)
	                await ctx.send(embed=embed)	                	









#Codigos de error	                

	async def cog_command_error(self,ctx,error):
	 	if isinstance(error,commands.MissingRequiredArgument):
	 		await ctx.send("manda la vaina bien pedazo de gay")
	 	elif isinstance(error,commands.CommandInvokeError):
	 		await ctx.send("Esa tag no existe mariguanero ve las tags bien")


def setup(bot):
	bot.add_cog(comando(bot))