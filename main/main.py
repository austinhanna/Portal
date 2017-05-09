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
import configparser
cfg = configparser.ConfigParser()

## Get if first boot ###
cfg.read('config.ini')
fboot = cfg.get('General', 'firstboot')
#print(cfg.get('General', 'firstboot')) # Some debug cause this issue took me 10 minutes....

if fboot == 'Enable':
    print("This is the first boot! Running Setup.py...")
    time.sleep(1)
    print()
    os.system('python setup.py 1')
elif fboot == 'Disable':
    print("Not first boot.. Loading settings. ")
    print()
    time.sleep(1)
    print("Loading..")
    time.sleep(1)
    main()
else:
    print("Corrupted!!!")
    time.sleep(1)
    print("Something broke in the code. Try running the setup again.")
