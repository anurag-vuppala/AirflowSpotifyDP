import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID ="f908f6f5d766436a8b0570af37c4bcb"
CLIENT_SECRET = "f140673ff7424cb599e24cbb8490446c"
REDIRECT_URL = "http://localhost:9090" ## i need a server url here / may be when i make a server in GCS or AWS

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URL,
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])