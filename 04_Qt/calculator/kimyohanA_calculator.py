import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

from_class = uic.loadUiType("calculator/kimyohanA_calculator.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('Calculator')
        self.textBrowser.setText("0")

        # 숫자 버튼 연결
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
        self.Button_dot.clicked.connect(self.buttonDot_clicked)
        
        # 기능 버튼 연결
        self.Button_AC.clicked.connect(self.buttonAC_reset)
        self.Button_CE.clicked.connect(self.buttonCE_clicked)
        self.Button_sign.clicked.connect(self.buttonSign_clicked)
        
        # 연산 버튼 연결
        self.Button_divide.clicked.connect(lambda: self.operation_clicked("/"))
        self.Button_multiply.clicked.connect(lambda: self.operation_clicked("*"))
        self.Button_minus.clicked.connect(lambda: self.operation_clicked("-"))
        self.Button_plus.clicked.connect(lambda: self.operation_clicked("+"))
        
        # 결과 버튼 연결
        self.Button_equalsign.clicked.connect(self.equals_clicked)

        # 상태 변수
        self.firstNumber = None
        self.operator = None
        self.isSecondNumber = False
        self.isResultDisplayed = False
        self.waitingForOperand = True

    def button_clicked(self, number):
        currentText = self.textBrowser.toPlainText()

        # if self.waitingForOperand:
        #     selfText = ""
        #     self.waitingForOperand = False

        if self.isResultDisplayed or currentText == "0" or self.isSecondNumber:
            currentText = number
            self.isResultDisplayed = False
            self.isSecondNumber = False
        else:
            currentText += number # 현재 텍스트 숫자 추가

        self.textBrowser.setText(currentText)

    def buttonDot_clicked(self):
        currentText = self.textBrowser.toPlainText()

        if self.isResultDisplayed or self.isSecondNumber:
            currentText = "0"
            self.isResultDisplayed = False
            self.isSecondNumber = False
        elif currentText == "0":
            currentText = "0."
        elif '.' not in currentText:
            currentText += "."

        self.textBrowser.setText(currentText)

    def buttonAC_reset(self):
        self.textBrowser.setText("0")
        self.firstNumber = None
        self.operator = None
        self.isSecondNumber = False
        self.isResultDisplayed = False
        self.waitingForOperand = True

    def buttonCE_clicked(self):
        current_text = self.textBrowser.toPlainText()
        if len(current_text) <= 1:
            self.textBrowser.setText("0")
            self.waitingForOperand = True
        else:
            self.textBrowser.setText(current_text[:-1])

    def buttonSign_clicked(self):
        currentText = self.textBrowser.toPlainText()
        if currentText[0] == '-':
            self.textBrowser.setText(currentText[1:])
        else:
            self.textBrowser.setText('-' + currentText)

    def operation_clicked(self, operator):
        currentText = self.textBrowser.toPlainText().rstrip()

        if self.isResultDisplayed or self.firstNumber is None:
            # 결과가 표시된 후 바로 연산자를 누른 경우, 결과값을 첫 번째 숫자로 사용
            self.firstNumber = float(currentText)
            self.isResultDisplayed = False
        self.waitingForOperand = True

        # elif self.firstNumber is None:
        #     # 첫 번째 숫자가 설정되지 않은 경우, 현재 텍스트를 첫 번째 숫자로 사용
        #     self.firstNumber = float(currentText)
        # else:
        #     self.equals_clicked()

        if currentText[-1] in "+-*/":
            self.textBrowser.setText(currentText[:-2] + ' ' + operator + ' ') # 마지막 연산자 교체 사용
        else:
            self.textBrowser.setText(currentText + ' ' + operator + ' ') # 새 연산자 추가

        self.operator = operator
        self.isSecondNumber = True  # 두 번째 숫자 입력을 기다립니다.
        # self.textBrowser.setText(self.textBrowser.toPlainText() + ' ' + operator + ' ')

    def equals_clicked(self):
        currentText = self.textBrowser.toPlainText()
        if self.firstNumber is not None and self.operator:
            # currentText = self.textBrowser.toPlainText()
            try:
                secondNumber = float(currentText.split(' ' + self.operator + ' ')[-1])
            except ValueError:
                secondNumber = self.firstNumber # 연산자 바로 후에 '='를 누른 경우

            result = None
            if self.operator == "+":
                result = self.firstNumber + secondNumber
            elif self.operator == "-":
                result = self.firstNumber - secondNumber
            elif self.operator == "*":
                result = self.firstNumber * secondNumber
            elif self.operator == "/":
                if secondNumber == 0:
                    self.textBrowser.setText("0")
                    return
                result = self.firstNumber / secondNumber

            if result is not None:
                if result == int(result):
                    result = int(result)
                self.textBrowser.setText(str(result))
                self.firstNumber = result

            self.operator = None
            self.isSecondNumber = False
            self.isResultDisplayed = True
            self.waitingForOperand = True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())
