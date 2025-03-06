# ch 4.2.1 main.py
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox)
from PyQt5.QtGui import QIcon # icon 추가

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def activateMessage(self):
        QMessageBox.information(self, 'information', 'Button clicked!')

    def initUI(self):
        self.btn1 = QPushButton('Message', self)
        self.btn1.clicked.connect(self.activateMessage)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.btn1)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('Calc.png'))
        self.resize(250,250)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())
