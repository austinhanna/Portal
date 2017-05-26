import sys
import time
import datetime
import os
import socket
import configparser
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

config = configparser.ConfigParser()
config.read('bin/config.ini')
sshuser = config.get('General','SSH Username')
sshpass = config.get('General','SSH Password')

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
    font2 = QtGui.QFont() # Make font element
    fontp = QtGui.QPalette()

    font.setFamily("Helvetica") # Set Font
    font.setPointSize(12)
    font.setBold(False) # Bold?
    font2.setFamily("Helvetica") # Set Font
    font2.setPointSize(24)
    font2.setBold(False) # Bold?
    ip.setFont(font)
    fontp.setColor(QtGui.QPalette.Foreground,QtCore.Qt.white) # Label Color


    ip.setPalette(fontp) # Set label to palette
    ip.setGeometry(960,0,2500,500) # Label size and positioning
    ip.setText("Setup your mirror @ "+socket.gethostbyname(socket.gethostname()))

    la1.setPalette(fontp) # Set label to palette
    la1.setGeometry(960,0,2500,200) # Label size and positioning
    la1.setFont(font2)
    la1.setText("Welcome")

    la2.setPalette(fontp) # Set label to palette
    la2.setGeometry(960,0,2500,600) # Label size and positioning
    la2.setFont(font)
    la2.setText("SSSH Username: "+sshuser)

    la3.setPalette(fontp) # Set label to palette
    la3.setGeometry(960,0,2500,700) # Label size and positioning
    la3.setFont(font)
    la3.setText("SSH Password: "+sshpass)

    la4.setPalette(fontp) # Set label to palette
    la4.setGeometry(960,0,2500,800) # Label size and positioning
    la4.setFont(font)
    la4.setText("Login and run command 'python setup.py' from the root folder.")

    la5.setPalette(fontp) # Set label to palette
    la5.setGeometry(960,0,2500,900) # Label size and positioning
    la5.setFont(font)
    la5.setText("This will stop showing after the first launch.")

     # Set label text
    w.setWindowTitle("Boot") # Set window title text

    # Color #
    w.setAutoFillBackground(True) # Fill
    p = w.palette() # Make P palette for window and color options
    p.setColor(w.backgroundRole(), Qt.black) # Set window color
    w.setPalette(p) #
    w.show()
    w.showFullScreen() # Make window fullscreen
    sys.exit(app.exec_())

def gotojail():
    os.system("python main.py 1")

fboot = config.get('General','firstboot')

if fboot == 'Enable':
    startup()
elif fboot == 'Disable':
    print("FIRSTBOOT DETECTED. LAUNCHING INTO MAIN.")
    gotojail() # And don't collect $200
else:
    print("Corruption with FBOOT. Launching into main.")
    gotojail()
