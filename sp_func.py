import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius
import tweepy
import random
import os
from dotenv import load_dotenv


def download_song_ids(sp, username, playlist_id):
    song_ids = []
    playlist = sp.user_playlist(username, playlist_id)
    for item in playlist['tracks']['items']:
        song = item['track']
        song_ids.append(song['id'])
    return song_ids
