import os
import requests
import subprocess

# good practice to store api creds via environment variables
client_id = os.environ['TWITCH_CLIENT_ID']
client_secret = os.environ['TWITCH_CLIENT_SECRET']


def auth_token():
    r = requests.post('https://id.twitch.tv/oauth2/token', data = {'client_id' : client_id, 'client_secret' : client_secret, 'grant_type' : 'client_credentials'})
    return r.json()['access_token']

def get_vod(* , latest = 1) -> list[str]:
    payload = {                      # creates query string from these key/values
        'user_id' : 22484632,        # this is forsans id
        'first' : latest             # number of items to return
    }
    headers = {                 # idk the headers are like the verification details n shit (google)
        'Authorization' : 'Bearer ' + auth_token(),
        'Client-Id' : client_id
    }
    r = requests.get('https://api.twitch.tv/helix/videos', headers=headers , params=payload)
    print(r.json())





    vod_id = [] 

    for vod in r.json()['data']:        # {'data': [{vod_info}], [{vod_info1}]}
        nums = [char for char in vod['url'] if char.isdigit()]              # extract id
        vod_id.append(''.join(nums))

    print(vod_id)
    return vod_id


def download_vod(id, *, start: int, end: int, name = None):      # usage: TwitchDownloaderCLI.exe videodownload --id <vod-id-here> -o <name>.mp4
    '''
    -b : Time in seconds to crop beginning. 
    -e : Time in seconds to crop ending.s
    -q : quality 1080p60, 720p60 ...
    '''
    name = str(id) if (name is None) else name
    current_dir = os.path.dirname(os.path.realpath(__file__))
    save_dir = current_dir + "\\vods"                                # the path where the vods get saved

    # command = current_dir + '\TwitchDownloaderCLI.exe videodownload --id %d -b %d -e %d --quality 720p60 -o vods/%s.mp4' % (id, start, end, name)
    command = current_dir + f'\TwitchDownloaderCLI.exe videodownload --id {id} -b {start} -e {end} --quality 720p60 -o {save_dir}\{name}.mp4'

    print(command)
    print("Downloading vod...")
    
    subprocess.run(command.split(" "), shell=True)

    # check if there is a file at that path
    if not os.path.isfile(f'vods/{name}.mp4'):
        raise Exception("could not download vod :(")



# download_vod(1871917822, start=23000, end = 24000, name='test')
# download_vod(get_vod_id()[0], start = 1000, end = 2000)
get_vod()
