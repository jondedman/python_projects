from bs4 import BeautifulSoup
import requests
import dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

dotenv.load_dotenv()

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Get billboard top 100 songs for a given date

url  = f'https://www.billboard.com/charts/hot-100/1998-09-01'

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

list_items = soup.find_all('li', class_='o-chart-results-list__item')
song_titles = [item.find('h3', class_='c-title').text.strip() for item in list_items if item.find('h3', class_='c-title')]

print(len(song_titles))
for title in song_titles:
    print(title)

# Spotify
client = os.getenv("SPOTIFY_ID")
secret = os.getenv("SPOTIFY_SECRET")
redirect = os.getenv("SPOTIFY_REDIRECT")

# authentication
# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client,
#                                                            client_secret=secret))
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client, client_secret=secret, redirect_uri=redirect, scope=scope))

# get user id
results = sp.current_user()
id = results['id']
# print(id)

#add playlist
new_playlist = sp.user_playlist_create(user="fyburchett", name="1998", public=False, collaborative=False, description="top 100 songs from 1998")
print(new_playlist)

# search for songs
tracks = []
for title in song_titles:
    results = sp.search(q=f'{title}', limit=1)
    track_uri = results['tracks']['items'][0]['uri']
    tracks.append(track_uri)

# add tracks
user = "fyburchett"
playlist_id = "1xogTp0vADS7nw19HtIhWG"

sp.user_playlist_add_tracks(user, playlist_id, tracks, position=None)
