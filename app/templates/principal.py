from PyQt4.QtCore import *
from PyQt4.QtGui import *
import threading
import sys

from app.templates._main import *
from app.templates.call import iniciar
from app.templates.table import chamar_tabela


class _main_(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QFrame.__init__(self, parent=None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        def call_1():
            t = threading.Thread(target=iniciar)
            t.start()


        QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL('clicked()'), call_1)




def _principal():
    app = QtGui.QApplication(sys.argv)
    principal_ = _main_()
    principal_.show()
    sys.exit(app.exec_())
