import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import pyqtSignal


class MainWindow(QWidget):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        self.setLayout(QVBoxLayout())

        self.laber1 = QLabel(self)
        self.laber2 = QLabel(self)
        self.laber1.setText("输入您的名字.")
        self.laber2.setText("输入您的手机号码")
        self.change = QPushButton(self)
        self.change.setText("更改")
        self.change.clicked.connect(self.onChange)
        self.layout().addWidget(self.laber1)
        self.layout().addWidget(self.laber2)
        self.layout().addWidget(self.change)

        self.show()

    def onChange(self):
        self.formwindow = FormWindow()
        self.formwindow.submitted1.connect(self.laber1.setText)
        self.formwindow.submitted2.connect(self.laber2.setText)
        self.formwindow.show()


class FormWindow(QWidget):
    submitted1 = pyqtSignal(str)
    submitted2 = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())

        self.edit1 = QLineEdit(self)
        self.edit2 = QLineEdit(self)
        self.submit = QPushButton(self)
        self.submit.setText('Submit')
        self.submit.clicked.connect(self.onSubmit)

        self.layout().addWidget(self.edit1)
        self.layout().addWidget(self.edit2)
        self.layout().addWidget(self.submit)
        self.show()

    def onSubmit(self):
        self.submitted1.emit(self.edit1.text())
        self.submitted2.emit(self.edit2.text())
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
