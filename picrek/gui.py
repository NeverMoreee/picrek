#!/user/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QToolTip,
                             QDesktopWidget, QMainWindow, QLabel, QHBoxLayout,
                             QGridLayout)
from PyQt5.QtGui import QIcon, QFont, QPixmap


class TopWin(QMainWindow):
    def __init__(self):
        super(TopWin, self).__init__()
        self.resize(1000, 700)
        self.center()
        self.setWindowTitle('picrek')
        self.setWindowIcon(QIcon('/home/nemos/misc/pic/370987.jpg'))
        QToolTip.setFont(QFont('SansSerif', 10))

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        label1 = QLabel(self)
        label2 = QLabel(self)
        hbox.addWidget(label1)
        hbox.addWidget(label2)
        label1.setFixedWidth(300)
        label1.setFixedHeight(300)
        label2.setFixedWidth(300)
        label2.setFixedHeight(300)
        label1.setPixmap(QPixmap('/home/nemos/misc/pic/370987.jpg'))
        label2.setPixmap(QPixmap('/home/nemos/misc/pic/370987.jpg'))

        btn = QPushButton('Btn1', self)
        btn.resize(btn.sizeHint())
        self.statusBar().showMessage('Ready')

        self.setLayout(hbox)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


app = QApplication(sys.argv)
topwin = TopWin()
sys.exit(app.exec_())
