# System Stuff #
import sys
import time
import datetime
import os
import configparser
import random
import requests
import textwrap

# pyQt stuff #
from PyQt5 import QtWidgets, QtGui
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

# Import CFG file #
cfg = configparser.ConfigParser()
cfg.read('bin/config.ini')

# General Data #
fboot = cfg.get('General','firstboot')

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
unit = cfg.get('Weather Module', 'units')
wth_api = cfg.get('Weather Module', 'apikey')


# Logging #
now = datetime.datetime.now()
tyme = now.strftime("%H-%M-%S")
lo = open("bin/logs/log_"+now.strftime("%Y-%m-%d-%H-%M")+".txt",'w')
lo.close()
lo = open("bin/logs/log_"+now.strftime("%Y-%m-%d-%H-%M")+".txt",'a')

# Stream isn't workin' fella... find a way to put the class into the thingo below.
class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"].encode('UTF-8')
        username = all_data["user"]["screen_name"].encode('UTF-8')
        time.sleep(1)
        print(username,tweet)
        fo = open("bin/tweet.txt","wb")
        fo.write('@'+username+tweet)
        fo.close()
        return True

    def on_error(self, status):
        print (status)

def rheadline():
    lo.write("["+tyme+"]: "+"Gathering Reddit Data (First Time)\n")
    fo = open('bin/headlines.txt','wb')
    reddit = praw.Reddit(user_agent='Portal Reddit Module (by /u/Swagmanhanna)',
                        client_id='9EASNimdp6ItMw', client_secret="cuuiAqw8QCq3f8jDMbU0uV4uLWA")
    for submission in reddit.subreddit(subreddit).hot(limit=10):
        fo.write(submission.title.encode("utf-8")+b'\n')
    print("Done with Reddit!")
    lo.write("["+tyme+"]: "+"Gathered Successfully.\n")
    fo.close()

def startup():
    lo.write("\n")
    lo.write("["+tyme+"]: "+"STARTUP MODULE\n")
    lo.write("["+tyme+"]: "+"Initializing..\n")
    words = "Loading Settings"
    for char in words:
        time.sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print("Grabbing Reddit Data...")
    rheadline()
    dottt = "..........."
    for char in dottt:
        time.sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("Done!")
    lo.write("["+tyme+"]: "+"Gathered all Data successfully.\n")
    print()
    lo.write("["+tyme+"]: "+"Launching into GUI...\n")
    print("Launching into GUI...")
    time.sleep(1)
    main()

