from flask import Flask, render_template, request, jsonify
import pandas
from textblob import TextBlob

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
    return(file)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
