import s3fs
from credentials import *
import configparser
import json
import pprint
import os

config = configparser.RawConfigParser()
path = os.path.join(os.path.expanduser('~'), '.aws/credentials')
config.read(path)

profile_name = 'wasabi'
profile_type = 'wasabi'

ACCESS_KEY_ID =config.get(profile_name, 'aws_access_key_id')
SECRET_ACCESS_KEY = config.get(profile_name, 'aws_secret_access_key')

if(profile_type == 'wasabi'):
    fs = s3fs.S3FileSystem( key=ACCESS_KEY_ID, secret=SECRET_ACCESS_KEY \
              ,client_kwargs={'endpoint_url':'https://s3.wasabisys.com'})

with fs.open('tweetanalyzer/bitcoin_1630002975.txt', mode='r') as file:
#with open('/Users/srijithraj/Documents/Development/twitter_streaming/local_files/AAPL_1626653527.txt','r') as file:
    data = file.readlines()
    for line in data:
        decoded_data = json.loads(line)
        print(decoded_data['text'])
