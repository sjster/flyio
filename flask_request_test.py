import requests
import json

# This assumes that you have the flask server running locally om port 5000
headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}
url = 'http://127.0.0.1:5000/sentiment'
r = requests.post(url, data=json.dumps({'file': 'filename.txt', 'text': 'At @nongmoreport yes! we plan to repost it to all our social channels'}), headers=headers)

r = requests.post('https://spring-silence-4034.fly.dev/files', data=json.dumps({'filename': 'tweetanalyzer/bitcoin_1630002975.txt'}), headers=headers)
