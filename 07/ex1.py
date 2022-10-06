import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(550, 550)
    w.move(1000, 900)
    w.setWindowTitle('Simplel')
    w.show()

    sys.exit(app.exec_())
