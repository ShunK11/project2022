# import get_saved_tracks as gst
import sqlite3
import pandas as pd
import numpy as np
import learn as st
import get_now as gn

dbname = 'TEST.db'
conn = sqlite3.connect(dbname)
c = conn.cursor()

df = pd.read_csv('data/saved_tracks.csv')

check_lists = {"season":[],"time":[],"weather":[]}
# condition_lists = ["fall","sunny","night"]
condition_lists = gn.now_list
for index, track in df.iterrows():
    # track = item['track']
    if track["name"]:
        name = track["name"]
        artist = track["artist"]
    # print(name,artist)

    for check_list,condition_list in zip(check_lists,condition_lists):
        try: #DBに曲が入っている場合
            
            c.execute("SELECT "+condition_list+" FROM "+check_list+"_table WHERE Name=? and Artist=? and "+condition_list+">= 2",(name,artist))
            data_list = c.fetchone()
            # print(data_list)
            if data_list is not None:
                check_lists[check_list].append(track["id"])
                # print(check_lists)
            else:
                data_list = str(data_list[6])
        except: #DBに曲が入っていない場合
            # print(name)
            # print(st.study(check_list,condition_list,track))
            if st.study(check_list,condition_list,track):
                check_lists[check_list].append(track["id"])
            pass
        # print(check_lists)

# print(type(check_lists["season"]))
# print(check_lists["weather"])
# print(check_lists["time"])

# season = set(list[check_lists["season"]])
# weather = set(list[check_lists["weather"]])
track = set(check_lists["time"]) & set(check_lists["season"]) & set(check_lists["weather"])
# print(track)

# print(season)
# print(weather)
# print(time)
        