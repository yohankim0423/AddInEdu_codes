import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit
import serial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *

from_class = uic.loadUiType("iot_project/ControlTower.ui")[0]

class ArduinoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.serial_port = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # 적절한 COM 포트를 설정하세요
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.text_display = QTextEdit()
        self.text_display.setReadOnly(True)
        self.layout.addWidget(self.text_display)

        self.button_send = QPushButton('Send Command to Arduino', self)
        self.button_send.clicked.connect(self.send_command)
        self.layout.addWidget(self.button_send)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Arduino Control')
        self.show()

    def send_command(self):
        self.serial_port.write(b's')  # 예제로 's' 명령을 보냄
        response = self.serial_port.readline().decode('utf-8').strip()
        self.text_display.append("Arduino Response: " + response)

    def closeEvent(self, event):
        self.serial_port.close()
        super().closeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ArduinoApp()
    sys.exit(app.exec_())
