import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QFormLayout, QLabel, QLineEdit, QTextEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('表单示例')

        formlayout = QFormLayout()
        nameLabel = QLabel('姓名')
        nameLineEdit = QLineEdit('')
        introLabel = QLabel('简介')
        introLineEdit = QLineEdit('')

        formlayout.addRow(nameLabel, nameLineEdit)
        formlayout.addRow(introLabel, introLineEdit)
        self.setLayout(formlayout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())
