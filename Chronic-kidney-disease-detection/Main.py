from PyQt5 import QtWidgets
from ViewControl.mainwindowmanager import mainwindowmanager
import sys

if __name__ == '__main__':
   args = list(sys.argv)
   args[1:1] = ['-stylesheet','aqua.qss']
   app = QtWidgets.QApplication(args)
   win = mainwindowmanager()
   app.exec()
   win.show()