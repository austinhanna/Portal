import sys
import time
import datetime
import os
import socket
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

def startup():
    app = QtWidgets.QApplication(sys.argv)

    # Create our elements #
    w = QtWidgets.QWidget() # The window itself

    ip = QtWidgets.QLabel(w) # IP Label
    la1 = QtWidgets.QLabel(w) # Label 1
    la2 = QtWidgets.QLabel(w) # Label 2
    la3 = QtWidgets.QLabel(w) # Label 3
    la4 = QtWidgets.QLabel(w) # Label 4
    la5 = QtWidgets.QLabel(w) # Label 5
    la6 = QtWidgets.QLabel(w) # Label 6


    font = QtGui.QFont() # Make font element
    fontp = QtGui.QPalette()

    font.setFamily("Helvetica") # Set Font
    font.setPointSize(12)
    font.setBold(False) # Bold?
    ip.setFont(font)
    fontp.setColor(QtGui.QPalette.Foreground,QtCore.Qt.white) # Label Color


    ip.setPalette(fontp) # Set label to palette
    ip.setGeometry(0,0,2500,500) # Label size and positioning
    ip.setText("Setup your mirror @ "+socket.gethostbyname(socket.gethostname()))

     # Set label text
    w.setWindowTitle("Boot") # Set window title text

    # Color #
    w.setAutoFillBackground(True) # Fill
    p = w.palette() # Make P palette for window and color options
    p.setColor(w.backgroundRole(), Qt.black) # Set window color
    w.setPalette(p) #
    w.show()
    #w.showFullScreen() # Make window fullscreen
    sys.exit(app.exec_())
startup()
