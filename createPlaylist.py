import requests
user_id = '1225602293'
SPOTIFY_CREATE_PLAYLIST_URL = 	'https://api.spotify.com/v1/users/1225602293/playlists'
ACCESS_TOKEN = ''

def create_playlist_on_spotify(name, public):
    response = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json={
            "name": name,
            "public": public
        }
    )
    json_resp = response.json()

    return json_resp

def main():
    playlist = create_playlist_on_spotify(
        name = "My Private Playlist",
        public=False
    )
    print(f"Playlist: {playlist}")

if __name__ == '__main__':
    main()
