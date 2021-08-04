import UI
import TestClient
import sys
import socket
import threading
from PyQt5.QtCore import QCoreApplication, QObject, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit

ADDRESS = ('localhost', 20007)
IP_ADDRESS = ('192.168.50.210', 20008)


class Signal(QObject):
    signal_text = pyqtSignal(str)

class MainWinow (...):
    def __init__(self):
        self.client = TcpClient()
        self.btn.clicked.connect(self.btn_send())

    def btn_send(self):
        text = self.lineedit.text()
        self.client.send(text)


class TcpClient:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.client.connect(IP_ADDRESS)

        # recv
        self.recv_thread = threading.Thread(target=self.recv)
        self.recv_thread.start()

    def recv(self):
        while True:
            bytes_data = self.client.recv(1024)
            if not bytes_data:
                break
            str_data = bytes_data.decode('utf-8')
            print(f'\r{str_data}\n', end='')

    def send(self, string: str):
        string = UI.Text.text()
        self.client.send(string.encode('utf-8'))

    def search(self):
        self.client.send('ls'.encode('utf-8'))

    def exit(self):
        self.client.send('exit'.encode('utf-8'))
        self.recv_thread.join()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = TcpClient()
    UI = UI.Ui_MainWindow()
    mw = QMainWindow()
    UI.setupUi(mw)
    mw.show()
    sys.exit(app.exec_())
