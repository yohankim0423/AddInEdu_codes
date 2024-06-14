import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
import urllib.request

from_class = uic.loadUiType("Test9.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        min = self.spinBox.minimum()
        max = self.spinBox.maximum()
        step = self.spinBox.singleStep()

        self.editMin.setText(str(min))
        self.editMax.setText(str(max))
        self.editStep.setText(str(step))

        self.slider.setRange(min, max)
        self.slider.setSingleStep(step)

        self.btnApply.clicked.connect(self.apply)
        self.spinBox.valueChanged.connect(self.changeSpinBox)
        self.slider.valueChanged.connect(self.changeSlider)

        url = "https://imageio.forbes.com/specials-images/imageserve/61b1f8b2eaeafa01018fdd64/Funny-black-Labrador-Retriever-sits-on-a-small-kid-/0x0.jpg?format=jpg&crop=900,916,x0,y89,safe&width=1440"
        image = urllib.request.urlopen(url).read()

        self.pixmap = QPixmap()
        self.pixmap.loadFromData(image)

        self.pixmap = self.pixmap.scaled(self.pixMap.width(), self.pixMap.height())
        self.pixMap.setPixmap(self.pixmap)

        # self.pixmap = QPixmap()
        # self.pixmap.load('cat.jpg')

        # self.pixMap.setPixmap(self.pixmap)
        # self.pixMap.resize(self.pixmap.width(), self.pixmap.height())

    def apply(self):
        min = self.editMin.text()
        max = self.editMax.text()
        step = self.editStep.text()

        self.spinBox.setRange(int(min), int(max))
        self.spinBox.setSingleStep(int(step))

        self.slider.setRange(int(min), int(max))
        self.slider.setSingleStep(int(step))

    def changeSpinBox(self):
        actualValue = self.spinBox.value()
        self.labelValue.setText(str(actualValue))
        self.slider.setValue(actualValue)

    def changeSlider(self):
        actualValue = self.slider.value()
        self.labelValue2.setText(str(actualValue))
        self.spinBox.setValue(actualValue)

        

if __name__== "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())