import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
    char = 'No'
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 320
        self.height = 400
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        ai = 'а'
        while ai <= 'я':
            print(ai)
            button = QPushButton(ai, self)
            button.setToolTip('This is an example button')
            i = ord(ai) - ord('а') 
            button.move(40*(i%8),20*int(i/8))
            button.resize(40, 20)
            button.char = ai
            button.clicked.connect(self.on_click)
            oi = ord(ai) + 1
            ai = chr(oi)

        self.te = QTextEdit(self)
        self.te.move(0,120)
        self.te.resize(320, 200)

        self.show()
 
    @pyqtSlot()
    def on_click(self):
        s = 'PyQt5 button '+ self.sender().char + ' click'
        print(s)
        self.te.append(s)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
