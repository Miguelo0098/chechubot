import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='<', description='bot stuff')

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)

@bot.command(pass_context=True)
async def hola(ctx):
	await bot.say('@{} Saludos, individuo humanoide.'.format(str(ctx.message.author)))

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
	await bot.join_voice_channel(channel)
	await vc.disconnect(channel)

bot.run('MzYyOTQ1NDE0MzIxNjY4MDk2.DYAFIQ._wULz77Vrzu1kxdmA47SwaWK58k')