def main():
    def parentmodule():
        lo.write("\n")
        lo.write("["+tyme+"]: "+"MAIN MODULE.\n")
        lo.write("["+tyme+"]: "+"Setting all variables.\n")
        app = QtWidgets.QApplication(sys.argv)

        # Create our elements #
        w = QtWidgets.QWidget() # The window

        # Labels hold text and can also show us images. How cool!
        tweet = QtWidgets.QLabel(w) # Label - "Tweet"
        headline = QtWidgets.QLabel(w) # Label - "Reddit"
        la2 = QtWidgets.QLabel(w) # Label - "Reddit"
        time_time = QtWidgets.QLabel(w) # Label - "Time"
        time_time_s = QtWidgets.QLabel(w) # Label - "Time, Seconds"
        time_day = QtWidgets.QLabel(w) # Label - "Day"
        time_date = QtWidgets.QLabel(w) # Label - ""
        wth_dsc_img = QtWidgets.QLabel(w) # Image - Weather Icon
        snoo_img = QtWidgets.QLabel(w) # Image - Reddit Icon
        weather_city = QtWidgets.QLabel(w) # Label - "Weather/City Name"
        weather_temp = QtWidgets.QLabel(w) # Label - "Weather/Temperature"
        weather_humid = QtWidgets.QLabel(w) # Label - "Weather/Humidity"
        wth_tmp_img = QtWidgets.QLabel(w) # Label - "Weather/Thermometer Image"

        font = QtGui.QFont() # Make font element
        fontp = QtGui.QPalette() # Make new pallete for the first font
        font.setFamily("Helvetica") # Set Font
        font.setPointSize(26) # Set font size
        font.setBold(False) # Bold? No way Jose

        font2 = QtGui.QFont() # Make font element
        font2.setFamily("Helvetica") # Set Font
        font2.setPointSize(64) # Set font size
        font2.setBold(False) # Nope.

        font3 = QtGui.QFont() # Make font element
        font3.setFamily("Helvetica") # Set Font
        font3.setPointSize(32) # Set font size
        font3.setBold(False) # Nope.

        font4 = QtGui.QFont() # Make font element
        font4.setFamily("Helvetica") # Set Font
        font4.setPointSize(12) # Set font size
        font4.setBold(False) # Nope.

        lt_font = QtGui.QFont() # Make font element
        lt_font.setFamily("Helvetica") # Set Font
        lt_font.setPointSize(16) # Set font size
        lt_font.setBold(False) # Nah.

        # Set labels to fonts.
        la1 = QtWidgets.QLabel(w) # Label - "Welcome"
        la2.setFont(font)
        tweet.setFont(lt_font)
        headline.setFont(font4)
        time_time.setFont(font2)
        time_time_s.setFont(lt_font)
        time_day.setFont(font3)
        time_date.setFont(lt_font)
        weather_city.setFont(lt_font)
        weather_temp.setFont(lt_font)
        weather_humid.setFont(lt_font)

        # Set labels to pallete's
        fontp.setColor(QtGui.QPalette.Foreground,QtCore.Qt.white) # Label Color
        la2.setPalette(fontp) # Set label to palette
        tweet.setPalette(fontp) # Set label to palette
        headline.setPalette(fontp) # Set label to palette
        time_time.setPalette(fontp)
        time_time_s.setPalette(fontp)
        time_day.setPalette(fontp)
        time_date.setPalette(fontp)
        weather_city.setPalette(fontp)
        weather_temp.setPalette(fontp)
        weather_humid.setPalette(fontp)

        # Geometry!
        la2.setGeometry(10,50,1920,100)
        tweet.move(860,1000)
        tweet.setGeometry(0,750,1920,500)
        headline.setGeometry(600,50,1920,500)
        time_time.setGeometry(600,10,1080,120)
        time_time_s.setGeometry(950,0,1080,120)
        time_day.setGeometry(605,125,1080,80)
        time_date.setGeometry(605,190,1920,50)
        weather_city.setGeometry(600,500,1920,50)
        weather_temp.setGeometry(600,540,1920,50)
        weather_humid.setGeometry(850,500,1920,50)

        lo.write("["+tyme+"]: "+"All variables set.\n")

        """
        # Begin setting labels
        def goodmorning():
            currentTime = datetime.datetime.now()
            if currentTime.hour < 12:
                la1.setText("Good Morning,")
            elif 12 <= currentTime.hour < 18:
                la1.setText("Good Afternoon,")
            else:
                la1.setText("Good Night,")

        la1.setFont(font)
        la1.setPalette(fontp) # Set label to palette
        la1.setGeometry(10,0,1920,75)
        la2.setText(u_name)


        timer_timer = QtCore.QTimer()
        timer_timer.timeout.connect(goodmorning)
        timer_timer.start(500) # Check for new tweet/headline every second
        """
        # Set the title of the window.
        w.setWindowTitle("Main") # Set window title text

        def time():
            now = datetime.datetime.now()
            time_time.setText(now.strftime("%H:%M"))
            time_time_s.setText(now.strftime("%S"))
            time_day.setText(now.strftime("%A"))
            time_date.setText(now.strftime("%d %B"))
        time_timer = QtCore.QTimer()
        time_timer.timeout.connect(time)
        time_timer.start(500)  # Check for new tweet/headline every second

        # Color #
        w.setAutoFillBackground(True) # Fill
        p = w.palette() # Make P palette for window and color options
        p.setColor(w.backgroundRole(), Qt.black) # Set window color
        w.setPalette(p) #
        w.show()
        w.showFullScreen() # Make window fullscreen
        headline.setText("Loading..")

        # Weather Data #
        lo.write("["+tyme+"]: "+"Gathering Weather Data... (First time)\n")

        url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+wth_api
        data = requests.get(url)
        read = data.json()

        weather_city.setText(read['name'])
        if unit == 'C' or unit == 'Celsius':
            weather_temp.setText(str(read['main']['temp']-273.15)+'°C')
            lo.write("["+tyme+"]: "+str(read['main']['temp']-273.15)+'°C'+"\n")
        elif unit == 'F' or unit == 'Fareinheit':
            weather_temp.setText(str(read['main']['temp']*9/5-459.67)[:4]+'°F')
            lo.write("["+tyme+"]: "+str(read['main']['temp']*9/5-459.67)[:4]+'°F'+"\n")
        weather_humid.setText(str(read['main']['humidity'])+'%')
        lo.write("["+tyme+"]: "+str(read['main']['humidity'])+'%'+"\n")
        lo.write("["+tyme+"]: "+read['weather'][0]['description']+"\n")

        # Set thermometer icon to corresponding temperature
        if unit == 'C' or 'Celsius':
            if read['main']['temp']-273.15 < 5:
                wth_tmp_img.setPixmap(QtGui.QPixmap('rsc/climacons/Thermometer-Zero.svg'))
            elif read['main']['temp']-273.15 <= 10:
                wth_tmp_img.setPixmap(QtGui.QPixmap('rsc/climacons/Thermometer-25.svg'))
            elif read['main']['temp']-273.15 >= 10:
                wth_tmp_img.setPixmap(QtGui.QPixmap('rsc/climacons/Thermometer-50.svg'))
            elif read['main']['temp']-273.15 >= 20:
                wth_tmp_img.setPixmap(QtGui.QPixmap('rsc/climacons/Thermometer-75.svg'))
            elif read['main']['temp']-273.15 >= 35:
                wth_tmp_img.setPixmap(QtGui.QPixmap('rsc/climacons/Thermometer-100.svg'))
        elif unit == 'F' or 'Fareinheit': #
            if read['main']['temp']*9/5-459.67 < 10:
                wth_tmp_img.setPixmap(QtGui.QPixmap('rsc/climacons/Thermometer-Zero.svg'))
            elif read['main']['temp']*9/5-459.67 >= 32:
                wth_tmp_img.setPixmap(QtGui.QPixmap('rsc/climacons/Thermometer-25.svg'))
            elif read['main']['temp']*9/5-459.67 != 50:
                wth_tmp_img.setPixmap(QtGui.QPixmap('rsc/climacons/Thermometer-50.svg'))
            elif read['main']['temp']-273.15 >= 75:
                wth_tmp_img.setPixmap(QtGui.QPixmap('rsc/climacons/Thermometer-75.svg'))
            elif read['main']['temp']-273.15 >= 100:
                wth_tmp_img.setPixmap(QtGui.QPixmap('rsc/climacons/Thermometer-100.svg'))

        wth_tmp_img.setGeometry(675,540,1920,50)

        # Set icon to corresponding weather #
        wth_desc = read['weather'][0]['description']
        if 'cloud' in wth_desc:
            wth_dsc_img.setPixmap(QtGui.QPixmap('rsc/climacons/Cloud.svg'))
        elif 'clear sky' in wth_desc:
            wth_dsc_img.setPixmap(QtGui.QPixmap('rsc/climacons/Sun.svg'))
        elif 'rain' or 'shower' in wth_desc:
            wth_dsc_img.setPixmap(QtGui.QPixmap('rsc/climacons/Cloud-Rain.svg'))
        elif 'thunder' in wth_desc:
            wth_dsc_img.setPixmap(QtGui.QPixmap('rsc/climacons/Cloud-Lightning.svg'))
        elif 'snow' in wth_desc:
            wth_dsc_img.setPixmap(QtGui.QPixmap('rsc/climacons/Cloud-Snow.svg'))
        elif 'mist' in wth_desc:
            wth_dsc_img.setPixmap(QtGui.QPixmap('rsc/climacons/Cloud-Drizzle.svg'))
        wth_dsc_img.setGeometry(750,570,100,50)

        def wthtime():
            lo.write("["+tyme+"]: "+"Gathering Weather Data... (Automatic)\n")
            requests.get(url) # Re-Get Updated data
            data.json() # Get-it

            weather_city.setText(read['name'])
            if unit == 'C' or unit == 'Celsius':
                weather_temp.setText(str(read['main']['temp']-273.15)+'°C')
                lo.write("["+tyme+"]: "+str(read['main']['temp']-273.15)+'°C'+"\n")
            elif unit == 'F' or unit == 'Fareinheit':
                weather_temp.setText(str(read['main']['temp']*9/5-459.67)[:4]+'°F')
                lo.write("["+tyme+"]: "+str(read['main']['temp']*9/5-459.67)[:4]+'°F'+"\n")
            weather_humid.setText(str(read['main']['humidity'])+'%')
            lo.write("["+tyme+"]: "+str(read['main']['humidity'])+'%'+"\n")
            lo.write("["+tyme+"]: "+read['weather'][0]['description']+"\n")

            # Set thermometer icon to corresponding temperature
            if unit == 'C' or 'Celsius':
                if read['main']['temp']-273.15 < 5:
                    wth_tmp_img.setPixmap(QtGui.QPixmap('rsc/climacons/Thermometer-Zero.svg'))
                elif read['main']['temp']-273.15 <= 10:
                    wth_tmp_img.setPixmap(QtGui.QPixmap('rsc/climacons/Thermometer-25.svg'))
                elif read['main']['temp']-273.15 >= 10:
                    wth_tmp_img.setPixmap(QtGui.QPixmap('rsc/climacons/Thermometer-50.svg'))
                elif read['main']['temp']-273.15 >= 20:
                    wth_tmp_img.setPixmap(QtGui.QPixmap('rsc/climacons/Thermometer-75.svg'))
                elif read['main']['temp']-273.15 >= 35:
                    wth_tmp_img.setPixmap(QtGui.QPixmap('rsc/climacons/Thermometer-100.svg'))
            elif unit == 'F' or 'Fareinheit': #
                if read['main']['temp']*9/5-459.67 < 10:
                    wth_tmp_img.setPixmap(QtGui.QPixmap('rsc/climacons/Thermometer-Zero.svg'))
                elif read['main']['temp']*9/5-459.67 >= 32:
                    wth_tmp_img.setPixmap(QtGui.QPixmap('rsc/climacons/Thermometer-25.svg'))
                elif read['main']['temp']*9/5-459.67 != 50:
                    wth_tmp_img.setPixmap(QtGui.QPixmap('rsc/climacons/Thermometer-50.svg'))
                elif read['main']['temp']-273.15 >= 75:
                    wth_tmp_img.setPixmap(QtGui.QPixmap('rsc/climacons/Thermometer-75.svg'))
                elif read['main']['temp']-273.15 >= 100:
                    wth_tmp_img.setPixmap(QtGui.QPixmap('rsc/climacons/Thermometer-100.svg'))

            wth_tmp_img.setGeometry(675,90,1920,50)

            # Set icon to corresponding weather #
            wth_desc = read['weather'][0]['description']
            if 'cloud' in wth_desc:
                wth_dsc_img.setPixmap(QtGui.QPixmap('rsc/climacons/Cloud.svg'))
            elif 'clear sky' in wth_desc:
                wth_dsc_img.setPixmap(QtGui.QPixmap('rsc/climacons/Sun.svg'))
            elif 'rain' or 'shower' in wth_desc:
                wth_dsc_img.setPixmap(QtGui.QPixmap('rsc/climacons/Cloud-Rain.svg'))
            elif 'thunder' in wth_desc:
                wth_dsc_img.setPixmap(QtGui.QPixmap('rsc/climacons/Cloud-Lightning.svg'))
            elif 'snow' in wth_desc:
                wth_dsc_img.setPixmap(QtGui.QPixmap('rsc/climacons/Cloud-Snow.svg'))
            elif 'mist' in wth_desc:
                wth_dsc_img.setPixmap(QtGui.QPixmap('rsc/climacons/Cloud-Drizzle.svg'))
            wth_dsc_img.setGeometry(750,70,100,50)

        wth_timer = QtCore.QTimer()
        wth_timer.timeout.connect(wthtime)
        wth_timer.start(1800*1000)  # Time in seconds * 1000 for milliseconds, 30 minutes
        # # # # # # # # #

        # Update Reddit and Twitter feeds #
        def rheadlinez():
            lo.write("["+tyme+"]: "+"Gathering Reddit Data (Automatic)\n")
            fo = open('bin/headlines.txt','wb')
            reddit = praw.Reddit(user_agent='Portal Reddit Module (by /u/Swagmanhanna)',
                                client_id='9EASNimdp6ItMw', client_secret="cuuiAqw8QCq3f8jDMbU0uV4uLWA")
            for submission in reddit.subreddit(subreddit).hot(limit=10):
                fo.write(submission.title.encode("utf-8")+b'\n')
            print("Done with Reddit!")
            lo.write("["+tyme+"]: "+"Gathered Successfully.\n")
            fo.close()
        hlz_timer = QtCore.QTimer()
        hlz_timer.timeout.connect(rheadlinez)
        hlz_timer.start(3600*1000)  # Time in seconds * 1000 for milliseconds, 60 minutes, 1 Hour
        snoo_img.setPixmap(QtGui.QPixmap("rsc/reddit_ico.svg"))
        snoo_img.setGeometry(10,200,100,50)

        def update_label():
            with open('bin/tweet.txt', 'r',encoding="utf8") as tweet_file:
                tweet_content = tweet_file.read()
            #tweet.setText(tweet_content) # Split this! Add @ and says.
            reddit_content = random.choice([f for f in open('bin/headlines.txt')])
            headline.setText("/r/"+subreddit+": "+textwrap.fill(reddit_content,30))
            lo.write("["+tyme+"]: "+"Setting title to: "+reddit_content+"\n")
        timer = QtCore.QTimer() # Make a timer
        timer.timeout.connect(update_label) # Once time is up run the function
        timer.start(5000)  # Check for new tweet/headline every 5 seconds

        sys.exit(app.exec_())
        auth = OAuthHandler(ckey, csecret) # Auth Twitter
        auth.set_access_token(atoken, asecret) # Auth Twitter

        keyword = cfg.get('Twitter Module','keyword') # Get keyword
        twitterStream = Stream(auth, listener()) # Initiate Twitter Stream
        twitterStream.filter(track=[keyword]) # Filter tweets

        lo.write("["+tyme+"]: "+"Launching.\n")
        print("Main Launched") # Huston, we don't have a problem.

    parentmodule() # Full speed ahead.

# Launch Control #
if fboot == 'Enable':
    lo.write("["+tyme+"]: "+"Firstboot Found! Launch Setup.py!!!")
    print("Setup has not been run. Please run setup @ setup.py!") # Thanks for trying it out.
    time.sleep(1)
    print()
elif fboot == 'Disable':
    lo.write("["+tyme+"]: "+"Not firstboot! Let's go!")
    print("Not first boot.. Loading settings. ") # Woop.
    print()
    time.sleep(1)
    startup()
else:
    lo.write("["+tyme+"]: "+"Can't tell if Fboot or not... Please check your config.ini or run startup.py!")
    print("Corrupted!!!")
    time.sleep(1)
    print("Something broke in the code. Try running the setup again.") # Don't be an idiot.
# # # # # # # # # # #
