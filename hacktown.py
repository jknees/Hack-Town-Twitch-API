import requests, json

from flask import Flask, render_template

r = requests.get("https://api.twitch.tv/kraken/search/streams?q=Dark%20Souls")
data = json.loads(r.text)

game_details = {'Current Views':data['streams'][0]['viewers'],\
				'Top Streamer':data['streams'][0]['channel']['display_name'],\
				'Game Name':data['streams'][0]['channel']['game'],\
				'Total Views': data['streams'][0]['channel']['views'],\
				'Followers': data['streams'][0]['channel']['followers'],\
				'Streamer Logo':data['streams'][0]['channel']['logo']}

def main():
    return render_template('index.html')
    
#if __name__ == '__main__':
	#main()