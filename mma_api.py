import requests 
import time

api_key = 'mma api token'
# API docs :  https://developer.sportradar.com/docs/read/combat_sports/MMA_v2#mma-api-overview


# User input - 찾기 원하는 정보
search_keyword = 'UFC 273'
name_keyword = 'Jung'

######Season Info#########
seasons_data = requests.get('http://api.sportradar.us/mma/trial/v2/en/seasons.json?api_key=' + api_key)
seasons = seasons_data.json()

id_info = ''

for i in range(len(seasons['seasons'])):
  if search_keyword in seasons['seasons'][i]['name']:
    id_info = seasons['seasons'][i]['id']


########Get fighter id ###############

######
# Developer over Qps (1query/1sec)
# 1초에 하나의 쿼리를 던지기 위해서 time.sleep 
######

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

print(f'''
name: "{competitor_name}",
nickname: {competitor_nickname}
gender: {competitor_gender}
fighting out of country: {competitor_country}
reach: {competitor_reach}
height: {competitor_height}
weight: {competitor_weight}

record: "wins": {competitor_wins}, "draws": {competitor_draws}, "losses": {competitor_losses}


''')


#####Response- JSON - ERROR EXCEPTION#####
# print (competitor_profile)

# fighter_id = 'sr:competitor:312937'

# try:
#     competitor_profile_data = requests.get('http://api.sportradar.us/mma/trial/v2/en/competitors/'+ fighter_id +'/profile.json?api_key='+ key)
#     competitor_profile = competitor_profile_data.json()
# except requests.exceptions.JSONDecodeError as e:
#     print(e)
#     print(competitor_profile_data.content)
    
