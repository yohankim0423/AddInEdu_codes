import serial
import time
import mysql.connector

class Connect():
    def __init__(self):
        super().__init__()
        self.port = '/dev/ttyACM0'
        self.baudrate = 9600
        self.py_serial = serial.Serial(self.port, self.baudrate)

        self.ArduinoAndMysql()

    def ArduinoAndMysql(self):
        while True:
            commend = input('Input : ')
            print(commend.encode())
            self.py_serial.write(commend.encode())

            time.sleep(1)

            if self.py_serial.readable():
                response = self.py_serial.readline()
                print(response[:len(response)-1].decode())

if __name__ == "__main__":
    connect = Connect()