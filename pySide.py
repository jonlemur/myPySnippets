#!/usr/bin/python

'''
Just a simple base to get stared building pySide apps
1. install pyside cmd> pip install -U PySide
'''

# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *

def clickButton():
    print "Hello"

if __name__ == "__main__":
    app = QApplication(sys.argv)

    frame = QMainWindow()
    frame.setMinimumSize(QSize(300, 300))
    frame.setWindowTitle('I Am A Window!')
    frame.setStyleSheet("background-color: rgb(50,50,50); margin:5px;")
    frame.show()

    label = QLabel("Hello World", frame)
    label.setAlignment(Qt.AlignCenter)
    label.setStyleSheet("color: rgb(200, 200, 200);")
    label.show()

    btn = QPushButton('Press', frame)
    btn.move(10,30)
    btn.setStyleSheet("background-color: rgb(100,100,100); color: rgb(200, 200, 200);")
    btn.clicked.connect(clickButton)
    btn.show()

    # Enter Qt application main loop
    app.exec_()
    sys.exit()
        