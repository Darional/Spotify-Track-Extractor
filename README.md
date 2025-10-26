# Spotify Track Extractor

A simple Python script that retrieves all tracks from a Spotify playlist and saves them to a `.txt` file.
This version outputs only the song name and the artist name per line.

## Features

- Fetches all tracks from any public (or private, with proper permissions) Spotify playlist.
- Outputs only: Song Name, Artist Name.
- Handles large playlists via automatic pagination.
- Uses environment variables to keep credentials out of source control.

## Requirements

- Python 3.8+
- A Spotify account
- A Spotify access token with playlist-read-private if exporting private playlists

## Installation

1. Clone this repository:
```
   git clone https://github.com/yourusername/spotify-track-extractor.git
   cd spotify-track-extractor
```
2. (Optional) Create and activate a virtual environment:
```
   python -m venv venv
   source venv/bin/activate    # macOS / Linux
   venv\\Scripts\\activate       # Windows
```
3. Install dependencies:
```
   pip install -r requirements.txt
```
4. Create a .env file in the project root and add your 
   
client id and secret:
```
   client_id="51b651ba2a3s1r8g18198njdkjfe00"
   client_secret="51b651ba2a3s1r8g18198njdkjfe00"
```
   Make sure .env is listed in .gitignore.
   To get the client and secret, you need to:
    
   - Visit: https://developer.spotify.com/dashboard
   - Log in and click on the button ```Create App```
   - Fill the form and mark in ```APIs Used``` as Web API
   - Then you can click into you App the ```Client ID``` and ```Client Secret```
   - Copy them and paste it into the .env 

## Usage

1. Open main.py and set the playlist ID you want to export. The playlist ID is the part after /playlist/ in a Spotify link. For example, for the playlist: 

    ```https://open.spotify.com/intl-es/album/6NnOcPG7uLUSpJTS83Ra1T?si=389a08d1cd034fb9```

   The playlist ID is: ```6NnOcPG7uLUSpJTS83Ra1T```
   > Paste it into ```url = "https://api.spotify.com/v1/playlists/paste_it_here_your_playlist_ID/tracks"```
2. Run the script:
   python main.py

3. The script writes tracks.txt with one line per track:
   Song Name – Artist Name

## Example output

Blinding Lights, The Weeknd

Levitating, Dua Lipa

As It Was, Harry Styles

Viva La Vida, Coldplay

## Dependencies

- requests
- python-dotenv

Install manually if needed:
   pip install requests python-dotenv

## Project structure

spotify-track-extractor/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

## License

MIT License.