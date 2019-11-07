import sys
import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('G1.ui',self)
        self.pushButton.clicked.connect(self.run)
        self.fl = False
        self.show()

    def run(self):
        self.fl = True
        self.update()

    def paintEvent(self, event):
        if self.fl:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()
        self.fl = False

    def draw(self):
        self.qp.setBrush(QColor(250, 200, 0))
        x = random.randint(100, 350)
        y = random.randint(100, 350)
        z = random.randint(10, 50)
        self.qp.drawEllipse(x, y, z, z)

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())