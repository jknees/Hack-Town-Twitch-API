import requests, json
from flask import Flask, render_template

app = Flask(__name__)

devs_choice = {'Dark Souls': 'Dark%20Souls'}

dev_data = requests.get('https://api.twitch.tv/kraken/streams?game={}&limit=1'.format(devs_choice['Dark Souls']))

data = json.loads(dev_data.text)

game_details = {'Current Views':data['streams'][0]['viewers'],\
                'Display Name':data['streams'][0]['channel']['display_name'],\
                'Game Name':data['streams'][0]['channel']['game'],\
                'Total Views': data['streams'][0]['channel']['views'],\
                'Followers': data['streams'][0]['channel']['followers'],\
                'Logo':data['streams'][0]['channel']['logo'],\
                'Status':data['streams'][0]['channel']['status']}

@app.route("/")
def details():
    """ Displays the index page accessible at '/'
    """
    return render_template('index.html', streamer = game_details['Display Name'],\
                                         channel = game_details['Display Name'], \
                                         Stream = game_details['Status'], \
                                         picture = game_details['Logo'])

if __name__ == "__main__":
    app.run()
