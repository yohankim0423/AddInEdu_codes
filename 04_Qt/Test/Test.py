import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

# ui 파일 연결 - 코드 파일과 같은 폴더내에 위치해야함
from_class = uic.loadUiType("Test.ui")[0]

# 화면 클래스
class WindowClass(QMainWindow, from_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Test, PyOt!")
        self.textEdit.setText("This is text editor.")

        self.pushButton_1.clicked.connect(self.button1_Clicked)
        self.pushButton_2.clicked.connect(self.button2_Clicked)
        self.pushButton_3.clicked.connect(self.button3_Clicked)

        self.checkBox_1.clicked.connect(self.check1_Clicked)
        self.checkBox_2.clicked.connect(self.check2_Clicked)
        self.checkBox_3.clicked.connect(self.check3_Clicked)
        self.checkBox_4.clicked.connect(self.check4_Clicked)

        self.radio_1.clicked.connect(self.radio1_Clicked)
        self.radio_2.clicked.connect(self.radio2_Clicked)
        self.radio_3.clicked.connect(self.radio3_Clicked)

    def radio1_Clicked(self):
        self.textEdit.setText("Radio 1")
    
    def radio2_Clicked(self):
        self.textEdit.setText("Radio 2")
    
    def radio3_Clicked(self):
        self.textEdit.setText("Radio 3")

    def check1_Clicked(self):
        if (self.checkBox_1.isChecked()):
            self.textEdit.setText("CheckBox 1 Checked")
            self.checkBox_5.setChecked(True)
        else:
            self.textEdit.setText("CheckBox 1 Unchecked")
            self.checkBox_5.setChecked(False)
    
    def check2_Clicked(self):
        if (self.checkBox_2.isChecked()):
            self.textEdit.setText("CheckBox 2 Checked")
            self.checkBox_6.setChecked(True)
        else:
            self.textEdit.setText("CheckBox 2 Unchecked")
            self.checkBox_6.setChecked(False)
    
    def check3_Clicked(self):
        if (self.checkBox_3.isChecked()):
            self.textEdit.setText("CheckBox 3 Checked")
            self.checkBox_7.setChecked(True)
        else:
            self.textEdit.setText("CheckBox 3 Unchecked")
            self.checkBox_7.setChecked(False)
    
    def check4_Clicked(self):
        if (self.checkBox_4.isChecked()):
            self.textEdit.setText("CheckBox 4")
            self.checkBox_8.setChecked(True)
        else:
            self.textEdit.setText("CheckBox 4 Unchecked")
            self.checkBox_8.setChecked(False)

    def button1_Clicked(self):
        self.textEdit.setText("Button 1")

    def button2_Clicked(self):
        self.textEdit.setText("Button 2")
    
    def button3_Clicked(self):
        self.textEdit.setText("Button 3")

# Python Main 함수
if __name__ == "__main__":
    app = QApplication(sys.argv) # 프로그램 실행
    myWindows = WindowClass()    # 화면 클래스 생성
    myWindows.show()             # 프로그램 화면 보이기
    sys.exit(app.exec_())        # 프로그램 종료까지 동작시킴