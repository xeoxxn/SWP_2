import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        # Window
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        # Setting
        name = QLabel("Name:")
        age = QLabel("Age:")
        score = QLabel("Score:")
        amount = QLabel("Amount:")
        key = QLabel("Key:")
        result = QLabel("Result:")

        # keySet
        self.showkeyCombo = QComboBox()
        self.showkeyCombo.addItem("Name")
        self.showkeyCombo.addItem("Age")
        self.showkeyCombo.addItem("Score")

        # Input
        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()

        # Button
        AddButton = QPushButton("Add")
        DelButton = QPushButton("Del")
        FindButton = QPushButton("Find")
        IncButton = QPushButton("Inc")
        ShowButton = QPushButton("show")

        AddButton.clicked.connect(self.buttonClicked)
        DelButton.clicked.connect(self.buttonClicked)
        FindButton.clicked.connect(self.buttonClicked)
        IncButton.clicked.connect(self.buttonClicked)
        ShowButton.clicked.connect(self.buttonClicked)

        # First line(Ui)
        L1hb = QHBoxLayout()
        L1hb.addWidget(name)
        L1hb.addWidget(self.nameEdit)
        L1hb.addWidget(age)
        L1hb.addWidget(self.ageEdit)
        L1hb.addWidget(score)
        L1hb.addWidget(self.scoreEdit)

        # Second line(Ui)
        L2hb = QHBoxLayout()
        L2hb.addWidget(amount)
        L2hb.addWidget(self.amountEdit)
        L2hb.addWidget(key)
        L2hb.addWidget(self.showkeyCombo)

        # Third line(Ui)
        L3hb = QHBoxLayout()
        L3hb.addWidget(AddButton)
        L3hb.addWidget(DelButton)
        L3hb.addWidget(FindButton)
        L3hb.addWidget(IncButton)
        L3hb.addWidget(ShowButton)

        # Fourth line(Ui)
        L4hb = QHBoxLayout()
        L4hb.addWidget(result)

        # Result
        self.AllResult = QTextEdit()

        # Fifth line(Ui)
        L5hb = QHBoxLayout()
        L5hb.addWidget(self.AllResult)

        # Layout
        vbox = QVBoxLayout()
        vbox.addLayout(L1hb)
        vbox.addLayout(L2hb)
        vbox.addLayout(L3hb)
        vbox.addLayout(L4hb)
        vbox.addLayout(L5hb)
        self.setLayout(vbox)

        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        Keyc = self.showkeyCombo.currentText()
        St_Scoredb = sorted(self.scoredb, key = lambda x:x[Keyc])

        for i in St_Scoredb:
            self.AllResult.append("Age=" + str(i["Age"]) + "    " + "Name=" + str(i["Name"]) + "        " + "Score=" + str(i["Score"]) + "     ")

    def buttonClicked(self):
        sender = self.sender()

        if sender.text() == "Add":
            get = {}
            a = self.nameEdit.text()
            b = self.ageEdit.text()
            c = self.scoreEdit.text()

            get["Name"] = a
            get["Age"] = b
            get["Score"] = c

            self.AllResult.clear()
            self.scoredb.append(get)
            self.showScoreDB()

        if sender.text() == "Del":
            for j in self.scoredb:
                if j["Name"] == self.nameEdit.text():
                    self.scoredb.remove(j)

            self.AllResult.clear()
            self.showScoreDB()

        if sender.text() == "Find":
            for k in self.scoredb:
                if k["Name"] == self.nameEdit.text():
                    self.AllResult.append("Age=" + str(k["Age"]) + "    " + "Name=" + str(k["Name"]) + "        " + "Score=" + str(k["Score"]) + "     ")

        if sender.text() == "Inc":
            for l in self.scoredb:
                if l["Name"] == self.nameEdit.text():
                    l["Score"] += int(self.amountEdit.text())

            self.AllResult.clear()
            self.showScoreDB()

        if sender.text() == "Show":
            if self.showkeyCombo.currentText() == "Name":
                sorted(self.scoredb, key=lambda x: x["Name"])

            elif self.showkeyCombo.currentText() == "Age":
                sorted(self.scoredb, key=lambda x: x["Age"])

            elif self.showkeyCombo.currentText() == "Score":
                sorted(self.scoredb, key=lambda x: x["Score"])

            self.AllResult.clear()
            self.showScoreDB()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())