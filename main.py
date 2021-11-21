from os import getenv
from dotenv import load_dotenv
from database import Database
from extract import download_data_from_api
from transform import create_song_df
from transform import check_if_valid_data

load_dotenv()

if __name__ == "__main__":
    recently_played_songs = download_data_from_api()
    song_df = create_song_df(recently_played_songs)

    try:
        check_if_valid_data(song_df)
    except ValueError as err:
        print(err)

    sql_query = """
    CREATE TABLE IF NOT EXISTS my_played_tracks(
        song_name VARCHAR(200),
        artist_name VARCHAR(200),
        played_at VARCHAR(200),
        timestamp VARCHAR (200),
        CONSTRAINT  primary_key_constraint PRIMARY KEY (played_at)
    )
    """

    database = Database(getenv("DB_NAME"))
    database.create_table(sql_query)

    try:
        song_df.to_sql("my_played_tracks", database.connection, index=False, if_exists='replace')
    except Exception as err:
        print(err)

    database.__del__()
