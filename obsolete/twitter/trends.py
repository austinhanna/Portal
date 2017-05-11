import tweepy
import configparser
cfg = configparser.ConfigParser()

cfg.read('config.ini') # Open Config file to pull Auth codes.
ckey = cfg.get('Auth', 'ckey') # Client Key
csecret = cfg.get('Auth', 'csec') # Client Secret
atoken = cfg.get('Auth', 'atok') # Access Token
asecret = cfg.get('Auth', 'asec') # Access Secret

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

trends1 = api.trends_place(1)
data = trends1[0]
trends = data['trends']
names = [trend['name'] for trend in trends]
trendsName = ' '.join(names).encode('UTF-8')

fo = open('trends.txt','wb')
fo.write(trendsName)
print(trendsName)
