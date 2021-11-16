import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
# Spotify user nickname equals user id
USER_ID = "wonderpol"
# Spotify token generated in api
TOKEN = "BQDjJO7G-YHoF9EIk6RmnExfkW_JCcxZ5MFY9kx3mkcNlEqoOHBFklEJOgCprgbIS6HTPItQUW8ggux3wc8wO94qpK1AI5QcuZad6A23k_K0M-SLRd3ZYwzbTOL5zd0NOsZFsgPcXBdDqGd-sAU"

if __name__ == "__main__":
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token} ".format(token=TOKEN)
    }

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    req = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers=headers)

    data = req.json()

    print(data)