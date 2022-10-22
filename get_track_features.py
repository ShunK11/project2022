# -*- coding: utf-8 -*-
# import sys
# import pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
import os
#認証パート Authentication part
username = os.environ["username"]
my_id =os.environ["my_id"]
my_secret = os.environ["my_secret"]
redirect_uri = os.environ["redirect_uri"]
# import study_s as st

def getTrackFeatures(id):
    # print("artist:" + artist + " name:"+name)
    time.sleep(0.5)
    
    

    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=my_id,
                                                                client_secret=my_secret))

    meta = sp.track(id)
    features = sp.audio_features(id)

    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']
    key = features[0]['key']
    mode = features[0]['mode']
    danceability = features[0]['danceability']
    acousticness = features[0]['acousticness']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']
    valence = features[0]['valence']

    track = [name, album, artist, release_date, length, popularity, key, mode, danceability, acousticness, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature, valence]
    # print(track)
    return track[6:18]