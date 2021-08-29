from flask import Flask, render_template, request, jsonify
import pandas
from textblob import TextBlob
import s3fs
import configparser
import json
import os

app = Flask(__name__)

@app.route('/')
@app.route('/sentiment', methods=['POST'])
def hello(name=None):
    jsondata = request.get_json(force=False)
    testimonial = TextBlob(jsondata['text'])
    return(jsondata['text'] + ' ---    ' + str(testimonial.sentiment.polarity))

@app.route('/files', methods=['POST'])
def process_files(name=None):
    jsondata = request.get_json(force=False)
    file = jsondata['filename']

    print("filename -- ",file)
    profile_name = 'wasabi'
    profile_type = 'wasabi'

    #ACCESS_KEY_ID =config.get(profile_name, 'aws_access_key_id')
    #SECRET_ACCESS_KEY = config.get(profile_name, 'aws_secret_access_key')
    ACCESS_KEY_ID = os.environ.get('aws_access_key_id')
    SECRET_ACCESS_KEY = os.environ.get('aws_secret_access_key')

    if(profile_type == 'wasabi'):
        fs = s3fs.S3FileSystem( key=ACCESS_KEY_ID, secret=SECRET_ACCESS_KEY \
                  ,client_kwargs={'endpoint_url':'https://s3.wasabisys.com'})

    text = []
    with fs.open('tweetanalyzer/' + file, mode='r') as f:
    #with open('/Users/srijithraj/Documents/Development/twitter_streaming/local_files/AAPL_1626653527.txt','r') as file:
        data = f.readlines()
        for line in data:
            decoded_data = json.loads(line)
            testimonial = TextBlob(decoded_data['text'])
            text.append(decoded_data['text'] + ' --- ' + str(testimonial.sentiment.polarity))


    with fs.open('tweetanalyzerres/' + file, mode='w') as file:
                file.write(str(text))

    return(str(text))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
