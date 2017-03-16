# Tweepy Imports #
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time
import configparser

# Config Parser
cfg = configparser.ConfigParser()
# Tweepy #
ckey = 'WEzuoWntc2NqKVg0FSnhlmDNR'
csecret = 'Rq4dcMN9gGo1JWaglibGUDqDLLPFpPkbQOhYlMSaJRfPcIjnuF'
atoken = '1905281930-DWTNXwF3F50Zu5zfbKEvKssuu9ejkbawHN06Tga'
asecret = '2GaOj1TTMGY2ZYEXkOOolZRipIyu9cdB41X5Bkj2W4UkA'

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
