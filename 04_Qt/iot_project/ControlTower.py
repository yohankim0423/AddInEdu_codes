import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pymysql

from_class = uic.loadUiType("iot_project/ControlTower.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.StreetLamp()
        self.SpeedMeasurement()
        self.connectDB()
        self.getTestDB()

    def connectDB(self):
        self.conn = pymysql.connect(host='smartcity.cdv9nppqt3kw.ap-northeast-2.rds.amazonaws.com', user='dev', password='0423', db='SmartCity', charset='utf8')
        self.cur = self.conn.cursor()


    def getTestDB(self):
        sql = 'select distinct(위치) from TestDB'
        self.cur.execute(sql)

        result = self.cur.fetchall()
        # self.speedEdit.addItem('All')
        
        for data in result:
            # self.speedEdit.addItem(data[0])
            print(data[0])

    
    def StreetLamp(self):
        #위치1
        self.slBtn1.setChecked(True)
        self.slBtn1.setChecked(False)
        #위치2
        self.slBtn2.setChecked(True)
        self.slBtn2.setChecked(False)
        #위치3
        self.slBtn3.setChecked(True)
        self.slBtn3.setChecked(False)
        #위치4
        self.slBtn4.setChecked(True)
        self.slBtn4.setChecked(False)

    def SpeedMeasurement(self):
        self.speedEdit.setText("Speed Measurement")

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())