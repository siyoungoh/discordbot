import discord
from discord.ext import commands
import requests 
import time

token = 'discord bot token'
bot = commands.Bot(command_prefix='#',intents=discord.Intents.all())
 
@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
 
@bot.command()
async def hello(message):
    await message.channel.send('Hi!')
 
bot.run(token)
