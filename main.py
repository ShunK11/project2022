import spotipy
import spotipy.util as util
import time
import return_now_track as rnt

#入力パート Input part
creat_playlist = 'now_playlist'
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


def creat_play_list(list_name):
    spotify.user_playlist_create(username, name = list_name)
    list_data = spotify.user_playlists(user = username)
    for i in range(list_data['total']):
        play_list_name = list_data['items'][i]['name']
        if play_list_name == list_name:
            list_data
            url = list_data['items'][i]['external_urls']['spotify']
        else:
            pass
    return(url)


# def set_tempo_track(original_play_list, set_tempo, set_tempo_range):
#     list_data = spotify.playlist_tracks(original_play_list)
#     track_num = list_data['total']
#     if track_num > 100:
#         track_num =100
#     urls_list =[]
#     for i in range(track_num):
#         track_url = list_data['items'][i]['track']['external_urls']['spotify']
#         urls_list.append(track_url)
#     time.sleep(1) #1sec stop
#     tempo_urls_list =[]
#     for i in range(len(urls_list)):
#         track_url = urls_list[i]
#         track_feature = spotify.audio_features(track_url)[0]
#         time.sleep(1)
#         tempo = track_feature['tempo']
#         if (set_tempo-set_tempo_range) <= tempo <= (set_tempo + set_tempo_range):
#             tempo_urls_list.append(track_url)
#         else:
#             pass
#     return(tempo_urls_list)

play_list = creat_play_list(creat_playlist)
# tempo_urls_list = set_tempo_track(original_play_list, set_tempo, set_tempo_range)
# tracks = []
time.sleep(1)
tracks = list(rnt.track)
# tracks = {'0lz8eaAm64O2ODrDFCF1FV', '0W3uBjee7bOmKKlGoEk7yP', '0MemW1DmggDpHBGH4GgiaS', '5DMEvbg3gUmiR5HIBWdveV', '3gQSWGaCoaxONqXitmn7GX', '0XZyF9lv6diMt4bxThOL0h', '27udJcfu06TvbbOpgfxIlw', '4F32PqWZOPn2l8148QSlsT', '6UHwmfYfRm445uyyM9HO3o', '3TxjMrMGWFP0jkIy0tVvVn', '6n6dWS9oA9ImlFnXuWTXOC', '4JaLkM90MJutDAl5jD9BZX', '0xp3X2cwvMCfhVLIEzMSZj', '65zCSX2CSQXp1vr4hNtHDv', '4QL5DKkPZwBXkph4fW2Y0Z', '2A0zCiphI5e6Vxat20qyEv', '0nwLTlecLApkMzVXsiKdlD', '7dH0dpi751EoguDDg3xx6J', '6iEh5ejX1KRNZnYjyzBdjG', '6j0QZZa5O2LqSl1lWgypOw', '6nTtJld6EMw4MNoz21uUwF'}
# tracks = list(tracks)
spotify.user_playlist_add_tracks(username, play_list, tracks)
print('finish')
print(play_list)