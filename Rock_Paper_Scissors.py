import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('剪刀石头布')

        bt1 = QPushButton("剪刀", self)
        bt1.setGeometry(50, 200, 50, 50)

        bt2 = QPushButton("石头", self)
        bt2.setGeometry(150, 200, 50, 50)

        bt3 = QPushButton("布", self)
        bt3.setGeometry(250, 200, 50, 50)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(bt1)
        hbox.addStretch(1)
        hbox.addWidget(bt2)
        hbox.addStretch(1)
        hbox.addWidget(bt3)
        hbox.addStretch(6)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        bt1.clicked.connect(self.buttonClicked)
        bt2.clicked.connect(self.buttonClicked)
        bt3.clicked.connect(self.buttonClicked)

        self.setLayout(vbox)
        self.show()

    def buttonClicked(self):
        computer = randint(1, 3)
        player = 0
        sender = self.sender()
        if sender.text() == "剪刀":
            player = 1
        elif sender.text() == "石头":
            player = 2
        else:
            player = 3

        if computer == player:
            QMessageBox.about(self, '结果', '平手')
        elif player == 1 and computer == 2:
            QMessageBox.about(self, '结果', '电脑:石头,电脑赢了!')
        elif player == 2 and computer == 3:
            QMessageBox.about(self, '结果', '电脑:布,电脑赢了!')
        elif player == 3 and computer == 1:
            QMessageBox.about(self, '结果', '电脑:剪刀,电脑赢了!')
        elif computer == 1 and player == 2:
            QMessageBox.about(self, '结果', '电脑:剪刀,玩家赢了!')
        elif computer == 2 and player == 3:
            QMessageBox.about(self, '结果', '电脑:石头,玩家赢了!')
        elif computer == 3 and player == 1:
            QMessageBox.about(self, '结果', '电脑:布,玩家赢了!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
