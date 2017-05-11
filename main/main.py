# System Stuff
import sys
import time
import datetime
import os
import configparser
import random
import requests
# pyQt stuff #
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtGui import QPixmap

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

# User Data #
u_name = cfg.get('User Data', 'name')

# Weather Settings #
city = cfg.get('Weather Module', 'city_name')
#unit = cfg.get('Weather Module', 'unit')
wth_api = cfg.get('Weather Module', 'apikey')

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
    words = "Loading Settings"
    for char in words:
        time.sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print("Grabbing Reddit Data")
    rheadline()
    #print("Grabbing Twitter Data")
    #rheadline()
    #print("Grabbing Weather Data")
    #rheadline()
    dottt = "..........."
    for char in dottt:
        time.sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("Done!")
    print()
    print("Launching into GUI...")
    time.sleep(1)
    main()

def main():
    def parentmodule():
        app = QtWidgets.QApplication(sys.argv)

        # Create our elements #
        w = QtWidgets.QWidget() # The window

        la1 = QtWidgets.QLabel(w) # Label 1
        tweet = QtWidgets.QLabel(w) # Label "Tweet"
        headline = QtWidgets.QLabel(w) # Label "Reddit"
        la2 = QtWidgets.QLabel(w) # Label "Reddit"
        time_la = QtWidgets.QLabel(w) # Label "Time"

        weather_city = QtWidgets.QLabel(w)
        weather_temp = QtWidgets.QLabel(w)
        weather_humid = QtWidgets.QLabel(w)
        weather_desc = QtWidgets.QLabel(w)

        oImage = QImage("rsc/climacons/Cloud.png")
        sImage = oImage.scaled(QSize(300,200))                   # resize Image to widgets size

        font = QtGui.QFont() # Make font element
        fontp = QtGui.QPalette()
        font.setFamily("Tahoma") # Set Font
        font.setPointSize(30)
        font.setBold(False) # Bold?

        font2 = QtGui.QFont() # Make font element
        font2.setFamily("Tahoma") # Set Font
        font2.setPointSize(24)
        font2.setBold(False) # Bold?

        lt_font = QtGui.QFont() # Make font element
        lt_font.setFamily("Tahoma") # Set Font
        lt_font.setPointSize(16)
        lt_font.setBold(False) # Bold?

        la1.setFont(font)
        la2.setFont(font2)
        tweet.setFont(lt_font)
        headline.setFont(lt_font)
        time_la.setFont(lt_font)
        weather_city.setFont(lt_font)
        weather_temp.setFont(lt_font)
        weather_humid.setFont(lt_font)
        weather_desc.setFont(lt_font)

        fontp.setColor(QtGui.QPalette.Foreground,QtCore.Qt.white) # Label Color
        la1.setPalette(fontp) # Set label to palette
        la2.setPalette(fontp) # Set label to palette
        tweet.setPalette(fontp) # Set label to palette
        headline.setPalette(fontp) # Set label to palette
        time_la.setPalette(fontp)

        weather_city.setPalette(fontp)
        weather_temp.setPalette(fontp)
        weather_humid.setPalette(fontp)
        weather_desc.setPalette(fontp)

        la1.move(10,10)
        la2.move(10,100)
        tweet.move(860,1000)
        tweet.setGeometry(0,750,1920,500)
        headline.setGeometry(10,800,1920,500)
        time_la.setGeometry(700,0,1920,100)

        weather_city.setGeometry(1400,5,1920,100)
        weather_temp.setGeometry(1400,45,1920,100)
        weather_humid.setGeometry(1600,5,1920,100)
        weather_desc.setGeometry(1600,45,1920,100)

        la1.setText("Welcome,")
        la2.setText(u_name)
        w.setWindowTitle("Main") # Set window title text

        def time():
            time_la.setText(QtCore.QDateTime.currentDateTime().toString())
        time_timer = QtCore.QTimer()
        time_timer.timeout.connect(time)
        time_timer.start(500)  # Check for new tweet/headline every second

        # Color #
        w.setAutoFillBackground(True) # Fill
        p = w.palette() # Make P palette for window and color options
        p.setColor(w.backgroundRole(), Qt.black) # Set window color
        w.setPalette(p) #
        w.show()
        #os.system("cd Twitter")
        #os.system("python streaming.py 1")
        w.showFullScreen() # Make window fullscreen
        headline.setText("Loading..")

        url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+wth_api
        data = requests.get(url)
        read = data.json()

        weather_city.setText(read['name'])
        weather_temp.setText(str(read['main']['temp']-273.15)+'°C')
        weather_humid.setText(str(read['main']['humidity'])+'%')
        weather_desc.setText(read['weather'][0]['description'])

        """
        def weather():
            # add checks for weather Module
            url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+wth_api
            data = requests.get(url)
            read = data.json()

            weather_city.setText(read['name'])
            weather_temp.setText(str(read['main']['temp']-273.15))
            weather_humid.setText(read['main']['humidity'])
            weather_desc.setText(read['weather'][0]['description'])
        weath_timer = QtCore.QTimer()
        weath_timer.timeout.connect(weather)
        weath_timer.start(3600000) # 1 Hour
        """

        def update_label():
            #with open('bin/headlines.txt', 'r',encoding="utf-8") as headline_file:

                #reddit_content = headline_file.read()
            with open('bin/tweet.txt', 'r',encoding="utf8") as tweet_file:
                tweet_content = tweet_file.read()
            current_time = str(datetime.datetime.now().time())
            #tweet.setText(tweet_content) # Split this! Add @ and says.
            reddit_content = random.choice([f for f in open('bin/headlines.txt')])
            headline.setText("/r/"+subreddit+": "+reddit_content)
        timer = QtCore.QTimer()
        timer.timeout.connect(update_label)
        timer.start(5000)  # Check for new tweet/headline every 5 seconds
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
