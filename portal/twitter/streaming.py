import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'WEzuoWntc2NqKVg0FSnhlmDNR'
csec = 'Rq4dcMN9gGo1JWaglibGUDqDLLPFpPkbQOhYlMSaJRfPcIjnuF'
atoken = '1905281930-DWTNXwF3F50Zu5zfbKEvKssuu9ejkbawHN06Tga'
asec = '2GaOj1TTMGY2ZYEXkOOolZRipIyu9cdB41X5Bkj2W4UkA'

class listener(StreamListener):
    def on_data(self, data):
        try:
            #print(data)
            tweet = data.split(',"text":"')[1].split('","source')[0]
            print(tweet)
            return True
        except BaseException:
            print(str(e))
            time.sleep(5)
    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csec)
auth.set_access_token(atoken, asec)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=['Car'])
