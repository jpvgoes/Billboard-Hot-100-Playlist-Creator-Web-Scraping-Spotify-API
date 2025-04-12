from datetime import datetime
from bs4 import BeautifulSoup
import requests

from dotenv import load_dotenv
import os

#CRIE UM ARQUIVO .ENV PARA CARREGAR SEU "CLIENT_ID" E "CLIENT_SECRET"
load_dotenv()
#----------------- SPOTIFY -----------------#
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

#----------------- BILLBOARD -----------------#

def validar_data(data):
    try:
        datetime.strptime(data, "%Y-%m-%d")  # Tenta converter a string para data
        return True  # Se der certo, retorna True
    except ValueError:
        return False  # Se der erro, retorna False

year = input('Wich year do you want to travel to? Type the date in this format YYYY-MM-DD: ')

while not validar_data(year):
    print("\033[0;31mPlease enter a valid year\033[m")
    year = input('Wich year do you want to travel to? Type the date in this format YYYY-MM-DD: ')

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}


response = requests.get("https://www.billboard.com/charts/hot-100/" + year, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select('li ul li h3')
song_names = [song_name.getText().strip() for song_name in song_names_spans]

#----------------- SPOTIFY -----------------#

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path=".cache",
        username="jpvgoes", 
    )
)
print(sp.current_user())

user_id = sp.current_user()["id"]
song_uris = []

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year.split('-')[0]}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(f"Song {song} found, adding to the list")
        
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
    except Exception as e:
        print(e)
        
playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False,description=f"The Billboard Hot 100 of {year}")
#print(playlist)
playlist_id = playlist["id"]

sp.playlist_add_items(playlist_id, song_uris)
print("\033[0;32mPlaylist created\033[m")
    
