# Tweepy Imports #
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time
import configparser

# Config Parser
cfg = configparser.ConfigParser()

# Twitter Auth Codes #
cfg.read('config.ini')
ckey = cfg.get('auth', 'ckey')
csecret = cfg.get('auth', 'csec')
atoken = cfg.get('auth', 'atok')
asecret = cfg.get('auth', 'asec')

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"].encode('UTF-8')

        username = all_data["user"]["screen_name"].encode('UTF-8')

        time.sleep(3)
        print(username,tweet)
        fo = open("tweet.txt","wb")
        fo.write(username+tweet)
        fo.close()

        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

cfg.read('config.ini')
keyword = cfg.get('General','keyword')
twitterStream = Stream(auth, listener())
twitterStream.filter(track=[keyword])
