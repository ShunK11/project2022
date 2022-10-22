import pandas as pd
from sklearn.svm import SVC
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
import numpy as np
import get_track_features as gtf
import os
import pickle

def study(table_name,now_condition,track):
    path = now_condition + '.pkl'
    is_file = os.path.isfile(path)
    if is_file:
        # print("buriburi")
        # print(track[7:19])
        data = track[7:19]
        # print("buriburi")
        data = np.array(data).reshape(1,-1)
        data = pd.DataFrame(data, columns=["key", "mode","danceability","acousticness","energy","instrumentalness","liveness","loudness","speechiness","tempo","time_signature","valence"] )
        # print(data)
        # if int(model.predict(data))
        model = pickle.load(open(now_condition+'.pkl', 'rb'))
        return int(model.predict(data))
    else:
        df = pd.read_csv('data/' + table_name + '_out.csv')

        df = df.drop_duplicates()
        # print(df)
        # -- Separate features and label
        # (a) drop target column
        X = df.iloc[:,7:19]
        # print(df)
        # print(len(X))
        # print(X)
        # time_zone = time_zone.iloc[:,6:17]
        # weather = weather.iloc[:,6:17]
        # X = df.drop(columns=['season'])
        # (b) make an array with the target column
        y = df[now_condition].copy()
        # print(y)
        for i in range(0,len(y)):
            # y[i] = str(0)
            if y[i] >= 1:
                y[i] = str(1)
            else:
                y[i] = str(0)
        # y = [i = 1 for i in list(y) if i == "spring"]

        # -- Split the dataset into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
        clf_s = SVC(gamma="auto")
        clf_s.fit(X, y)

        # k-近傍法（k-NN）
        from sklearn.neighbors import KNeighborsClassifier

        #k-NNインスタンス。今回は3個で多数決。3の値を変更して色々試すと〇
        model = KNeighborsClassifier(n_neighbors=3)
        #学習モデル構築。引数に訓練データの特徴量と、それに対応したラベル
        model.fit(X_train, y_train)
        file = now_condition+".pkl"
        pickle.dump(model, open(file, 'wb'))
        # .scoreで正解率を算出。
        # print("train score:",model.score(X_train,y_train))
        # print("test score:",model.score(X_test,y_test))

        # print(data)
        data = track[7:19]
        data = np.array(data).reshape(1,-1)
        data = pd.DataFrame(data, columns=["key", "mode","danceability","acousticness","energy","instrumentalness","liveness","loudness","speechiness","tempo","time_signature","valence"])
        # print(data)
        # if int(model.predict(data))
        return int(model.predict(data))

    # df = pd.read_csv('spotify_shun_musicdata.csv')
    # X = df.iloc[:,6:17]
    # print(X)
    # pd.DataFrame(data, columns=[“列名A”, “列名B“…] )
    # stu("summer",)
    