# System Stuff
import sys
import time
import datetime
import os
import configparser
# pyQt stuff #
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

## Get if first boot ##
cfg = configparser.ConfigParser()
cfg.read('bin/config.ini')
fboot = cfg.get('General', 'firstboot')
#print(cfg.get('General', 'firstboot')) # Some debug cause this issue took me 10 minutes....

def startup():
    words = "Loading........"
    for char in words:
        time.sleep(0.3)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    print("Done!")
    print()
    time.sleep(.6)
    print("Launching")
    main()

def main():
    print("Main Launched")

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
        headline.move(10,500)
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
            with open('bin/headlines.txt', 'r',encoding="utf-8") as headline_file:
                reddit_content = headline_file.read()
            with open('twitter/store/tweet.txt', 'r',encoding="utf8") as tweet_file:
                tweet_content = tweet_file.read()
            current_time = str(datetime.datetime.now().time())
            tweet.setText(tweet_content) # Split this! Add @ and says.
            headline.setText(reddit_content)
        timer = QtCore.QTimer()
        timer.timeout.connect(update_label)
        timer.start(500)  # Check for new tweet/headline every second
        sys.exit(app.exec_())
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
