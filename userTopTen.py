import requests
import json
SPOTIFY_TOP_TEN_URL = 	'https://api.spotify.com/v1/me/top/artists'
ACCESS_TOKEN = ''

def top_ten():
    response = requests.get(
        SPOTIFY_TOP_TEN_URL,        #This is how we make a request out to the endpoint url
        # params={'type': 'artists'},
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        }
    )
    json_resp = response.json()

    return json_resp

def main():
    type = 'artists'
    data = top_ten()
    print(f"Top 10:\n")
    rank = 1
    for i in data['items']:
        print("#{} : {}".format(rank, i['name']))
        rank+=1
if __name__ == '__main__':
    main()