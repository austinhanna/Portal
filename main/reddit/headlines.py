import praw
import configparser
import os

cfg = configparser.ConfigParser()
os.chdir("..") # Put us up into the main area to access bin for configs
cfg.read('bin/config.ini')
subreddit = cfg.get('Reddit Module', 'subreddit')

fo = open('bin/headlines.txt','wb')

reddit = praw.Reddit(user_agent='Portal Reddit Module (by /u/Swagmanhanna)',
                     client_id='9EASNimdp6ItMw', client_secret="cuuiAqw8QCq3f8jDMbU0uV4uLWA")
for submission in reddit.subreddit(subreddit).hot(limit=10):
    print(submission.title.encode("utf-8")) # Find a way to remove the b'
    fo.write(submission.title.encode("utf-8"))
fo.close()
