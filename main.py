import os
import requests
import subprocess
from vod import Vod
import argparse

# good practice to store api creds via environment variables
client_id = os.environ['twitch_client_id']
client_secret = os.environ['twitch_client_secret']


def auth_token():
    r = requests.post('https://id.twitch.tv/oauth2/token', data = {'client_id' : client_id, 'client_secret' : client_secret, 'grant_type' : 'client_credentials'})
    return r.json()['access_token']

def get_vod(id, *, latest = 1) -> list[str]:
    '''
    Gets and returns a list of x latest vods from streamer    
    '''

    payload = {                      # creates query string from these key/values
        'user_id' : id,        # this is forsans id
        'first' : latest             # number of items to return
    }
    headers = {                 # idk the headers are like the verification details n shit (google)
        'Authorization' : 'Bearer ' + auth_token(),
        'Client-Id' : client_id
    }
    r = requests.get('https://api.twitch.tv/helix/videos', headers=headers , params=payload)

    vod_data = []

    for vod_json in r.json()['data']:
        vod_data.append(Vod(vod_json))

    return vod_data



def download_vod(id, *, start: int, end: int, name = None):      # usage: TwitchDownloaderCLI.exe videodownload --id <vod-id-here> -o <name>.mp4
    '''
    -b : Time in seconds to crop beginning. 
    -e : Time in seconds to crop ending.s
    -q : quality 1080p60, 720p60 ...
    '''
    name = str(id) if (name is None) else name
    save_dir = "vods"                                # the path where the vods get saved

    command = f'TwitchDownloaderCLI.exe videodownload --id {id} -b {start} -e {end} --quality 720p60 -o {save_dir}\{name}.mp4'

    print(command)
    print("Downloading vod...")
    
    subprocess.run(command.split(" "), shell=True)          # this gets run at the project root

    # check if there is a file at that path
    if not os.path.isfile(f'vods/{name}.mp4'):
        raise Exception("could not download vod :(")

def _time_format(time : str) -> int:  
    '''converts HH:MM:SS to seconds'''
    times = time.split(':')
    hrs = int(times[0])
    mins = int(times[1])
    secs = int(times[2])

    return (hrs*60*60) + (mins*60) + secs

    
# if __name__ == '__main__():':       # executes code When the this file is run as a script i.e. python main.py, but not when its imported as a module
#     '''
#     analyzes the first 
#     '''

#     forsen_id = 22484632
#     parser = argparse.ArgumentParser(description= 'downloads some vods from some streamer')
#     parser.add_argument("")
#     parser.add_argument





download_vod('1889111156', start= 3600, end = 3700)

# download_vod('1879662076', start = 2000, end = 10000)



