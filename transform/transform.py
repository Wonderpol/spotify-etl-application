import pandas as pd
import json


def create_song_df(request_result: json) -> pd.DataFrame:
    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    for song in request_result["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])

    song_dict = {
        "song_name": song_names,
        "artist_name": artist_names,
        "played_at": played_at_list,
        "timestamp": timestamps
    }

    return pd.DataFrame(song_dict, columns=["song_name", "artist_name", "played_at", "timestamp"])
