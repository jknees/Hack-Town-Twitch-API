import requests, json
from flask import Flask, render_template

top_data = requests.get('https://api.twitch.tv/kraken/games/top?limit=4')
data = json.loads(top_data.text)

top4_games = {}

for i in range(4):
    top4_games[data['top'][i]['game']['name']] = data['top'][i]['game']['name'].replace(" ", "%20")

'''
top4_games = {data['top'][0]['game']['name']:data['top'][0]['game']['name'].replace(" ", "%20"),\
              data['top'][1]['game']['name']:data['top'][1]['game']['name'].replace(" ", "%20"),\
              data['top'][2]['game']['name']:data['top'][2]['game']['name'].replace(" ", "%20"),\
              data['top'][3]['game']['name']:data['top'][3]['game']['name'].replace(" ", "%20")}
'''

