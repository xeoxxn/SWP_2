import sys
from PyQt5.QtCore import Qt  # 이벤트 처리
from PyQt5.QtWidgets import *  # GUI
# 상태바 쓰려면 QWidget 말고 QMainWindow
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Button1", self)
        btn1.move(30, 50)
        btn2 = QPushButton("Button2", self)
        btn2.move(150, 50)
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Sender()')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()



