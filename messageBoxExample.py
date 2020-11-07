import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QDialog, QApplication, QPushButton


class Example(QDialog):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)

        msgBox = QMessageBox()
        msgBox.setText('What to do?')
        msgBox.addButton(QPushButton('Accept'), QMessageBox.YesRole)
        msgBox.addButton(QPushButton('Reject'), QMessageBox.NoRole)
        msgBox.addButton(QPushButton('Cancel'), QMessageBox.RejectRole)
        ret = msgBox.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())