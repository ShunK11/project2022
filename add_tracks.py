import spotipy
import spotipy.util as util

#入力パート Input part
creat_playlist = 'test_list_XXX'

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

# play_list = 'https://open.spotify.com/playlist/XXXXXXXXXXXX'
# track_URL = 'https://open.spotify.com/track/6NJQpFNkDCMaRBogIi9sOI'
tracks = {'0lz8eaAm64O2ODrDFCF1FV', '0W3uBjee7bOmKKlGoEk7yP', '0MemW1DmggDpHBGH4GgiaS', '5DMEvbg3gUmiR5HIBWdveV', '3gQSWGaCoaxONqXitmn7GX', '0XZyF9lv6diMt4bxThOL0h', '27udJcfu06TvbbOpgfxIlw', '4F32PqWZOPn2l8148QSlsT', '6UHwmfYfRm445uyyM9HO3o', '3TxjMrMGWFP0jkIy0tVvVn', '6n6dWS9oA9ImlFnXuWTXOC', '4JaLkM90MJutDAl5jD9BZX', '0xp3X2cwvMCfhVLIEzMSZj', '65zCSX2CSQXp1vr4hNtHDv', '4QL5DKkPZwBXkph4fW2Y0Z', '2A0zCiphI5e6Vxat20qyEv', '0nwLTlecLApkMzVXsiKdlD', '7dH0dpi751EoguDDg3xx6J', '6iEh5ejX1KRNZnYjyzBdjG', '6j0QZZa5O2LqSl1lWgypOw', '6nTtJld6EMw4MNoz21uUwF'}
tracks = list(tracks)
playlist_id = "6eOYYf2efFvrHqZ6E1yB7g"

spotify.user_playlist_add_tracks(user = username, playlist_id = playlist_id, tracks = tracks)