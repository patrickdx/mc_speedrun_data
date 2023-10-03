
import pandas as pd
import sys
import time
from package.vision.run import Run
from run import logger 

''' 
A spreadsheet containing raw run data only, can fill with aggregations later (avg times of all cols, etc...)
'''
# https://stackoverflow.com/questions/13331518/how-to-add-a-single-item-to-a-pandas-series

def period():        # returns a generator object        
    animation = ['.  ','.. ','...']
    count = 0
    while True:
        yield animation[count]
        count += 1
        count = count % 3 


def progress(current, total, animation = period(), status=''):      # question is what to base progress of? percentage of vod? percentage of run?
    current, total = int(current), int(total)
    bar_len = 60                        # 60 chars long
    filled = current / total            # actual progress percentage
    filledBars = '=' * round(bar_len * filled)  # 9.6 -> 10 bars 
    rest = '-' * (bar_len - len(filledBars))
    sys.stdout.write("[%s] %s %s/%s %s\r" % (filledBars + rest, status, current, total, next(animation)))  

# for i in range(1,101):
#     progress(i,100, status = 'generating god seed')
#     time.sleep(0.5)


# t=3h30m38s
def get_vod_timestamp(currFrame: int, fps = 60, offset = 0):      # how much frames/time was skipped from the beginning of vod 
    secs = (currFrame + offset) / fps      
    mins, secs = divmod(secs, 60)     # quotient , remainder
    hrs, mins = divmod(mins, 60)
    
    print(hrs,mins,secs)
    return '%dh%dm%ds' % (hrs, mins, secs)

def get_current_date():
    from datetime import date 
    return str(date.today())


























dict = {
    'id': [],
    'video_id' : [],        # video + timestamp (expiry date 60 days?)
    'date' : [], 
    'nether_entry': [],
    'bastion': [],
    'fortress': [],
    'nether_exit': [],
    'stronghold': [],
    'end': [], 
    'elasped_time': []
}

id_count = 1 

# create record off run data 
def save(run : Run):
    dict['id'] = id_count
    dict['video_id'] = VOD_URL + get_vod_timestamp()

    for event in run.events:
        dict[str(event)].append(event.time)      # there might be nothing 

    
    id_count += 1

    str = []

    # log latest row 
    for list in dict.values():
        str.append(list[-1])
    


# convert dict to df 
values = list(dict.values())
assert all(len(col) == len(values[0]) for col in values), 'columns are not all same length...'

df = pd.DataFrame(dict)   
df.to_csv('raw_data.csv') 

