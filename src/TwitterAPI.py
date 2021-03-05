import flask
from flask import request, jsonify
import tweepy
import json


app = flask.Flask(__name__)
app.config["DEBUG"] = True

CONSUMER_KEY='SQFrh5nI06gW565qIrETKLiCJ'
CONSUMER_SECRET='nllMUUPLTEQrCoLeFnskqz9IoBvZtsFBoRTm36oB21q09nMCM9'
ACCESS_TOKEN_KEY='762316292938280960-dviHDb4jNAuLIRBvXNoGmomfEj9yMbY'
ACCESS_TOKEN_SECRET='7RGb1BJUTpukCKgrcSdSEEnW3lQFkQG53xwmSTjfMOHk3'

auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

@app.route('/twiiter/v1/follow')
def follow_handle():
    data=request.get_json()
    twitter_handles=data['twitter_handle']
    action_status={}
    for twitter_handle in twitter_handles:
        try:
            api.create_friendship(twitter_handle)
            action_status[twitter_handle]="Success"
        except tweepy.TweepError as e:
            action_status[twitter_handle]="Failure"
    return json.dumps(action_status)

@app.route('/twiiter/v1/send_message')
def send_direct_message():
    handle_msg_pair=request.get_json()['data']
    action_status={}
    for data in handle_msg_pair:
        twitter_handle=data['twitter_handle']
        msg=data['message']
        try :
            id1=api.get_user(twitter_handle)._json['id']
            api.send_direct_message(id1,msg)
            action_status[twitter_handle]="Success"
        except tweepy.TweepError as e:
            action_status[twitter_handle]="Failure"

    return json.dumps(action_status)

app.run()