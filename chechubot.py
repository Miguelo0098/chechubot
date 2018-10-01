import discord
import nacl
import asyncio
from chechusounds import pick_random_voice
from discord.ext import commands

bot = commands.Bot(command_prefix='<', description='ChechuBot: your friendly bot for personal fun!')

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)

@bot.command(pass_context=True)
async def hola(ctx):
	await bot.say('{} Saludos, entidad corpórea :vulcan:'.format(str(ctx.message.author.mention)))

@bot.command(pass_context=True)
async def ping(ctx):
	await bot.say('@{} Pong.'.format(str(ctx.message.author)))

@bot.group(pass_context=True)
async def role(ctx):
	if ctx.invoked_subcommand is None:
		await bot.say('Dame argumentos, coño.')
		await bot.say('`create -- > crea un rol.\ndelete -- > elimina un rol`')
		pass

@bot.command(pass_context=True)
async def moja(ctx):
	await bot.say('moja')

@bot.command(pass_context=True)
async def habla(ctx):
	author=ctx.message.author
	channel=author.voice_channel
	vc = await bot.join_voice_channel(channel)
	sound = pick_random_voice()
	print(sound)
	player = vc.create_ffmpeg_player(sound)
	player.start()
	while True:
		if player.is_done() == True:
			break
	await vc.disconnect()

bot.run('MzYyOTQ1NDE0MzIxNjY4MDk2.DYAFIQ._wULz77Vrzu1kxdmA47SwaWK58k')
