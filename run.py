
import pandas as pd




''' 
A spreadsheet containing raw run data only, can fill with aggregations later (avg times of all cols, etc...)
'''
cols = [
    'video_url', 
    'date',
    'timestamp',
    'reset_time', 
    'nether_entry',
    'found_bastion',
    'found_fortress',
    'nether_exit',
    'stronghold_entry',
    'end_entry',
    'dragon_kill',
    'elasped_time',
]

df = pd.DataFrame(columns=cols)
sample_row = ['Videos/12321321', '07/18/23', '03:23:05', '15:38', '05:01', '07:48', '11:43'	,'13:01', '15:54', '16:07',	'18:03'	,'18:12']
df.loc[0] = sample_row      # add a new row starting at index 0


# convert time cols to pandas datetime obj type

df['date'] = pd.to_datetime(df['date'])   
df['timestamp'] = pd.to_datetime(df['timestamp'], format = '%H:%M:%S')

# for cols that track timer 
for col in df.columns.values[3:]:
    print(df.columns.values)
    df[col] = pd.to_datetime(df[col], format = '%M:%S')

print(df.dtypes)



