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
TOKEN = "BQDDiws2MHFrd6KtWbtPOQLhim3sNiktiyD63LxIoz7Ji7QRdaZJw0PNN2EwNZjAIQ5TqTKkJs2DbbXqTA5AXsVl4l34Nb4XojEA_TaDwX34ty3FwICnHj5-GVO3lraT8yWptvO90xxYXStzoY8cS4NQsuTPw__fTmeEjgw6FB_bvvbqaiWOWDY7dJcG3A" # your Spotify API token
 
headers = {
    "Accept" : "application/json",
    "Content-Type" : "application/json",
    "Authorization" : "Bearer {token}".format(token=TOKEN)
    }
    
    # Convert time to Unix timestamp in miliseconds      
today = datetime.now()
yesterday = today - timedelta(days=1)
yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

# Download all songs you've listened to "after yesterday", which means in the last 24 hours      
r = requests.get("https://api.spotify.com/v1/anurag/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers = headers)

# a = ("time is {time}".format(time=yesterday_unix_timestamp), headers = headers))

data = r.json()
print(11112132312312312312312)
print(data)
print(11112132312312312312312)

song_names = []
artist_names = []
played_at_list = []
timestamps = []

# Extracting only the relevant bits of data from the json object      
for song in data["artists"]:
    song_names.append(song["track"]["name"])
    artist_names.append(song["track"]["album"]["artists"][0]["name"])
    played_at_list.append(song["played_at"])
    timestamps.append(song["played_at"][0:10])

# Prepare a dictionary in order to turn it into a pandas dataframe below       
song_dict = {
    "song_name" : song_names,
    "artist_name": artist_names,
    "played_at" : played_at_list,
    "timestamp" : timestamps
}

song_df = pd.DataFrame(song_dict, columns = ["song_name", "artist_name", "played_at", "timestamp"])
print(111111111111111111111000000000000000000000)

print(song_df)

print(111111111111111111111000000000000000000000)
#  # Validate
#   if check_if_valid_data(song_df):
#      print("Data valid, proceed to Load stage")

# Load

engine = sqlalchemy.create_engine(DATABASE_LOCATION)
conn = sqlite3.connect('my_played_tracks.sqlite')
cursor = conn.cursor()

sql_query = """
CREATE TABLE IF NOT EXISTS my_played_tracks(
song_name VARCHAR(200),
artist_name VARCHAR(200),
played_at VARCHAR(200),
timestamp VARCHAR(200),
CONSTRAINT primary_key_constraint PRIMARY KEY (played_at)
)
"""

cursor.execute(sql_query)
print("Opened database successfully")

try:
    song_df.to_sql("my_played_tracks", engine, index=False, if_exists='append')
except:
    print("Data already exists in the database")

conn.close()
print("Close database successfully")