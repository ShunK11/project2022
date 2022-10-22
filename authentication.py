import spotipy
import spotipy.util as util

#認証パート Authentication part
import os
#認証パート Authentication part
username = os.environ["username"]
my_id =os.environ["my_id"]
my_secret = os.environ["my_secret"]
redirect_uri = os.environ["redirect_uri"]
#アプリの権限付与に使用する
scope = 'user-library-read user-read-playback-state playlist-read-private user-read-recently-played playlist-read-collaborative playlist-modify-public playlist-modify-private'

token = util.prompt_for_user_token(username, scope, my_id, my_secret, redirect_uri)
spotify = spotipy.Spotify(auth = token)