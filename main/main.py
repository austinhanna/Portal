# System Stuff
import sys
import time
import datetime
import os
import configparser
import random
# pyQt stuff #
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
# Tweepy Stuff #
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
# Reddit Stuff #
import praw

## Get if first boot ##
cfg = configparser.ConfigParser()
cfg.read('bin/config.ini')
fboot = cfg.get('General', 'firstboot')
#print(cfg.get('General', 'firstboot')) # Some debug cause this issue took me 10 minutes....

# Reddit Settings #
subreddit = cfg.get('Reddit Module', 'subreddit')

# Twitter Auth Codes #
ckey = cfg.get('Twitter Auth', 'ckey')
csecret = cfg.get('Twitter Auth', 'csec')
atoken = cfg.get('Twitter Auth', 'atok')
asecret = cfg.get('Twitter Auth', 'asec')

class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"].encode('UTF-8')
        username = all_data["user"]["screen_name"].encode('UTF-8')
        time.sleep(1)
        print(username,tweet)
        fo = open("bin/tweet.txt","wb")
        fo.write(username+tweet)
        fo.close()
        return True

    def on_error(self, status):
        print (status)

def rheadline():
    fo = open('bin/headlines.txt','wb')
    reddit = praw.Reddit(user_agent='Portal Reddit Module (by /u/Swagmanhanna)',
                        client_id='9EASNimdp6ItMw', client_secret="cuuiAqw8QCq3f8jDMbU0uV4uLWA")
    for submission in reddit.subreddit(subreddit).hot(limit=10):
        print(submission.title.encode("utf-8")) # Find a way to remove the b'
        fo.write(submission.title.encode("utf-8")+b'\n')
    fo.close()

def startup():
    words = "Loading........"
    for char in words:
        time.sleep(0.3)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("Done!")
    print()
    time.sleep(.6)
    print("Launching")
    main()

def main():
    rheadline()
    def parentmodule():
        app = QtWidgets.QApplication(sys.argv)

        # Create our elements #
        w = QtWidgets.QWidget() # The window

        la1 = QtWidgets.QLabel(w) # Label 1
        tweet = QtWidgets.QLabel(w) # Label "Tweet"
        headline = QtWidgets.QLabel(w) # Label "Reddit"
        la2 = QtWidgets.QLabel(w) # Label "Reddit"

        font = QtGui.QFont() # Make font element
        fontp = QtGui.QPalette()
        font.setFamily("Tahoma") # Set Font
        font.setPointSize(32)
        font.setBold(False) # Bold?

        lt_font = QtGui.QFont() # Make font element
        lt_font.setFamily("Tahoma") # Set Font
        lt_font.setPointSize(16)
        lt_font.setBold(False) # Bold?

        la1.setFont(font)
        la2.setFont(font)
        tweet.setFont(lt_font)
        headline.setFont(lt_font)

        fontp.setColor(QtGui.QPalette.Foreground,QtCore.Qt.white) # Label Color
        la1.setPalette(fontp) # Set label to palette
        la2.setPalette(fontp) # Set label to palette
        tweet.setPalette(fontp) # Set label to palette
        headline.setPalette(fontp) # Set label to palette

        la1.move(10,10)
        la2.move(10,100)
        tweet.move(860,1000)
        headline.move(10,1000)
        tweet.setGeometry(0,750,1920,500)
        headline.setGeometry(0,0,1920,500)
        la1.setText("Hello")
        la2.setText("there.")
        w.setWindowTitle("Main") # Set window title text

        # Color #
        w.setAutoFillBackground(True) # Fill
        p = w.palette() # Make P palette for window and color options
        p.setColor(w.backgroundRole(), Qt.black) # Set window color
        w.setPalette(p) #
        w.show()
        #os.system("cd Twitter")
        #os.system("python streaming.py 1")
        w.showFullScreen() # Make window fullscreen

        def update_label():
            #with open('bin/headlines.txt', 'r',encoding="utf-8") as headline_file:

                #reddit_content = headline_file.read()
            with open('bin/tweet.txt', 'r',encoding="utf8") as tweet_file:
                tweet_content = tweet_file.read()
            current_time = str(datetime.datetime.now().time())
            tweet.setText(tweet_content) # Split this! Add @ and says.
            reddit_content = random.choice([f for f in open('bin/headlines.txt')])
            headline.setText(reddit_content)
        timer = QtCore.QTimer()
        timer.timeout.connect(update_label)
        timer.start(10000)  # Check for new tweet/headline every second
        sys.exit(app.exec_())
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        cfg.read('bin/config.ini')
        keyword = cfg.get('Twitter Module','keyword')
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=[keyword])
        print("Main Launched")
    parentmodule()

# Launch Control #
if fboot == 'Enable':
    print("This is the first boot! Running Setup.py...")
    time.sleep(1)
    print()
    os.system('python setup.py 1')
elif fboot == 'Disable':
    print("Not first boot.. Loading settings. ")
    print()
    time.sleep(1)
    startup()
else:
    print("Corrupted!!!")
    time.sleep(1)
    print("Something broke in the code. Try running the setup again.")
# # # # # # # # # # #
