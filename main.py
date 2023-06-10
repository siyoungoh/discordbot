import discord
from discord.ext import commands
from discord import app_commands
import requests 
import time

api_key = 'mma_api_token'
token = 'discord_bot_token'
bot = commands.Bot(command_prefix='/',intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')

 
@bot.command()
async def hello(message):
    await message.channel.send('Hi!')

# User input
search_keyword = 'UFC 273'
name_keyword = 'Jung'
  
# 정보 : MMA API 에서 입력한 시즌 이름의 시즌id 값 가져오기

@bot.command()
async def mma (message):
    ######Season Info#########
    seasons_data = requests.get('http://api.sportradar.us/mma/trial/v2/en/seasons.json?api_key=' + api_key)
    seasons = seasons_data.json()
    
    id_info = ''
    
    for i in range(len(seasons['seasons'])):
        if search_keyword in seasons['seasons'][i]['name']:
            id_info = seasons['seasons'][i]['id']
    
    time.sleep(1)  

    season_info_data = requests.get('http://api.sportradar.us/mma/trial/v2/en/seasons/'+ id_info+'/info.json?api_key='+ api_key)
    season_info = season_info_data.json()
    fighter_id = ''
    for i in range(len(season_info['competitors'])):
        if name_keyword in season_info['competitors'][i]['name']:
            fighter_id = season_info['competitors'][i]['id']
        
    competitor_profile_data = requests.get('http://api.sportradar.us/mma/trial/v2/en/competitors/'+ fighter_id +'/profile.json?api_key='+ api_key)
    competitor_profile = competitor_profile_data.json() 
    competitor_name = competitor_profile['competitor']['name']
    competitor_nickname = competitor_profile['info']['nickname']
    competitor_gender = competitor_profile['competitor']['gender']
    competitor_country = competitor_profile['info']['fighting_out_of_country']
    competitor_reach = competitor_profile['info']['reach']
    competitor_height = competitor_profile['info']['height']
    competitor_weight = competitor_profile['info']['weight']
    competitor_wins = competitor_profile['record']['wins']
    competitor_draws = competitor_profile['record']['draws']
    competitor_losses = competitor_profile['record']['losses']

    
    embed = discord.Embed(title='FIGHTER INFO',
                          description=f"This is '{competitor_name}''s info")
    embed.add_field(name='Name', value=f'{competitor_name}', inline=False)
    embed.add_field(name='Nickname', value=f'{competitor_nickname}', inline=False)
    embed.add_field(name='Gender', value=f'{competitor_gender}', inline=False)
    embed.add_field(name='Fighting out of country', value=f'{competitor_country}', inline=False)
    embed.add_field(name='Reach', value=f'{competitor_reach}', inline=False)
    embed.add_field(name='Height', value=f'{competitor_height}', inline=False)
    embed.add_field(name='Weight', value=f'{competitor_weight}', inline=False)
    embed.add_field(name='Record', value=f'wins: {competitor_wins}, Draws: {competitor_draws}, losses: {competitor_losses}', inline=False)
    
    


    await message.send(embed=embed)

@bot.command()
async def mmas(message, name_keyword, search_keyword):
    seasons_data = requests.get('http://api.sportradar.us/mma/trial/v2/en/seasons.json?api_key=' + api_key)
    seasons = seasons_data.json()
   
       
    # await message.send(embed=embed)
    # /echo something some
    # param1 = 성 (이름)
    #pram 2 = 그사람의 메인 이벤트 (예: UFC ###)

    
    id_info = ''
    
    for i in range(len(seasons['seasons'])):
        if search_keyword in seasons['seasons'][i]['name']:
            id_info = seasons['seasons'][i]['id']
    
    time.sleep(1)  

    season_info_data = requests.get('http://api.sportradar.us/mma/trial/v2/en/seasons/'+ id_info+'/info.json?api_key='+ api_key)
    season_info = season_info_data.json()
    fighter_id = ''
    for i in range(len(season_info['competitors'])):
        if name_keyword in season_info['competitors'][i]['name']:
            fighter_id = season_info['competitors'][i]['id']
        
    competitor_profile_data = requests.get('http://api.sportradar.us/mma/trial/v2/en/competitors/'+ fighter_id +'/profile.json?api_key='+ api_key)
    competitor_profile = competitor_profile_data.json() 
    competitor_name = competitor_profile['competitor']['name']
    competitor_nickname = competitor_profile['info']['nickname']
    competitor_gender = competitor_profile['competitor']['gender']
    competitor_country = competitor_profile['info']['fighting_out_of_country']
    competitor_reach = competitor_profile['info']['reach']
    competitor_height = competitor_profile['info']['height']
    competitor_weight = competitor_profile['info']['weight']
    competitor_wins = competitor_profile['record']['wins']
    competitor_draws = competitor_profile['record']['draws']
    competitor_losses = competitor_profile['record']['losses']

    
    embed = discord.Embed(title='FIGHTER INFO',
                          description=f"This is '{competitor_name}''s info")
    embed.add_field(name='Name', value=f'{competitor_name}', inline=False)
    embed.add_field(name='Nickname', value=f'{competitor_nickname}', inline=False)
    embed.add_field(name='Gender', value=f'{competitor_gender}', inline=False)
    embed.add_field(name='Fighting out of country', value=f'{competitor_country}', inline=False)
    embed.add_field(name='Reach', value=f'{competitor_reach}', inline=False)
    embed.add_field(name='Height', value=f'{competitor_height}', inline=False)
    embed.add_field(name='Weight', value=f'{competitor_weight}', inline=False)
    embed.add_field(name='Record', value=f'wins: {competitor_wins}, Draws: {competitor_draws}, losses: {competitor_losses}', inline=False)
    
    


    await message.send(embed=embed)
bot.run(token)
 
