import discord
import nacl
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='cyka.', description='CYKABOT: your little russian friend!')

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)

@bot.command(pass_context=True)
async def blyat(ctx):
	author=ctx.message.author
	channel=author.voice_channel
	vc = await bot.join_voice_channel(channel)
	player = vc.create_ffmpeg_player('voices/russian.mp3')
	player.start()
	while True:
		if player.is_done() == True:
			break
	await vc.disconnect()

bot.run('NDk2NDI0NDU3OTA5MzA1MzU2.DpQbQw.WNyT2mFhDjGiMpflfFDquwP3xVA')
