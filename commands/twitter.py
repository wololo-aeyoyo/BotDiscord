import discord
from threading import Thread
from discord.ext import commands
from random import randint
import aiohttp
import aiofiles
import os
from PIL import Image
from TwitterAPI import TwitterAPI
import asyncio
faggot=0
verga =0
api = TwitterAPI(os.environ["betica"],os.environ["betica2"],os.environ["betica3"],os.environ["betica4"])
NUMBER_OF_TWEETS_TO_DELETE = 1
class DeleteTweet(Thread):

    def __init__(self, tweet_id, count):
        Thread.__init__(self)
        self.tweet_id = tweet_id
        self.count = count

    def run(self):
        r = api.request('statuses/destroy/:%d' % self.tweet_id)
        print(self.count if r.status_code == 200 else 'PROBLEM: ' + r.text)


class comando(commands.Cog):
	
	def __init__(self, bot):
		self.bot=bot

	@commands.command()
	async def twitter(self,ctx,*,texto:str):
	    global soltext;soltext=texto
	    global faggot;faggot=1
	    global verga
	    global e
	    global flag
	    global mensajito
	    global nameo		
	    print("end my suffering")
	    nameo="<@"+ str(ctx.author.id )+ "> " 
	    print("aaasckasdmnfksdnmfklsdmfk")
	    if len(ctx.message.attachments)==0:
	    	await ctx.send("<@"+ str(ctx.author.id )+ "> "+" quiere spamear una vaina ahi en twister \n reacciona con 👍🏻 ~~a ver si me me cierran el twitter~~, \n reacciona con 👎🏿 porque es cringe \n los votos se mandaran en una (1) unidad de minuto")
	    	embed=discord.Embed(title="Wololo's personal twitter", url="https://twitter.com/Wololo_aeyoyo/", description="el mensaje autista: "+ soltext, color=0x031cfc)
	    	embed.set_footer(text=str(ctx.author.name)+" si tu pendejo")
	    	embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTvrFytZTMQnW6cD-85691yjeNYHetZ3aXe1Ts3sYzLzptQXXx")
	    	mensajito = await ctx.send(embed=embed)		
	    	await mensajito.add_reaction("👍🏻")
	    	await mensajito.add_reaction("👎🏿")
	    	verga=1
	    else:
	    	mensajito=ctx
	    	e=str(ctx.message.attachments[0])
	    	nani=e.split()
	    	link=str(nani[3])
	    	link=link.replace("url='","")
	    	link=link[:-2]
	    	await ctx.send("<@"+ str(ctx.author.id )+ "> "+" quiere spamear una vaina ahi en twister \n reacciona con 👍🏻 ~~a ver si me me cierran el twitter~~, \n reacciona con 👎🏿 porque es cringe \n los votos se mandaran en una (1) unidad de minuto")
	    	embed=discord.Embed(title="Wololo's personal twitter", url="https://twitter.com/Wololo_aeyoyo/", description="el mensaje autista: "+ soltext, color=0x031cfc)
	    	embed.set_footer(text=str(ctx.author.name)+" si tu pendejo")
	    	embed.set_image(url=link)
	    	embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTvrFytZTMQnW6cD-85691yjeNYHetZ3aXe1Ts3sYzLzptQXXx")
	    	mensajito = await ctx.send(embed=embed)		
	    	await mensajito.add_reaction("👍🏻")
	    	await mensajito.add_reaction("👎🏿")						
	    	flag=1			 
			

	@commands.command()
	async def testing(self,ctx,*,texto:str):
		embed=discord.Embed(title="[Click pa ve donde]", url="https://twitter.com/Wololo_aeyoyo/status/", description="el mensaje autista: ", color=0x031cfc)
		embed.set_author(name="Tu Tweet se posteo relajado en @wololo_aeyoyo", url="https://twitter.com/Wololo_aeyoyo", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTvrFytZTMQnW6cD-85691yjeNYHetZ3aXe1Ts3sYzLzptQXXx")
		embed.set_footer(text=str(ctx.author.name)+" si tu pendejo")
		mensajito = await ctx.send(embed=embed)		
		await mensajito.add_reaction("👍🏻")
		await mensajito.add_reaction("👎🏿")

	@commands.Cog.listener()
	async def on_message(self, message): 
		global verga 
		global faggot
		global e
		global nameo
		global flag
		if message.author.id==603204431135375370 and faggot==1:
			await asyncio.sleep(60)
			print("paso por listener")
			counts = {react.emoji: react.count for react in message.reactions}
			print(counts)
			compa=counts['👍🏻']
			compb=counts['👎🏿']

			
			if compa>compb and verga==1:
	 			r = api.request('statuses/update', {'status': soltext})
	 			print('SUCCESS' if r.status_code == 200 else 'PROBLEM: ')
	 			count=0
	 			r=api.request('statuses/user_timeline', {'count': 1})
	 			for item in r:
	 				if 'id' in item:
	 					count += 1
	 			tweet_id = item['id']
	 			faggot=0
	 			verga=0
	 			flag=0 
	 			embed=discord.Embed(title="[Click pa ve donde]", url="https://twitter.com/Wololo_aeyoyo/status/"+str(tweet_id), description="el mensaje autista: "+ soltext, color=0x031cfc)
	 			embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTvrFytZTMQnW6cD-85691yjeNYHetZ3aXe1Ts3sYzLzptQXXx")
	 			embed.set_author(name="Tu Tweet se posteo relajado en @wololo_aeyoyo", url="https://twitter.com/Wololo_aeyoyo", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTvrFytZTMQnW6cD-85691yjeNYHetZ3aXe1Ts3sYzLzptQXXx")
	 			embed.set_footer(text="dame sexo mi pana")
	 			await message.channel.send(embed=embed)



			if compa>compb and flag==1:
				flag=0
				faggot=0
				print("imagen mega gay")
				nani=e.split()
				link=str(nani[3])
				nombre=str(nani[2])
				nombre=nombre.replace("filename='","")
				nombre=nombre[:-1]
				link=link.replace("url='","")
				link=link[:-2]
				async with aiohttp.ClientSession() as session:
					async with session.get(link) as imagen:
						if imagen.status == 200:
							pic = await imagen.read()
							with open("images/{}".format(nombre), "wb") as f:
								f.write(pic)

							if nombre.endswith(".png" or ".jpg"):
								foo = Image.open("images/{}".format(nombre))
								rgb_im = foo.convert('RGB')
								rgb_im.thumbnail((1024, 1080), Image.ANTIALIAS)
								rgb_im.save("images/tumbnaila_{}".format(nombre)+".jpg",quality=95,optimize=True)
								file = open("images/tumbnaila_{}".format(nombre)+".jpg", 'rb')

							else:
								file = open("images/{}".format(nombre), 'rb')

							data = file.read()
							r = api.request('media/upload', None, {'media': data})
							print('UPLOAD MEDIA SUCCESS' if r.status_code == 200 else 'UPLOAD MEDIA FAILURE: ' + r.text)

							if r.status_code == 200:
								media_id = r.json()['media_id']
							print(media_id)
							r = api.request('statuses/update', {'status': soltext, 'media_ids': media_id})
							print(r)
							print('UPDATE STATUS SUCCESS' if r.status_code == 200 else 'UPDATE STATUS FAILURE: ' + r.text)
							print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
							count=0
							r=api.request('statuses/user_timeline', {'count': 1})
							for item in r:
								if 'id' in item:
									count += 1
									tweet_id = item['id']
							embed=discord.Embed(title="[Click pa ve donde]", url="https://twitter.com/Wololo_aeyoyo/status/"+str(tweet_id), description="el mensaje autista: "+soltext, color=0x031cfc)
							embed.set_author(name="Tu Tweet se posteo relajado en @wololo_aeyoyo", url="https://twitter.com/Wololo_aeyoyo", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTvrFytZTMQnW6cD-85691yjeNYHetZ3aXe1Ts3sYzLzptQXXx")
							embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTvrFytZTMQnW6cD-85691yjeNYHetZ3aXe1Ts3sYzLzptQXXx")
							embed.set_footer(text="dame sexo mi pana")
							embed.set_image(url=link)
							await message.channel.send(embed=embed)
			if compa<=compb:
				await message.channel.send(nameo+"post descartado por ser cringe")
				flag=0
				faggot=0
				verga=0											




#Codigos de error

	async def cog_command_error(self,ctx,error):
	 	if isinstance(error,commands.MissingRequiredArgument):
	 		await ctx.send("Mandame algo bien hecho gay")


def setup(bot):
	bot.add_cog(comando(bot))
