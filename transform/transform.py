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


def create_top_artist_df(request_result: json) -> pd.DataFrame:
    artist_names = []
    artist_popularities = []
    artist_genres = []

    for artist in request_result["items"]:
        artist_names.append(artist["name"])
        artist_popularities.append(artist["popularity"])
        artist_genres.append((lambda gen: gen[0] if gen != [] else "Not defined")(artist["genres"]))

    artist_dict = {
        "artist_name": artist_names,
        "artist_popularity": artist_popularities,
        "artist_genres": artist_genres
    }

    return pd.DataFrame(artist_dict, columns=["artist_name", "artist_popularity", "artist_genres"])
