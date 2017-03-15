import sys
import time
import datetime
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

def window():
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
    #font.setColor(Qt.white)

    fontp.setColor(QtGui.QPalette.Foreground,QtCore.Qt.white)
    la1.setPalette(fontp)


    la1.setGeometry(0,0,1100,500)
    def update_label():
        with open('tweet.txt', 'r') as content_file:
            content = content_file.read()
        current_time = str(datetime.datetime.now().time())
        la1.setText(content) # Split this! Add @ and says.

    timer = QtCore.QTimer()
    timer.timeout.connect(update_label)
    timer.start(1000)  # every 10,000 milliseconds

     # Set label text

    w.setWindowTitle("Test!") # Set window title text

    # Color #
    w.setAutoFillBackground(True) # Fill
    p = w.palette() # Make P palette for window and color options
    p.setColor(w.backgroundRole(), Qt.black) # Set window color
    w.setPalette(p) #

    w.show()
    #w.showFullScreen() # Make window fullscreen
    sys.exit(app.exec_())

window()
