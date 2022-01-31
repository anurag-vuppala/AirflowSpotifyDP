from datetime import timedelta, datetime
from email.policy import default
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago




import sqlalchemy
import pandas as pd 
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import sqlite3

def spotify_etl_function():
     # Extract part of the ETL process
     DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
     USER_ID =  	"31c46elir35wdgopjjfnkfilf4ba"       # your Spotify username 
     TOKEN = "BQCzlT2Jleeq-bANmtqgfBTBjc6MZVMbXXmIsb2KNAX-2Curp4cjivnRlvG-uQKJYtf1atS5mGNkZUue0cJdqMQ1JoH4eaGqaBHdZ3IOympFlO9EoVIFBRlzvj9Jspul6mi96x6vNZGC3L8zjw_HtMl8AEiirIQMd4Xh1prKrHWFt-aryVM" # your Spotify API token
 
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

     data = r.json()
     print(data)

     song_names = []
     artist_names = []
     played_at_list = []
     timestamps = []

    # Extracting only the relevant bits of data from the json object      
     for song in data["items"]:
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


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'asdag',
    default_args=default_args,
    description='A simple songs DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2022 , 1, 30),
    catchup = False,
    tags = ['example']
)

def fuction():
    print("Showing  something")

run_etl = PythonOperator(
    task_id='spotify_etl',
    python_callable=spotify_etl_function,
    dag=dag,
)  

run_etl