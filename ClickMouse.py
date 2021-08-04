import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal, QObject


class Signal(QObject):
    clickmouse = pyqtSignal()


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('点击鼠标')

        self.s = Signal()
        self.s.clickmouse.connect(self.about)

        self.show()

    def about(self):
        QMessageBox.about(self, '鼠标', '你点鼠标了吧！')

    def mousePressEvent(self, e):
        self.s.clickmouse.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())