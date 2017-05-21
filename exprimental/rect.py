import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtCore import *


class MyWindow(QMainWindow):
    def paintEvent(self, event):


def updateValues():
    global a, x
    a += 1
    x += 1
    mw.update()  # <-- update the window!


a = 10
b = 15
x = 90
y = 60

app = QApplication(sys.argv)

mw = MyWindow()
mw.setWindowTitle('PyQt5 - Main Window')
mw.setWindowIcon(QIcon("icon.jpg"))
mw.resize(300,100)

timer = QTimer()
timer.timeout.connect(updateValues)
timer.start(33)

mw.show()
sys.exit(app.exec_())
