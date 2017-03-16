import tweepy
import configparser
cfg = configparser.ConfigParser()

cfg.read('config.ini')
ckey = cfg.get('Auth', 'ckey')
csecret = cfg.get('Auth', 'csec')
atoken = cfg.get('Auth', 'atok')
asecret = cfg.get('Auth', 'asec')

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
trends1 = api.trends_place(1) # from the end of your code
# trends1 is a list with only one element in it, which is a
# dict which we'll put in data.
data = trends1[0]
# grab the trends
trends = data['trends']
# grab the name from each trend
names = [trend['name'] for trend in trends]
# put all the names together with a ' ' separating them
trendsName = ' '.join(names).encode('UTF-8')

fo = open('trends.txt','wb')
fo.write(trendsName)
print(trendsName)
