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
        w = QtWidgets.QWidget() # The window itself
        la1 = QtWidgets.QLabel(w) # Label 1

        font = QtGui.QFont() # Make font element
        fontp = QtGui.QPalette()

        font.setFamily("Tahoma") # Set Font
        font.setPointSize(12)
        font.setBold(False) # Bold?
        la1.setFont(font)
        fontp.setColor(QtGui.QPalette.Foreground,QtCore.Qt.white) # Label Color
        la1.setPalette(fontp) # Set label to palette
        la1.setGeometry(0,0,2500,500)
        la1.setText("Hello.")
        w.setWindowTitle("Main") # Set window title text

        # Color #
        w.setAutoFillBackground(True) # Fill
        p = w.palette() # Make P palette for window and color options
        p.setColor(w.backgroundRole(), Qt.black) # Set window color
        w.setPalette(p) #
        w.show()
        #os.system("cd Twitter")
        #os.system("python streaming.py 1")
        #w.showFullScreen() # Make window fullscreen
        sys.exit(app.exec_())
    parentmodule()

    def twittermodule():
        app = QtWidgets.QApplication(sys.argv)

        # Create our elements #
        w = QtWidgets.QWidget() # The window itself
        la1 = QtWidgets.QLabel(w) # Label 1

        font = QtGui.QFont() # Make font element
        fontp = QtGui.QPalette()

        font.setFamily("Tahoma") # Set Font
        font.setPointSize(12)
        font.setBold(False) # Bold?
        la1.setFont(font)
        fontp.setColor(QtGui.QPalette.Foreground,QtCore.Qt.white) # Label Color


        la1.setPalette(fontp) # Set label to palette

        la1.setGeometry(0,0,2500,500) # Label size and positioning
        def update_label():
            with open('twitter/store/tweet.txt', 'r',encoding="utf8") as content_file:
                content = content_file.read()
            current_time = str(datetime.datetime.now().time())
            la1.setText(content) # Split this! Add @ and says.

        timer = QtCore.QTimer()
        timer.timeout.connect(update_label)
        timer.start(1000)  # Check for new tweet every second

         # Set label text
        w.setWindowTitle("Main") # Set window title text

        # Color #
        w.setAutoFillBackground(True) # Fill
        p = w.palette() # Make P palette for window and color options
        p.setColor(w.backgroundRole(), Qt.black) # Set window color
        w.setPalette(p) #
        w.show()
        #os.system("cd Twitter")
        #os.system("python streaming.py 1")
        #w.showFullScreen() # Make window fullscreen
        sys.exit(app.exec_())
    #twittermodule()


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
