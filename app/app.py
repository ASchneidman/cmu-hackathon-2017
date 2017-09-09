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
<<<<<<< HEAD
    replies = ['Churches in Texas should be entitled to reimbursement from FEMA Relief Funds for helping victims of Hurricane Harvey (just like others).']
    batch_count = 100
=======
    print('Getting replies for tid {}'.format(tid))
    replies = getReplies('https://twitter.com/statuses/{}'.format(tid))
    print(replies)
    batch_count = 30
>>>>>>> 7cdecd0e4f529ea09fe9d035de86b8eed2cb5950
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
