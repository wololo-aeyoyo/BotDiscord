import discord
from discord.ext import commands
from random import randint
import time

idloco="wololo#2078"
lista=[" En mi opinión, sí","Es cierto,","Es decididamente así"," Probablemente","Buen pronóstico","Todo apunta a que sí"," Sin duda","Sí","Sí - definitivamente","Debes confiar en ello","Respuesta vaga, vuelve a intentarlo","Pregunta en otro momento","Será mejor que no te lo diga ahora","No puedo predecirlo ahora","Concéntrate y vuelve a preguntar","No cuentes con ello","Mi respuesta es no","Mis fuentes me dicen que no","Las perspectivas no son buenas","Muy dudoso"]

class comando(commands.Cog):
	
	def __init__(self, bot):
		self.bot=bot

	@commands.command()
	async def ping(self,ctx):
		before = time.monotonic()
		message = await ctx.send("Pong!")
		ping = (time.monotonic() - before) * 1000
		await message.edit(content=f"Pong!  `{int(ping)}ms`")
		print(f'Ping {int(ping)}ms')
		#print(str(ctx.author.avatar_url))

	@commands.command()
	async def info(self,ctx):

		embed=discord.Embed(title="Vrooooooom", description="El suicidio es una opcion", color=0x0b00d7)
		embed.set_author(name="HowDoYouTurnThisOn? Bot (El autismo evoluciona) v.0.1", icon_url="https://i.kym-cdn.com/entries/icons/facebook/000/020/043/cobra.jpg")
		embed.set_footer(text = "creado por: tu pana Wololo#2078", icon_url = "https://cdn.discordapp.com/avatars/186538096580493312/c1995c58657e24f82a173f682d7abfdd.webp?size=1024")		
		await ctx.send(embed=embed)

	@commands.command()
	async def bola(self,ctx,*,ask):
	        await ctx.send("<@"+ str(ctx.author.id )+ "> "+lista[randint(0, 19)])


	@commands.command()
	async def dado(self,ctx,d:str,num:int):
	        d=d.replace("d","")
	        culo=""
	        e=0
	        if int(d) > 1:
	            for x in range(int(d)):
	                azar=str(randint(0,num))
	                e=int(azar)+e
	                culo=azar+"+"+culo
	            culo=culo[:-1]
	            await ctx.send("<@"+ str(ctx.author.id )+ "> " +culo+ " = "+str(e))
	        else:
	            await ctx.send("<@"+ str(ctx.author.id )+ "> "+ str(randint(0,num)))






#Codigos de error

	async def cog_command_error(self,ctx,error):
	 	if isinstance(error,commands.MissingRequiredArgument):
	 		await ctx.send("manda la vaina bien gay ve help")
def setup(bot):
	bot.add_cog(comando(bot))