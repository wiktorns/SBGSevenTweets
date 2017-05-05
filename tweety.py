from flask import Flask
from flask import request
from storage import Storage
import json

app = Flask(__name__)

_service_name = "Tweety"


@app.route('/tweets', methods=['GET'])
def get_tweets():
    return json.dumps(Storage.get_tweets())


@app.route('/tweets/<int:tweet_id>', methods=['GET', 'DELETE'])
def get_tweet(tweet_id):
    if request.method == 'GET':
        tweet = Storage.get_tweet(tweet_id)
        return json.dumps(tweet) if tweet else 'Not found', 400
    else:
        Storage.remove_tweet(tweet_id)
        return '', 204


@app.route('/tweets', methods=['POST'])
def add_tweet():
    message = request.args.get('tweet', '')
    tweet = Storage.add_tweet(message, _service_name)
    return json.dumps(tweet), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0')
