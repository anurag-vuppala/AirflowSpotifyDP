# from googleapiclient.discovery import build
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# import json

# api_key = 'AIzaSyBw89DTYxrWPJdH2mFE0WMDGITHRqFhJDI'

# youtube = build('youtube','v3', developerKey=api_key)

# # request = youtube.channels().list( part='statistics', id='UCkc_R-JFgFnlwzzJJ2AsqZA')

# # request2 = youtube.activities().list( part='statistics', channelId='UCkc_R-JFgFnlwzzJJ2AsqZA')

# request3 = youtube.search().list( part='', channelId='UCkc_R-JFgFnlwzzJJ2AsqZA')

# # responce = request.execute()
# # responce2 = request2.execute()
# responce3 = request3.execute()

# print(json.dumps(responce3))
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "client_secret.json"

# Get credentials and create an API client
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
credentials = flow.run_console()
youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

request = youtube.channels().list( part= 'statistics', id='UCkc_R-JFgFnlwzzJJ2AsqZA')
response = request.execute()

print(response)

