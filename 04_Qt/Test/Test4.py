import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("Test4.ui")[0]

class WindowClass(QMainWindow, from_class) :

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Add.clicked.connect(self.addText)
        self.FontUbuntu.clicked.connect(lambda: self.setFont("Ubuntu"))
        self.FontNanumGothic.clicked.connect(lambda:self.setFont("NamumGothic"))

        self.Red.clicked.connect(lambda: self.setTextColor(255, 0, 0))
        self.Green.clicked.connect(lambda: self.setTextColor(0, 255, 0))
        self.Blue.clicked.connect(lambda: self.setTextColor(0, 0, 255))

    def setTextColor(self, r, g, b):
        color = QColor(r, g, b)
        self.Output.setTextColor(color)

    def addText(self):
        input = self.Input.toPlainText()
        self.Input.clear()
        self.Output.append(input)

    def setFont(self, fontName):
        font = QFont(fontName, 11)
        self.Output.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())