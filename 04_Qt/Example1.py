import sys
import mysql.connector
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from_class = uic.loadUiType("Example1.ui")[0]

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "0032",
    database = "armbase"
)

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.connect = mydb
        self.cur = mydb.cursor()
        self.getSex()
        self.getJobTitle()
        self.getAgency()

        # sex list
    def getSex(self):
        mydb = 'SELECT DISTINCT SEX FROM celeb'
        self.cur.execute(mydb)
        result = self.cur.fetchall()
        self.editSex.addItem('All')

        for data in result:
            self.editSex.addItem(data[0])

        # JobTitle list
    def getJobTitle(self):
        mydb = 'SELECT DISTINCT JOB_TITLE FROM celeb'
        self.cur.execute(mydb)
        result = self.cur.fetchall()
        self.editJobTitle.addItem('All')

        for data in result:
            self.editJobTitle.addItem(data[0])

        # Agency list
    def getAgency(self):
        mydb = 'SELECT DISTINCT AGENCY FROM celeb'
        self.cur.execute(mydb)
        result = self.cur.fetchall()
        self.editAgency.addItem('All')

        for data in result:
            self.editAgency.addItem(data[0])



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())