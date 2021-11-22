from os import getenv
from dotenv import load_dotenv
from datetime import datetime
import datetime
import requests

load_dotenv()

headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token} ".format(token=getenv("TOKEN"))
    }


def check_request_status(req: requests.request):
    if req.status_code != requests.codes.ok:
        print(f"Downloading error with code: {req.status_code}")
        req_json = req.json()
        print(req_json['error']['message'])
        exit(-1)


def get_recently_played_songs() -> requests.Response:

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    req = requests.get(
        "https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp),
        headers=headers)

    check_request_status(req)

    return req.json()


def get_top_three_artists() -> requests.Response:
    req = requests.get("https://api.spotify.com/v1/me/top/artists?limit=3",
                       headers=headers)

    check_request_status(req)

    return req.json()
