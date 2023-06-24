import discord
from discord.ext import commands
import requests 
import time
import json

with open('config.json','r') as config_file:
    config_data = json.load(config_file)
    
api_key = config_data['API_KEY']
token = config_data['DISCORD_TOKEN']

print(api_key, token)

bot = commands.Bot(command_prefix='/',intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')

@bot.command()
async def mma(message, name_keyword, search_keyword):
    try:
        name_keyword = name_keyword.lower()
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
            if name_keyword in season_info['competitors'][i]['name'].lower():
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
    
    except Exception as e:
        print(e)
        await message.channel.send("Please Check For Any Spelling Errors")

bot.run(token)

