import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    la = QtWidgets.QLabel(w)
    font = QtGui.QFont()
    font.setFamily("Helvetica")
    font.setBold(True)
    la.setFont(font)
    la.setText("Hello World!")
    w.setWindowTitle("Test!")
    w.setGeometry(100,100,300,200)
    w.show()
    #w.showFullScreen() -- Make window fullscreen
    sys.exit(app.exec_())

window()
