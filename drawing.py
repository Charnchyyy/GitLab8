import sys

from PySide.QtGui import *
from PySide.QtCore import *
import PySide.QtCore as QtCore

class W(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(400,400)
        
        self.clear = QPushButton('Erase')
        self.clear.clicked.connect(self.erase)

        layout = QVBoxLayout(self)
        layout.addWidget(self.clear)
        
        self.myIsMousePressing = False
        self.p = QPainter(self)
        self.autoFillBackground()
        self.x = 0
        self.y = 0
        self.r = dict()#{(x,Y,15, 15):rect}
        self.penColor = 1
        
    def erase(self):
        self.r = dict()
        self.update()

    
    def mousePressEvent(self, event):
        self.myIsMousePressing = True
    def mouseReleaseEvent(self, event):
        self.myIsMousePressing = False
    def myTimeOut(self):
        if self.myIsMousePressing:
            pos = self.mapFromGlobal(QCursor.pos())
            self.x = pos.x()/50
            self.y = pos.y()/50
            self.r[(int(self.x*50), int(self.y*50), 55, 55)] = self.penColor
    def paintEvent(self, event):
        self.p.begin(self)
        for k in self.r.keys():
            if self.r[k] == 1:
                self.p.setPen(QtCore.Qt.black)
                self.p.setBrush(QtCore.Qt.black)
            self.p.drawRect(*k)
        self.p.end()
        self.update()

class MyWidget(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(400, 400)
        self.w = W()
        self.setCentralWidget(self.w)
        
        self.t = QTimer(self.w)
        self.t.timeout.connect(self.w.myTimeOut)
        self.t.start()

        
def main():
      app = QApplication(sys.argv)
      w  = MyWidget() 
      w.show()

      return app.exec_()

if __name__=="__main__":
    sys.exit(main())

      

