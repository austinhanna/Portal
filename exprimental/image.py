import sys
from PyQt5 import QtWidgets, QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l1 = QtWidgets.QLabel(w)
    l2 = QtWidgets.QLabel(w)
    l1.setText('ya')
    l2.setPixmap(QtGui.QPixmap('Cloud.png'))
    w.setWindowTitle('Cloud')
    w.setGeometry(800, 400, 720, 600)
    l1.move(360, 5)
    l2.move(100, 20)
    w.show()
    sys.exit(app.exec_())


window()
