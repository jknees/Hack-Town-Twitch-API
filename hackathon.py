import requests
import json
from flask import Flask, render_template

app = Flask(__name__)

top4_data = requests.get('https://api.twitch.tv/kraken/games/top?limit=4')
top_data = json.loads(top4_data.text)

games = []

for i in range(4):
    games.append(top_data['top'][i]['game']['name'])

devs_choice = {'Dark Souls': 'Dark%20Souls'}
dev_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(devs_choice['Dark Souls'])).text)
game1_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[0].replace(' ', '%20'))).text)
game2_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[1].replace(' ', '%20'))).text)
game3_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[2].replace(' ', '%20'))).text)
game4_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[3].replace(' ', '%20'))).text)

def game_details(data):
    '''
Returns details for given data.
args:
    data: link of parsed json
returns:
    Details of game in a dictionary file
'''
    details = {'Current Views':data['streams'][0]['viewers'],\
                'Display Name':data['streams'][0]['channel']['display_name'],\
                'Game Name':data['streams'][0]['channel']['game'],\
                'Total Views': data['streams'][0]['channel']['views'],\
                'Followers': data['streams'][0]['channel']['followers'],\
                'Logo':data['streams'][0]['channel']['logo'],\
                'Status':data['streams'][0]['channel']['status']}
    return details

@app.route("/")
@app.route("/index.html")
@app.route("/index")
def index():
    """ Displays the index page accessible at '/'
    """
    top4_data = requests.get('https://api.twitch.tv/kraken/games/top?limit=4')
    top_data = json.loads(top4_data.text)
    game1_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[0].replace(' ', '%20'))).text)
    game2_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[1].replace(' ', '%20'))).text)
    game3_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[2].replace(' ', '%20'))).text)
    game4_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[3].replace(' ', '%20'))).text)
    return render_template('index.html', Game1 = games[0],\
                                         Game2 = games[1],\
                                         Game3 = games[2],\
                                         Game4 = games[3],\
                                         )
@app.route("/top_pick.html")
@app.route("/top_pick")
def top_pick():
    """ Displays the top_pick page accessible at '/'
    """
    top4_data = requests.get('https://api.twitch.tv/kraken/games/top?limit=4')
    top_data = json.loads(top4_data.text)
    game1_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[0].replace(' ', '%20'))).text)
    game2_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[1].replace(' ', '%20'))).text)
    game3_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[2].replace(' ', '%20'))).text)
    game4_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[3].replace(' ', '%20'))).text)
    return render_template('top_pick.html', streamer = game_details(dev_data)['Display Name'],\
                                         channel = game_details(dev_data)['Display Name'].strip(' '), \
                                         Stream = game_details(dev_data)['Status'], \
                                         picture = game_details(dev_data)['Logo'],\
                                         current_viewers = game_details(dev_data)['Current Views'],\
                                         Game1 = games[0],\
                                         Game2 = games[1],\
                                         Game3 = games[2],\
                                         Game4 = games[3],\
                                         )

@app.route("/top_stream.html")
@app.route("/top_stream")
def top_stream():
    """ Displays the top_stream page accessible at '/'
    """
    top4_data = requests.get('https://api.twitch.tv/kraken/games/top?limit=4')
    top_data = json.loads(top4_data.text)
    game1_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[0].replace(' ', '%20'))).text)
    game2_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[1].replace(' ', '%20'))).text)
    game3_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[2].replace(' ', '%20'))).text)
    game4_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[3].replace(' ', '%20'))).text)
    return render_template('top_stream.html', streamer = game_details(game1_data)['Display Name'],\
                                         channel = ''.join(game_details(game1_data)['Display Name'].split()), \
                                         Stream = game_details(game1_data)['Status'], \
                                         picture = game_details(game1_data)['Logo'],\
                                         current_viewers = game_details(game1_data)['Current Views'],\
                                         Game1 = games[0],\
                                         Game2 = games[1],\
                                         Game3 = games[2],\
                                         Game4 = games[3],\
                                         )

