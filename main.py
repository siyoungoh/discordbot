import discord
from discord.ext import commands
import requests 
import time

api_key = 'mma api token'

token = 'discord bot token'
bot = commands.Bot(command_prefix='#',intents=discord.Intents.all())
 
@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')

 
@bot.command()
async def hello(message):
    await message.channel.send('Hi!')

  
# User input
search_keyword = 'UFC 273'
name_keyword = 'Jung'
  
# TODO : 특정 command 입력하면 정보 출력하기 
# 정보 : MMA API 에서 입력한 시즌 이름의 시즌id 값 가져오기
@bot.command()
async def mma(message):
    ######Season Info#########
    seasons_data = requests.get('http://api.sportradar.us/mma/trial/v2/en/seasons.json?api_key=' + api_key)
    seasons = seasons_data.json()
    
    id_info = ''
    
    for i in range(len(seasons['seasons'])):
        if search_keyword in seasons['seasons'][i]['name']:
            id_info = seasons['seasons'][i]['id']
    
    # TODO : Hi 대신 선수 정보 출력하기        
    await message.channel.send('Hi!')
    
 
bot.run(token)
