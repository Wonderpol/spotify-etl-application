from os import getenv
from dotenv import load_dotenv
from datetime import datetime
import datetime
import requests

load_dotenv()


def download_data_from_api() -> requests.Response:
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token} ".format(token=getenv("TOKEN"))
    }

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    req = requests.get(
        "https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp),
        headers=headers)

    if req.status_code != requests.codes.ok:
        print(f"Downloading error with code: {req.status_code}")
        req_json = req.json()
        print(req_json['error']['message'])
        exit(-1)

    return req.json()
