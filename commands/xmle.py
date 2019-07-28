import discord
from discord.ext import commands
import os
from urllib import parse, request
from random import randint
import re
from xml.dom import minidom

class comando(commands.Cog):
	
	def __init__(self, bot):
		self.bot=bot


	@commands.command()
	async def r34(self,ctx,*,lurk):  
		busca = parse.urlencode({"":lurk})
		pagina = request.urlopen("https://rule34.xxx/index.php?page=dapi&s=post&q=index&limit=100&pid=0&tags"+busca)
		resultado = re.findall(r"\<(.*?)\>", pagina.read().decode())
		largo=len(resultado)
		largo=largo-2
		print(largo)
		aux=resultado[randint(2,largo)]
		aux=re.findall(r"\"(.*?)\"",aux)
		embed=discord.Embed(title="[Click pa ve donde]", url="https://rule34.xxx/index.php?page=post&s=view&id=".format(aux[10]), description="deberia hacer algo mejor con mi vida", color=0xe90309)
		embed.set_author(name="el beta", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTvrFytZTMQnW6cD-85691yjeNYHetZ3aXe1Ts3sYzLzptQXXx")
		embed.set_thumbnail(url="https://i.pinimg.com/originals/d9/51/bb/d951bbee810ba54ba379ec286a57a073.png")
		embed.set_footer(text="im gonna say the n word")
		embed.set_image(url=aux[2])
		embed.add_field(name="la tag es: " +lurk, value="nada" ,inline=True)
		await ctx.send(embed=embed)


#Codigos de error	                
"""
	async def cog_command_error(self,ctx,error):
	 	if isinstance(error,commands.MissingRequiredArgument):
	 		await ctx.send("manda la vaina bien pedazo de gay")
	 	elif isinstance(error,commands.CommandInvokeError):
	 		await ctx.send("Esa tag no existe mariguanero ve las tags bien")
"""

def setup(bot):
	bot.add_cog(comando(bot))