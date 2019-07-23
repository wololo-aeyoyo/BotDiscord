import discord
from discord.ext import commands

class comando(commands.Cog):
	
	def __init__(self, bot):
		self.bot=bot

	@commands.command()
	async def help(self,ctx):

		embed=discord.Embed(title="Vrooooooom", description="El suicidio es una opcion", color=0x0b00d7)
		embed.set_author(name="HowDoYouTurnThisOn? Bot (El autismo evoluciona) v.0.1", icon_url="https://i.kym-cdn.com/entries/icons/facebook/000/020/043/cobra.jpg")
		embed.set_footer(text = "creado por: tu pana Wololo#2078", icon_url = "https://cdn.discordapp.com/avatars/186538096580493312/c1995c58657e24f82a173f682d7abfdd.webp?size=1024")		
		await ctx.send(embed=embed)
		await ctx.send("```El autismo evoluciona:\n bola <pregunta>\n dado <nd> <cantidad de dados>\n dolla <cantidad trumpcoin> \n duro <cantidad de duros>\n g <tag de gelbooru>\n nhentai <busqueda>\n twitter <tweet> (adjunta imagen) \n info ```")



#Codigos de error

	async def cog_command_error(self,ctx,error):
	 	if isinstance(error,commands.MissingRequiredArgument):
	 		await ctx.send("manda la vaina bien gay ve help")
def setup(bot):
	bot.add_cog(comando(bot))