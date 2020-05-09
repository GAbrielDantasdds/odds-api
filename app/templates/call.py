from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


from app.templates.interface import *
from app.control.tratar_banco import take_league, take_events_name
from app.control.tratar_banco import take_odds
from app.config import sports, plataformas_dic



class tela(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QFrame.__init__(self, parent=None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sports = sports()
        self.sport_name  = None
        self._ligas      = None
        self.events_name = None
        self.new_dic     = {}


        def get_league() -> str:
            """ Pega a liga. """

            _response = str(self.ui.comboBox_2.currentText())
            if _response != 'Escolha a liga':
                return _response
            else:
                return False


        def get_event() -> str:
            """ Pega o jogo. """

            _response = str(self.ui.comboBox_3.currentText())
            if _response != 'Escolha o jogo':
                return _response
            else:
                return False

        def insert_table(id) -> None:
            _lista = take_odds(id, self.sport_name)
            self.ui.tableWidget.clearContents()
            dic = plataformas_dic()
            print(_lista)

            for e in _lista:
                self.ui.tableWidget.setItem(dic[e[0]],0, QTableWidgetItem(f'{e[1]}'))
                self.ui.tableWidget.setItem(dic[e[0]],1, QTableWidgetItem(f'{e[2]}'))
                self.ui.tableWidget.setItem(dic[e[0]],2, QTableWidgetItem(f'{e[3]}'))



        def validate() -> list:
            """ Verifica se todos os campos foram preenchidos. """

            _var = [get_league(), get_event()]
            if all(_var):
                insert_table(self.new_dic[_var[1]])
            else:
                print('Preencha todos os campos!')


        def select_sport() -> None:
            """ Mostra o esporte escolhido. """

            self.ui.comboBox_3.clear()
            self.ui.comboBox_2.clear()

            self.sport_name = str(self.ui.comboBox.currentText())
            sport_id = self.sports[str(self.ui.comboBox.currentText())]

            self._ligas = take_league(self.sport_name)
            for liga in self._ligas:
                self.ui.comboBox_2.addItem(liga)


        def select_league() -> None:
            """ Seleciona os nomes de eventos. """

            if self.sport_name != None:
                self.events_name = take_events_name(self.ui.comboBox_2.currentText(), self.sport_name)
                self.ui.comboBox_3.clear()
                self.new_dic.clear()

                for e in self.events_name:
                    self.new_dic[e[0]] = e[1]
                    self.ui.comboBox_3.addItem(e[0])







        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'), validate)
        self.ui.comboBox.currentIndexChanged.connect(select_sport)
        self.ui.comboBox_2.currentIndexChanged.connect(select_league)



def iniciar():
    app = QtGui.QApplication(sys.argv)
    principal = tela()
    principal.show()
    sys.exit(app.exec_())
