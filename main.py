import os
import requests
from dotenv import load_dotenv

#Spotify Credentials
load_dotenv()
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

url_spotify = 'https://accounts.spotify.com/api/token'
header_spotify = {"Content-Type": "application/x-www-form-urlencoded"}
data_spotify = {"grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        }
token_spotify = requests.post(url=url_spotify, headers= header_spotify,data=data_spotify).json()["access_token"]

#Obtaining the list of the tracks
url = "https://api.spotify.com/v1/playlists/1AfNCgOlOc6WaSycqxdOwL/tracks"

header ={"Authorization": "Bearer " + token_spotify}
data = {"fields": "items(track(name,href,album(name,href)))"}
Tracks_result = requests.get(url=url, headers=header).json()
tracks_obtained = list()
while True:
    for track in Tracks_result["items"]:
        name = track["track"]["name"]
        if (len(track["track"]["artists"]) > 0):
            artist = track["track"]["artists"][0]["name"]
        tracks_obtained.append(str(name) + ", " + str(artist)+ "\n")
        print(name)
        print(artist)
        print(" ")

    if Tracks_result["next"] is None:
        break

    else: 
        url_next = Tracks_result["next"]
        Tracks_result = requests.get(url=url_next, headers=header).json()

with open("extracted_spotify_songs.txt", "w", encoding="utf-8") as f:
    f.writelines(tracks_obtained)  


