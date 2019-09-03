import discord
from discord.ext import commands

class comando(commands.Cog):
	
	def __init__(self, bot):
		self.bot=bot

	@commands.command()
	async def help(self,ctx):
		embed=discord.Embed(title="Vrooooooom", description="El suicidio es una opcion **reloaded**", color=0x0b00d7)
		embed.set_author(name="trebuchet Bot (El autismo muta) v.0.2", icon_url="https://vignette.wikia.nocookie.net/ageofempires/images/b/b2/Trebunpacket.png/revision/latest?cb=20160310093526")
		embed.set_footer(text = "creado por: tu pana Wololo#2078", icon_url = "https://i.imgur.com/oGXEVkl.jpg")		
		await ctx.send(embed=embed)
		await ctx.send("```El autismo muta:\n bola <pregunta>\n dado <nd> <cantidad de dados>\n dolla <cantidad trumpcoin> \n duro <cantidad de duros>\n g <tag de gelbooru>\n nhentai <busqueda>\n twitter <tweet> \n info ```")



#Codigos de error

	async def cog_command_error(self,ctx,error):
	 	if isinstance(error,commands.MissingRequiredArgument):
	 		await ctx.send("manda la vaina bien gay ve help")
	 	elif isinstance(error,commands.CommandInvokeError):
	 		pass
def setup(bot):
	bot.add_cog(comando(bot))