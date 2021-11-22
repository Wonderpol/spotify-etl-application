from os import getenv
from dotenv import load_dotenv
from service import Service
from extract import get_recently_played_songs
from transform import create_song_df
from transform import check_if_valid_data
from extract import get_top_three_artists
from transform import create_top_artist_df

load_dotenv()

if __name__ == "__main__":
    recently_played_songs = get_recently_played_songs()
    song_df = create_song_df(recently_played_songs)
    top_artist = get_top_three_artists()
    artists_df = create_top_artist_df(top_artist)
    print(artists_df)

    try:
        check_if_valid_data(song_df)
    except ValueError as err:
        print(err)

    sql_query_played_tracks = """
    CREATE TABLE IF NOT EXISTS my_played_tracks(
        song_name VARCHAR(200),
        artist_name VARCHAR(200),
        played_at VARCHAR(200),
        timestamp VARCHAR (200),
        CONSTRAINT  primary_key_constraint PRIMARY KEY (played_at)
    )
    """

    sql_query_top_artists = """
        CREATE TABLE IF NOT EXISTS my_top_three_artists(
            artist_name VARCHAR(200),
            artist_popularity INTEGER,
            artist_genres VARCHAR(200),
            CONSTRAINT  primary_key_constraint PRIMARY KEY (artist_name)
        )
        """

    database = Service(getenv("DB_NAME"))
    database.create_table(sql_query_played_tracks)
    database.create_table(sql_query_top_artists)

    try:
        song_df.to_sql("my_played_tracks", database.connection, index=False, if_exists='replace')
        artists_df.to_sql("my_top_three_artists", database.connection, index=False, if_exists='replace')
    except Exception as err:
        print(err)

    database.__del__()
