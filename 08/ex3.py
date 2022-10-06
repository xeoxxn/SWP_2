import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        # 가로 상자 레이아웃
        # 두 개의 버튼이 있는 가로상자
        hbox = QHBoxLayout()
        hbox.addStretch(1)  # 임의의 빈 공간(늘림 인수!) # (비율이 되는 거임 위에 1 아래 1이면 1 : 1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)
        # 여기서 두 버튼 묶고

        # 세로상자 레이아웃
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        # vbox 안에다 배치
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

