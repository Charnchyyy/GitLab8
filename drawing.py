import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Simple_drawing_window(QWidget):

        
def main():
        app = QApplication(sys.argv)
        w  = Simple_paint() 
        w.show()

          return app.exec_()

if __name__=="__main__":
    sys.exit(main())

      

