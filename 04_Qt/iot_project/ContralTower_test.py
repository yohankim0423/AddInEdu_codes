import sys
import serial  # pyserial 라이브러리 추가
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *

from_class = uic.loadUiType("iot_project/ControlTower.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initSerial()

        # 버튼 상태를 추적하기 위한 변수
        self.button_states = {
            'pushButton': False,
            'pushButton_2': False,
            'pushButton_3': False,
            'pushButton_4': False
        }

        self.pushButton.clicked.connect(lambda: self.toggle_button_color(self.pushButton, 'pushButton'))
        self.pushButton_2.clicked.connect(lambda: self.toggle_button_color(self.pushButton_2, 'pushButton_2'))
        self.pushButton_3.clicked.connect(lambda: self.toggle_button_color(self.pushButton_3, 'pushButton_3'))
        self.pushButton_4.clicked.connect(lambda: self.toggle_button_color(self.pushButton_4, 'pushButton_4'))

    def initSerial(self):
        # 시리얼 포트 초기화
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # 아두이노 연결 포트와 일치시키기
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.readSerialData)
        self.timer.start(1000)  # 1초 간격으로 데이터 읽기

    def readSerialData(self):
        if self.ser.inWaiting() > 0:
            data = self.ser.readline().decode('utf-8').strip()
            self.label.setText(f"Received: {data}")  # 수신 데이터를 레이블에 표시

    def toggle_button_color(self, button, button_name):
        if self.button_states[button_name]:
            # 이미 해당 색상이면 스타일을 초기 상태로 되돌림
            button.setStyleSheet("")
            self.button_states[button_name] = False
        else:
            # 색상 변경
            button.setStyleSheet("background-color: green;")
            self.button_states[button_name] = True

    def closeEvent(self, event):
        if self.ser.is_open:
            self.ser.close()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WindowClass()  # 수정된 클래스 이름
    ex.show()
    sys.exit(app.exec_())