@app.route("/game1.html")
@app.route("/game1")
def game1():
    """ Displays the game1 page accessible at '/'
    """
    top4_data = requests.get('https://api.twitch.tv/kraken/games/top?limit=4')
    top_data = json.loads(top4_data.text)
    game1_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[0].replace(' ', '%20'))).text)
    game2_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[1].replace(' ', '%20'))).text)
    game3_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[2].replace(' ', '%20'))).text)
    game4_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[3].replace(' ', '%20'))).text)
    return render_template('game1.html', streamer = game_details(game1_data)['Display Name'],\
                                         channel = ''.join(game_details(game1_data)['Display Name'].split()), \
                                         Stream = game_details(game1_data)['Status'], \
                                         picture = game_details(game1_data)['Logo'],\
                                         current_viewers = game_details(game1_data)['Current Views'],\
                                         Game1 = games[0],\
                                         Game2 = games[1],\
                                         Game3 = games[2],\
                                         Game4 = games[3],\
                                         )

@app.route("/game2.html")
@app.route("/game2")
def game2():
    """ Displays the game2 page accessible at '/'
    """
    top4_data = requests.get('https://api.twitch.tv/kraken/games/top?limit=4')
    top_data = json.loads(top4_data.text)
    game1_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[0].replace(' ', '%20'))).text)
    game2_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[1].replace(' ', '%20'))).text)
    game3_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[2].replace(' ', '%20'))).text)
    game4_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[3].replace(' ', '%20'))).text)
    return render_template('game2.html', streamer = game_details(game2_data)['Display Name'],\
                                         channel = ''.join(game_details(game2_data)['Display Name'].split()), \
                                         Stream = game_details(game2_data)['Status'], \
                                         picture = game_details(game2_data)['Logo'],\
                                         current_viewers = game_details(game2_data)['Current Views'],\
                                         Game1 = games[0],\
                                         Game2 = games[1],\
                                         Game3 = games[2],\
                                         Game4 = games[3],\
                                         )


@app.route("/game3.html")
@app.route("/game3")
def game3():
    """ Displays the game3 page accessible at '/'
    """
    top4_data = requests.get('https://api.twitch.tv/kraken/games/top?limit=4')
    top_data = json.loads(top4_data.text)
    game1_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[0].replace(' ', '%20'))).text)
    game2_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[1].replace(' ', '%20'))).text)
    game3_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[2].replace(' ', '%20'))).text)
    game4_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[3].replace(' ', '%20'))).text)
    return render_template('game3.html', streamer = game_details(game3_data)['Display Name'],\
                                         channel = ''.join(game_details(game3_data)['Display Name'].split()), \
                                         Stream = game_details(game3_data)['Status'], \
                                         picture = game_details(game3_data)['Logo'],\
                                         current_viewers = game_details(game3_data)['Current Views'],\
                                         Game1 = games[0],\
                                         Game2 = games[1],\
                                         Game3 = games[2],\
                                         Game4 = games[3],\
                                         )


@app.route("/game4.html")
@app.route("/game4")
def game4():
    """ Displays the game4 page accessible at '/'
    """
    top4_data = requests.get('https://api.twitch.tv/kraken/games/top?limit=4')
    top_data = json.loads(top4_data.text)
    game1_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[0].replace(' ', '%20'))).text)
    game2_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[1].replace(' ', '%20'))).text)
    game3_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[2].replace(' ', '%20'))).text)
    game4_data = json.loads(requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(games[3].replace(' ', '%20'))).text)
    return render_template('game4.html', streamer = game_details(game4_data)['Display Name'],\
                                         channel = ''.join(game_details(game4_data)['Display Name'].split()), \
                                         Stream = game_details(game4_data)['Status'], \
                                         picture = game_details(game4_data)['Logo'],\
                                         current_viewers = game_details(game4_data)['Current Views'],\
                                         Game1 = games[0],\
                                         Game2 = games[1],\
                                         Game3 = games[2],\
                                         Game4 = games[3],\
                                         )

if __name__ == "__main__":
    app.run()
