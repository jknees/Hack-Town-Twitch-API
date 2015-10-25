import requests, json
from flask import Flask, render_template

app = Flask(__name__)

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

def details():
    """ Displays the index page accessible at '/'
    """
    return render_template('index.html', game1 = top4_games[0],\
                                         game2 = top4_games[1],\
                                         game3 = top4_games[2],\
                                         game4 = top4_games[3])

if __name__ == "__main__":
    app.run()
