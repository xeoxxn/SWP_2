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
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        # QTextEdit (class 내 다른 함수에서 사용해야 해서 self. 를 추가함)
        self.txtResult = QTextEdit() # LineEdit과 다르게 여러줄의 데이터를 입력할 수 있음.

        # QLabels
        labelname = QLabel('Name: ', self)
        labelage = QLabel('Age: ', self)
        labelscore = QLabel('Score: ', self)
        labelamount = QLabel('Amount: ', self)
        labelkey = QLabel('Key: ', self)
        labelresult = QLabel('Result: ', self)

        # QLineEdits
        self.showkeyCombo = QComboBox()
        self.showkeyCombo.addItem("Name")
        self.showkeyCombo.addItem("Age")
        self.showkeyCombo.addItem("Score")

        # QComboBox
        nameEdit = QLineEdit("", self) # lne
        ageEdit = QLineEdit("", self)
        scoreEdit = QLineEdit("", self)
        amountEdit = QLineEdit("", self)

        # QPushButtons
        addbtn = QPushButton("Add", self)
        delbtn = QPushButton("Del", self)
        findbtn = QPushButton("Find", self)
        incbtn = QPushButton("Inc", self)
        showbtn = QPushButton("Show", self)
        # addbtn = QPushButton("Add")
        # delbtn = QPushButton("Del")
        # findbtn = QPushButton("Find")
        # incbtn = QPushButton("Inc")
        # showbtn = QPushButton("show")
        addbtn.clicked.connect(lambda : self.doScoreDb(self.scoredb, "Add " + nameEdit.text() + " " + ageEdit.text() + " " + scoreEdit.text()))
        delbtn.clicked.connect(lambda : self.doScoreDb(self.scoredb, "Del " + nameEdit.text()))
        findbtn.clicked.connect(lambda : self.doScoreDb(self.scoredb, "Find " + nameEdit.text()))
        incbtn.clicked.connect(lambda : self.doScoreDb(self.scoredb, "Inc " + nameEdit.text() + " " + amountEdit.text()))
        showbtn.clicked.connect(lambda : self.doScoreDb(self.scoredb, "Show " + self.showkeyCombo.currentText()))

        # addbtn.clicked.connect(self.buttonClicked)
        # delbtn.clicked.connect(self.buttonClicked)
        # findbtn.clicked.connect(self.buttonClicked)
        # incbtn.clicked.connect(self.buttonClicked)
        # showbtn.clicked.connect(self.buttonClicked)
        # First Line QHBoxLayout
        hb1 = QHBoxLayout()

        hb1.addWidget(labelname)
        hb1.addWidget(nameEdit)
        hb1.addWidget(labelage)
        hb1.addWidget(ageEdit)
        hb1.addWidget(labelscore)
        hb1.addWidget(scoreEdit)

        # Second Line QHBoxLayout
        hb2 = QHBoxLayout()

        hb2.addStretch(1)
        hb2.addWidget(labelamount)
        hb2.addWidget(amountEdit)
        hb2.addWidget(labelkey)
        hb2.addWidget(self.showkeyCombo)

        # Third Line QHBoxLayout
        hb3 = QHBoxLayout()

        hb3.addStretch(1)
        hb3.addWidget(addbtn)
        hb3.addWidget(delbtn)
        hb3.addWidget(findbtn)
        hb3.addWidget(incbtn)
        hb3.addWidget(showbtn)

        hb4 = QVBoxLayout()
        hb4.addWidget(labelresult)

        # QVBoxLayout
        vb = QVBoxLayout()

        vb.addLayout(hb1)
        vb.addLayout(hb2)
        vb.addLayout(hb3)
        vb.addLayout(hb4)
        vb.addWidget(self.txtResult)

        self.setLayout(vb)

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

    def showScoreDB(self, keyname='Name'):
        resultText = ''
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                resultText += (attr + "=" + str(p[attr]) + "    ")
            resultText += "\n"

        self.txtResult.setText(resultText)

    # def showScoreDB(self, keyname='Name'):
    #     resultText = ''
    #     for p in sorted(self.scoredb, key=lambda person: person[keyname]):
    #         for attr in sorted(p):
    #             resultText += (attr + "=" + str(p[attr]) + "    ")
    #         resultText += "\n"
    #
    #     self.txtResult.setText(resultText)

    # def showScoreDB(self):
    #     keyname = str(self.showKeyCombo.currentText())
    #     msg = ""
    #     keyname = "Name" if not keyname else keyname
    #
    #     for p in sorted(self.scoredb, key = lambda person: person[keyname]):
    #         for attr in sorted(p):
    #             msg += attr + "=" + str(p[attr]) + "      \t"
    #
    #         msg += "\n"
    #     self.txtResult.setText(msg)


    def doScoreDb(self, scoredb, inputstr):
        parse = inputstr.split(" ")
        if parse[0] == 'Add':
            record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
            scoredb += [record]
            self.showScoreDB()
        elif parse[0] == 'Del':
            for p in scoredb:
                if p['Name'] == parse[1]:
                    scoredb.remove(p)
            self.showScoreDB()
        elif parse[0] == 'Show':
            sortKey = parse[1]
            self.showScoreDB(sortKey)
        elif parse[0] == 'Inc':
            for p in scoredb:
                if p['Name'] == parse[1]:
                    p['Score'] = int(p['Score']) + int(parse[2])
            self.showScoreDB()
        elif parse[0] == 'Find':
            resultText = ''
            for p in scoredb:
                if p['Name'] == parse[1]:
                    for attr in sorted(p):
                        resultText += (attr + "=" + str(p[attr]) + "    ")
                    resultText += "\n"
            self.txtResult.setText(resultText)


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())