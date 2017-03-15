import sys
import time
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

class Window(QWidget):

    def __init__(self, parent = None):

        QWidget.__init__(self, parent)

        button = QtWidgets.QPushButton(self.tr("Click me!"))

        button.clicked.connect(self.fade)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(button)

    def fade(self):

        self.setWindowOpacity(0.5)
        QtCore.QTimer.singleShot(1000, self.unfade)

    def unfade(self):

        self.setWindowOpacity(1)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
