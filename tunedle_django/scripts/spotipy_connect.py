import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd


def get_all_playlist_items(playlist_len, playlist_uri, sp, limit_step=100):
  tracks = []
  for offset in range(0, playlist_len, limit_step):
    response = sp.playlist_items(playlist_uri,
      limit=limit_step,
      offset=offset,
    )['items']
    if len(response) == 0:
      break
    tracks.extend(response)
  return tracks


def get_things(playlist):
  playlist_albums = []
  for i in playlist:

    img = i['track']['album']['images'][0]['url']
    name = i['track']['album']['name']
    artist = i['track']['artists'][0]['name']
    playlist_albums.append({'name': name, 'artist': artist, 'image': img, 'date_used': None })

  df = pd.DataFrame(playlist_albums)

  return df


def run():
  
    cid = "1f1c5bbbc4524659be74b57d195ba5ae"
    # Need to paste in secret key before running
    secret = 'Enter Access Key Here'

    # Authenticating
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Pulling playlist
    playlist_link = "https://open.spotify.com/playlist/1udqwx26htiKljZx4HwVxs?si=c1082668a5b24ace"
    playlist_uri = playlist_link.split("/")[-1].split("?")[0]
    playlist_items = get_all_playlist_items(200, playlist_uri, sp)
    get_things(playlist_items).to_csv('data/albums.csv')