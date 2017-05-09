import sys
import time
import datetime
import os
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

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
        with open('store/tweet.txt', 'r',encoding="utf8") as content_file:
            content = content_file.read()
        current_time = str(datetime.datetime.now().time())
        la1.setText(content) # Split this! Add @ and says.

    timer = QtCore.QTimer()
    timer.timeout.connect(update_label)
    timer.start(1000)  # Check for new tweet every second

     # Set label text
    w.setWindowTitle("Twitter") # Set window title text

    # Color #
    w.setAutoFillBackground(True) # Fill
    p = w.palette() # Make P palette for window and color options
    p.setColor(w.backgroundRole(), Qt.black) # Set window color
    w.setPalette(p) #
    w.show()
    os.system("python streaming.py 1")
    #w.showFullScreen() # Make window fullscreen
    sys.exit(app.exec_())

twittermodule()
