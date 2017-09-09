from flask import Flask, render_template, jsonify, send_from_directory
from collections import Counter
from scroll import getReplies
import requests

app = Flask(__name__)

def call_api(t):
    r = requests.post("https://shl-mp.p.mashape.com/webresources/jammin/emotionV2",
            headers={
                "X-Mashape-Key": "U4ycnCQ53BmshJeIIpfiebCZvomAp1Kk8Y0jsnQGJm0PYu7TyL",
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded"
              },
            data = {
                "lang": "en",
                "text": t
            }
            ).json()
    return r


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_tweet/<tid>')
def get_tweet(tid):
    emotion_counter = Counter()
    print('Getting replies for tid {}'.format(tid))
    replies = getReplies('https://twitter.com/statuses/{}'.format(tid))
    print(replies)
    batch_count = 30
    for reply_batch in range(0, len(replies), batch_count):
        print('Starting batch')
        tweet_text = ''
        for reply_index in range(reply_batch, reply_batch + batch_count):
            if reply_index >= len(replies):
                break
            tweet_text += replies[reply_index] + '\n'

        resp = call_api(tweet_text)
        for group in resp['groups']:
            emotion_counter.update(group['emotions'])
        print(emotion_counter)

    return jsonify(emotion_counter.most_common(10))

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

def main():
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
