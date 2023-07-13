from os import environ
import requests

# good practice to store api creds via environment variables
client_id = environ['TWITCH_CLIENT_ID']
client_secret = environ['TWITCH_CLIENT_SECRET']


def auth_token():
    r = requests.post('https://id.twitch.tv/oauth2/token', data = {'client_id' : client_id, 'client_secret' : client_secret, 'grant_type' : 'client_credentials'})
    print(r.json()['access_token'])
    return r.json()['access_token']

def get_vod():
    payload = {                 # creates query string from these key/values
        'user_id' : 22484632,   # this is forsans id
        'first' : 1             # number of items to return
    }
    headers = {                 # idk the headers are like the verification details n shit (google)
        'Authorization' : 'Bearer ' + auth_token(),
        'Client-Id' : client_id
    }
    r = requests.get('https://api.twitch.tv/helix/videos', headers=headers , params=payload)
    return r.json()

print(get_vod()['data'][0]['title'])