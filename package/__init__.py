import os
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))            # this is the project root 
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets') + '/'
VOD_DIR = os.path.join(ROOT_DIR, 'vods') + '/'

# print(os.listdir(ROOT_DIR + '/vods'))
# print(os.listdir(ASSETS_DIR))
print(os.listdir(VOD_DIR))