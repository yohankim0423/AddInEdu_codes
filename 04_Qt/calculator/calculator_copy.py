import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class CalculatorApp(QDialog):
    def __init__(self):
        super().__init__()

        # UI 파일 로드
        loadUi("Qt/src/Calculator.ui", self)

        # 창 제목 설정
        self.setWindowTitle('Calculator')

        # 버튼 클릭 이벤트 연결
        self.btn_0.clicked.connect(self.input_digit)
        self.btn_1.clicked.connect(self.input_digit)
        self.btn_2.clicked.connect(self.input_digit)
        self.btn_3.clicked.connect(self.input_digit)
        self.btn_4.clicked.connect(self.input_digit)
        self.btn_5.clicked.connect(self.input_digit)
        self.btn_6.clicked.connect(self.input_digit)
        self.btn_7.clicked.connect(self.input_digit)
        self.btn_8.clicked.connect(self.input_digit)
        self.btn_9.clicked.connect(self.input_digit)

        self.btn_plus.clicked.connect(self.input_operation)
        self.btn_minus.clicked.connect(self.input_operation)
        self.btn_multiply.clicked.connect(self.input_operation)
        self.btn_divide.clicked.connect(self.input_operation)

        self.btn_AC.clicked.connect(self.clear_display)
        self.btn_CE.clicked.connect(self.clear_last_entry)
        self.btn_dot.clicked.connect(self.input_dot)
        self.btn_sign.clicked.connect(self.change_sign)

        self.btn_equal.clicked.connect(self.calculate_result)
        

        # 초기화
        self.current_input = ""

    def input_digit(self):
        button = self.sender()
        self.current_input += button.text()
        self.textBrowser.setText(self.current_input)

    def input_operation(self):
        button = self.sender()

        # 현재 버튼 색상이 붉게 표시되어 있는지 확인
        if button.styleSheet() == "background-color: red;":
            # 붉게 표시되어 있으면 색상 초기화 및 연산자 입력 취소
            self.clear_button_colors()
            # 현재 입력에서 가장 최근의 연산자를 찾아 삭제
            last_operator_index = max(self.current_input.rfind('+'), self.current_input.rfind('-'), self.current_input.rfind('*'), self.current_input.rfind('/'))
            self.current_input = self.current_input[:last_operator_index] if last_operator_index != -1 else ""
            self.textBrowser.setText(self.current_input)
            return

        # 선택된 버튼 붉게 표시
        self.clear_button_colors()
        button.setStyleSheet("background-color: red;")

        if self.current_input:
            # 이전에 입력된 값이 있고 마지막 입력 값이 숫자인 경우
            if self.current_input[-1].isdigit():
                self.current_input += f" {button.text()} "
            else:
                # 마지막 입력 값이 숫자가 아닌 경우 이전 연산자를 삭제하고 새로운 연산자로 대체
                last_operator_index = max(self.current_input.rfind('+'), self.current_input.rfind('-'), self.current_input.rfind('*'), self.current_input.rfind('/'))
                self.current_input = self.current_input[:last_operator_index] if last_operator_index != -1 else self.current_input
                self.current_input += f" {button.text()} "
        else:
            # 입력된 값이 없는 경우 (처음 연산자를 입력한 경우)
            # 연산자를 입력하지 않음
            return

        # 최근 입력값 붉게 표시
        button.setStyleSheet("background-color: red;")

        self.textBrowser.setText(self.current_input)

    def clear_button_colors(self):
        # 모든 버튼 색상 초기화
        for button in [self.btn_plus, self.btn_minus, self.btn_multiply, self.btn_divide]:
            button.setStyleSheet("")

    def change_sign(self):
        if self.current_input and (self.current_input[-1].isdigit() or self.current_input[-1] == '.'):
            # 현재 입력 값이 숫자나 소수점인 경우에만 부호를 변경함
            if self.current_input.startswith('-'):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = '-' + self.current_input
            self.textBrowser.setText(self.current_input)

    def clear_display(self):
        self.current_input = ""
        self.textBrowser.clear()

    def clear_last_entry(self):
        self.current_input = self.current_input[:-1]
        self.textBrowser.setText(self.current_input)

    def input_dot(self):
        if  ('.' not in self.current_input) or \
            (self.current_input[-2] in "+-*/"):
             self.current_input += "."
             self.textBrowser.setText(self.current_input)
        if self.current_input[-1].isdigit() and '.' not in self.current_input.split()[-1]:
            self.current_input += "."
            self.textBrowser.setText(self.current_input)


    def calculate_result(self):
        try:
            result = eval(self.current_input)
            self.textBrowser.setText(str(result))
            self.current_input = str(result)
        except Exception as e:
            self.textBrowser.setText('Error')
            self.current_input = ""
        finally:
            # 모든 연산자 버튼 색상 초기화
            self.clear_button_colors()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec_())