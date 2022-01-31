from pendulum import time
import sqlalchemy
import pandas as pd 
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime, timedelta

import sqlite3

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
USER_ID =  	"31c46elir35wdgopjjfnkfilf4ba"       # your Spotify username 
TOKEN = "BQCPXjcjdDSNISFHFQxZFG16bCLbcczzNowgabQsaFVeK6sNdd2PNE8ZHsBcQzV4z8w29olTW0uAv156deNjq_DSO3yF-d_cZ7MvjPG1FnJyM3Fec7XoFlkrPVAeB6AHA7O5bhkP1sEKkocZ6HUSrNwhcGZm8JVsgMfnfpehpT_CyWjrPVR9tGvl04ZwnQ" # your Spotify API token
 
headers = {
    "Accept" : "application/json",
    "Content-Type" : "application/json",
    "Authorization" : "Bearer {token}".format(token=TOKEN)
    }
    
    # Convert time to Unix timestamp in miliseconds      
today = datetime.now()
yesterday = today - timedelta(days=1)
yesterday_unix_timestamp = int(today.timestamp()) * 1000

# Download all songs you've listened to "after yesterday", which means in the last 24 hours   
r = requests.get("https://api.spotify.com/v1/me/tracks?market=us", headers=headers)


data = r.json()


song_names = []
artist_names = []
played_at_list = []


# Extracting only the relevant bits of data from the json object      
for song in data["items"]:
    print(song)
    song_names.append(song["track"]["name"])
    artist_names.append(song["track"]["album"]["artists"][0]["name"])
    played_at_list.append(song["added_at"])
    

# Prepare a dictionary in order to turn it into a pandas dataframe below       
song_dict = {
    "song_name" : song_names,
    "artist_name": artist_names,
    "added_at" : played_at_list,
    
}

song_df = pd.DataFrame(song_dict, columns = ["song_name", "artist_name", "added_at"])


print(song_df)


#  # Validate
#   if check_if_valid_data(song_df):
#      print("Data valid, proceed to Load stage")

# Load

# engine = sqlalchemy.create_engine(DATABASE_LOCATION)
# conn = sqlite3.connect('my_played_tracks.sqlite')
# cursor = conn.cursor()

# sql_query = """
# CREATE TABLE IF NOT EXISTS my_played_tracks(
# song_name VARCHAR(200),
# artist_name VARCHAR(200),
# added_at VARCHAR(200),
# CONSTRAINT primary_key_constraint PRIMARY KEY (aded_at)
# )
# """

# cursor.execute(sql_query)
# print("Opened database successfully")

# try:
#     song_df.to_sql("my_played_tracks", engine, index=False, if_exists='append')
# except:
#     print("Data already exists in the database")

# conn.close()
# print("Close database successfully")
