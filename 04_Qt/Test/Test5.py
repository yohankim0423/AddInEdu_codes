import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from_class = uic.loadUiType("Test5.ui")[0]

class WindowsClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnName.clicked.connect(self.inputName)
        self.btnSeason.clicked.connect(self.inputSeason)
        self.btnColor.clicked.connect(self.inputColor)
        self.btnFont.clicked.connect(self.inputFont)
        self.btnFile.clicked.connect(self.openFile)
        self.lineEdit.returnPressed.connect(self.question)

    def question(self):
        text = self.lineEdit.text()

        if text.isdigit():
            self.textEdit.setText(text)
        else:
            retval = QMessageBox.question(self, 'QMessageBox - setText',
                                          'Are you sure to print?',
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if retval == QMessageBox.Yes:
                self.textEdit.setText(text)
            else:
                self.lineEdit.clear()

    def openFile(self):
        name = QFileDialog.getOpenFileName(self, 'Open File', './')

        if name[0]:
            with open(name[0], 'r') as file:
                data = file.read()
                self.textEdit.setText(data)

    def inputFont(self):
        font, ok = QFontDialog.getFont()

        if ok and font:
            info = QFontInfo(font)
            self.textEdit.append(info.family() + info.styleName())
            self.textEdit.selectAll()
            self.textEdit.setFont(font)
            self.textEdit.moveCursor(QTextCursor.End)

    def inputColor(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.textEdit.append("Color")
            self.textEdit.selectAll()
            self.textEdit.setTextColor(color)
            self.textEdit.moveCursor(QTextCursor.End)

    def inputName(self):
        text, ok = QInputDialog.getText(self, 'QInputDialog - Name',
                                        'User name:')
        
        if ok and text:
            self.textEdit.append(text)
        
    def inputSeason(self):
        items = ['Spring', 'Summer', 'Fall', 'Winter']
        item, ok = QInputDialog.getItem(self, 'QinputDialog - Season',
                                         'Season:', items, 0, False)
        
        if ok and item:
            self.textEdit.append(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowsClass()
    myWindows.show()

    sys.exit(app.exec_())