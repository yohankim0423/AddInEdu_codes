import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal
import cv2, imutils
import time
import datetime

import cv2
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog

class Camera(QThread):
    updatePixmap = pyqtSignal(QPixmap)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.cap = None
        self.running = False

    def run(self):
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                p = convert_to_Qt_format.scaled(640, 480, Qt.KeepAspectRatio)
                self.updatePixmap.emit(QPixmap.fromImage(p))
            else:
                self.stop()
            self.msleep(10)  # msleep to control the frame rate

    def openVideo(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open Video File', '.', 'Video files (*.mp4 *.avi)')
        if file:
            self.cap = cv2.VideoCapture(file)
            self.running = True
            self.start()

    def stop(self):
        self.running = False
        if self.cap:
            self.cap.release()
        self.quit()

from_class = uic.loadUiType("opencv.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.camera = Camera(self)
        self.camera.daemon = True
        self.camera.updatePixmap.connect(self.updateCamera)

        # self.isCameraOn = False
        # self.isRecStart = False
        # self.btnRecord.hide()
        # self.btnCapture.hide()

        # self.pixmap = QPixmap()

        # self.camera = Camera(self)
        # self.camera.daemon = True

        # self.record = Camera(self)
        # self.record.daemon = True
        # self.count = 0

        self.btnOpen.clicked.connect(self.openFile)
        self.btnCamera.clicked.connect(self.clickCamera)
        self.camera.update.connect(self.updateCamera)
        self.btnRecord.clicked.connect(self.clickRecord)
        self.record.update.connect(self.updateRecording)
        self.btnCapture.clicked.connect(self.capture)

        self.count = 0                                                                                                                                           

    def capture(self):
        self.now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = self.now + '.png'

        cv2.imwrite(filename, cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR))

    def updateRecording(self):
            self.writer.write(self.image)
            self.label2.setText(str(self.count))
            self.count += 1

    def clickRecord(self):
        if self.isRecStart == False:
            self.btnRecord.setText('Rec Stop')
            self.isRecStart = True

            self.recordingStart()
        else:
            self.btnRecord.setText('Rec Start')
            self.isRecStart = False

            self.recordingStop()

    def recordingStart(self):
        self.record.running = True
        self.record.start()

        self.now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = self.now + '.avi'
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')

        w = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))

        self.writer = cv2.VideoWriter(filename, self.fourcc, 20.0, (w, h))

    def recordingStop(self):
        self.record.running = False

        if self.isRecStart == True:
            self.writer.release()

    def updateCamera(self):
        retval, self.image = self.video.read()
        if retval:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

            h,w,c = self.image.shape
            qimage = QImage(self.image.data, w, h, w*c, QImage.Format_RGB888)

            self.pixmap = self.pixmap.fromImage(qimage)
            self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

            self.label.setPixmap(self.pixmap)
        # self.label.setText('Camera Running : ' + str(self.count))
        self.count += 1

    def clickCamera(self):
        if self.isCameraOn == False:
            self.btnCamera.setText('Camera off')
            self.isCameraOn = True
            self.btnRecord.show()
            self.btnCapture.show()

            self.cameraStart()

        else:
            self.btnCamera.setText('Camera on')
            self.isCameraOn = False
            self.btnRecord.hide()
            self.btnCapture.hide()

            self.cameraStop()
            self.recordingStop()

    def cameraStart(self):
        self.camera.running = True
        self.camera.start()
        self.video = cv2.VideoCapture(-1)

    def cameraStop(self):
        self.camera.running = False
        self.count = 0
        self.video.release

    def openFile(self):
        file = QFileDialog.getOpenFileName(self, 'Open file', '.', 'Image files (*.jpg *.png)')
        if file[0]:  # Check if a file was selected
            image = cv2.imread(file[0])
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
            h, w, c = image.shape
            bytes_per_line = w * c
            qimage = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        
            self.pixmap = QPixmap.fromImage(qimage)
            self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())
            self.label.setPixmap(self.pixmap)

if __name__== "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())
