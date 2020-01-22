from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import subprocess
import socket
import netifaces as ni



class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def move2RightBottomCorner(win):
        screen_geometry = QApplication.desktop().availableGeometry()
        screen_size = (screen_geometry.width(), screen_geometry.height())
        win_size = (win.frameSize().width(), win.frameSize().height())
        x = screen_size[0] - win_size[0]
        y = screen_size[1] - win_size[1]
        win.move(x, y)


    def initUI(self):
        #GET_IP_CMD ="hostname -i"

        #def run_cmd(cmd):
           # return subprocess.check_output(cmd, shell=True).decode('utf-8') 

        #ip = run_cmd(GET_IP_CMD) 
        ni.ifaddresses('eth0')
        ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
        lbl1 = QLabel(ip, self)
        lbl1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        lbl1.setAlignment(Qt.AlignCenter)
        #lbl1.setWindowFlags(Qt.WA_TranslucentBackground)
        lbl1.setStyleSheet("QLabel {color: red; font-size:40px;}")

        self.layout = QGridLayout()
        self.layout.addWidget(lbl1, 0, 0)

        self.setLayout(self.layout)
        #flags = self.windowFlags() | Qt.FramelessWindowHint | Qt.WA_TranslucentBackground | Qt.WA_NoSystemBackground | Qt.WA_NoSystemBackground | Qt.WA_TranslucentBackground
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint)
        self.setGeometry(50, 50, 100, 100)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.move2RightBottomCorner()
        self.show()

        def move2RightBottomCorner(win):
            screen_geometry = QApplication.desktop().availableGeometry()
            screen_size = (screen_geometry.width(), screen_geometry.height())
            win_size = (win.frameSize().width(), win.frameSize().height())
            x = screen_size[0] - win_size[0]
            y = screen_size[1] - win_size[1]
            win.move(x, y)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())