from datetime import timedelta, datetime
from email.policy import default
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import json
from google_sheet_api import update_data_to_sheet
cr = open('cr.json')
crd = json.load(cr)
print(crd['user_id'])



import sqlalchemy
import pandas as pd 
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import sqlite3

def spotify_etl_function():
    DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
    USER_ID =  	crd["user_id"]      # your Spotify username 
    TOKEN = crd["spotify_api_key"] # your Spotify API token
    
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

    print("afskgsfiaufbkabfiaefoa")
    print(song_df)


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
    added_at VARCHAR(200),
    CONSTRAINT primary_key_constraint PRIMARY KEY (added_at)
    )
    """

    cursor.execute(sql_query)
    print("Opened database successfully")

    try:
        song_df.to_sql("my_played_tracks", engine, index=False, if_exists='append')
    except:
        sql = pd.read_sql('SELECT song_name FROM my_played_tracks',conn)
        song_df = song_df[~song_df['song_name'].isin(sql['song_name'])]
        song_df.to_sql("my_played_tracks", conn, index=False, if_exists='append')
        
        print("Data already exists in the database")
        print(" New Songs appended to the existing table")
    

    conn.close()
    print(update_data_to_sheet)
    print("Close database successfully")


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=1),
}

dag = DAG(
    'Spotify_Song_dag',
    default_args=default_args,
    description='A simple songs DAG',
    schedule_interval=timedelta(seconds=15),
    start_date=datetime(2022 , 1, 31),
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