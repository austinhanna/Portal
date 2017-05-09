import sys
import time
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QApplication, QLCDNumber

def window():
    app = QtWidgets.QApplication(sys.argv)

    while True != False:
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]

    # Create our elements #
    w = QtWidgets.QWidget() # The window itself
    la1 = QtWidgets.QLabel(w) # Label 1
    la2 = QtWidgets.QLabel(w) # Label 1

    font = QtGui.QFont() # Make font element
    fontp = QtGui.QPalette()

    font.setFamily("Tahoma") # Set Font
    font.setPointSize(72)
    font.setBold(False) # Bold?
    la1.setFont(font)
    la2.setFont(font)
    #font.setColor(Qt.white)

    fontp.setColor(QtGui.QPalette.Foreground,QtCore.Qt.white)
    la1.setPalette(fontp)
    la2.setPalette(fontp)

    #la1.setGeometry(0,330,1100,500)
    la2.setGeometry(560,330,1100,500)
    la1.setText("Welcome") # Set label text
    la2.setText(text) # Set label text

    w.setWindowTitle("Test!") # Set window title text

    # Color #
    w.setAutoFillBackground(True) # Fill
    p = w.palette() # Make P palette for window and color options
    p.setColor(w.backgroundRole(), Qt.black) # Set window color
    w.setPalette(p) #

    w.show()
    w.showFullScreen() # Make window fullscreen
    sys.exit(app.exec_())

window()
