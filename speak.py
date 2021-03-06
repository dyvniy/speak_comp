import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from playpart import PlayPart
import soundfile as sf
import os.path
 
class App(QWidget):
    lastAlpha = ' '
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 320
        self.height = 550
        self.initVoice()
        self.initUI()

    def initVoice(self):
        voice_name = 'Words1_nick_vovk'

        if not os.path.isfile(voice_name + '.wav'): 
            data, samplerate = sf.read(voice_name + '.ogg')
            sf.write(voice_name + '.wav', data, samplerate)

        self.pp = PlayPart(voice_name + '.wav')
        fpairs = open(voice_name + '.txt', encoding="utf8")
        lines = fpairs.readlines()
        fpairs.close()
        pair_name = ''
        pair_dict = {}
        comnamval = [0, 0, 0]
        for line in lines:
            if line[0] == '#':
                comnamval[0] += 1
                continue # it's comment
            elif line[0] == '"':
                comnamval[1] += 1
                pair_name = line[1:3]
            else:
                comnamval[2] += 1
                p = line.split()
                pair_dict[pair_name] = [float(p[0]), float(p[1])]
        self.pairs = pair_dict
        print(len(self.pairs))
        
        
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
        self.te.move(0,100)
        self.te.resize(320, 200)

        self.te2 = QTextEdit(self)
        self.te2.move(0,320)
        self.te2.resize(320, 200)
        self.te2.append('не и ')
        button = QPushButton("read", self)
        button.move(20, 530)
        button.resize(40, 20)
        button.clicked.connect(self.on_click2)

        self.show()
 
    @pyqtSlot()
    def on_click(self):
        pair = self.lastAlpha + self.sender().char
        s = 'PyQt5 button '+ self.sender().char + ' click, say = '+ pair
        print(s)
        try:
            self.say(pair)
        except Exception as e:
            print(e)
        self.te.append(s)
        
        self.lastAlpha = self.sender().char

    @pyqtSlot()
    def on_click2(self):
        try:
            text = self.te2.toPlainText()
            lastA = ' '
            for a in text:
                pair = lastA + a
                self.say(pair)
                lastA = a
        except Exception as e:
            print(e)

    def say(self, pair):
        times = self.pairs.get(pair, [0, 1])
        self.pp.Play(times[0], times[1] - times[0])
        pass
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
