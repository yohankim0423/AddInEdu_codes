import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

from_class = uic.loadUiType("calculator.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('Calculator')
        self.textBrowser.setText("0")

        # 모든 숫자 버튼
        self.Button_0.clicked.connect(lambda: self.button_clicked("0"))
        self.Button_1.clicked.connect(lambda: self.button_clicked("1"))
        self.Button_2.clicked.connect(lambda: self.button_clicked("2"))
        self.Button_3.clicked.connect(lambda: self.button_clicked("3"))
        self.Button_4.clicked.connect(lambda: self.button_clicked("4"))
        self.Button_5.clicked.connect(lambda: self.button_clicked("5"))
        self.Button_6.clicked.connect(lambda: self.button_clicked("6"))
        self.Button_7.clicked.connect(lambda: self.button_clicked("7"))
        self.Button_8.clicked.connect(lambda: self.button_clicked("8"))
        self.Button_9.clicked.connect(lambda: self.button_clicked("9"))
        # 기능 버튼
        self.Button_AC.clicked.connect(self.buttonAC_reset)
        self.Button_CE.clicked.connect(self.buttonCE_clicked)
        self.Button_sign.clicked.connect(self.buttonSign_clicked)
        # 사칙연산 버튼
        self.Button_divide.clicked.connect(lambda: self.operation_clicked("/"))
        # 결과 버튼
        self.Button_equalsign.clicked.connect(self.equals_clicked)

        self.firstNumber = None
        self.operator = None
        self.isSecondNumber = False
        self.isResultDisplayed = False

    def buttonAC_reset(self):
        self.textBrowser.setText("0")
        self.firstNumber = None
        self.operator = None
        self.isSecondNumber = False
        self.isResultDisplayed = False

    def buttonCE_clicked(self):
        current_text = self.textBrowser.toPlainText()
        if len(current_text) <= 1:  # 현재 텍스트가 한 자리 숫자이거나 0일 때
            self.textBrowser.setText("0")
        else:
            self.textBrowser.setText(current_text[:-1])  # 마지막 숫자를 제거

    def buttonSign_clicked(self):
        # 현재 텍스트의 부호를 변경
        current_text = self.textBrowser.toPlainText()
        if current_text[0] == '-':  # 이미 음수일 경우
            self.textBrowser.setText(current_text[1:])  # '-' 제거
        else:  # 양수일 경우
            self.textBrowser.setText('-' + current_text)

    def button_clicked(self, number):
        if self.isResultDisplayed or self.textBrower.toPlainText == "0":
            self.textBrowser.setText(number)
            self.isResultDisplayed = False
        else:
            self.textBrowser.setText(self.textBrowser.toPlainText() + number)

    def button_clicked(self, number):
        if self.textBrowser.toPlainText() == "0":
            self.textBrowser.setText(number)
        else:
            self.textBrowser.setText(self.textBrowser.toPlainText() + number)

    def operation_clicked(self, operator):
        if self.firstNumber is None:
            self.firstNumber = float(self.textBrowser.toPlainText())
            self.operator = operator
            self.textBrowser.setText(self.textBrowser.toPlainText() + operator)

    def equals_clicked(self):
        if self.firstNumber is not None and self.operator and not self.isSecondNumber:
            currentText = self.textBrowser.toPlainText()
            secondNumberStr = currentText.split(self.operator)[1]
            secondNumber = float(secondNumberStr)

            if self.operator == "/":
                if secondNumber == 0:
                    self.textBrowser.setText("0")
                else:
                    result = self.firstNumber / secondNumber
                    self.textBrowser.setText(str(result))

            # 추가 연산을 위한 준비
            self.firstNumber = None
            self.operator = None
            self.isSecondNumber = False
            self.isResultDisplayed = True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())