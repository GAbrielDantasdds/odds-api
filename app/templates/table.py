from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from app.control.tratar_banco import take_league, take_events_name
from app.control.tratar_banco import take_odds
from app.config import sports, plataformas_dic

from app.templates.tabela import *

import time


class _main(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QFrame.__init__(self, parent=None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sports = sports()
        self._eventos = None


        def mini_tabela(home_od: str, draw_od: str, away_od: str) -> QTableWidgetItem:
            """ Retorna uma mini tabela. """

            tabela = QTableWidget()
            tabela.setRowCount(1)
            if draw_od == None:
                tabela.setColumnCount(2)
            else:
                tabela.setColumnCount(3)
            tabela.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            tabela.horizontalHeader().setVisible(False)
            tabela.verticalHeader().setVisible(False)
            if draw_od == None:
                tabela.horizontalHeader().setDefaultSectionSize(50)
            else:
                tabela.horizontalHeader().setDefaultSectionSize(35)

            tabela.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
            tabela.setItem(0, 0,  QTableWidgetItem(f"{home_od}"))
            if draw_od != None:
                tabela.setItem(0, 1,  QTableWidgetItem(f"{draw_od}"))
                tabela.setItem(0, 2,  QTableWidgetItem(f"{away_od}"))
            else:
                tabela.setItem(0, 1,  QTableWidgetItem(f"{away_od}"))
            return tabela

        def preencher_tabela() -> None:
            """ Preenche os novos campos. """

            for line in range(self.ui.tableWidget.rowCount()):
                for column in range(6):
                    self.ui.tableWidget.setCellWidget(line, column, mini_tabela())


        def select_sport() -> None:
            """ Mostra o esporte escolhido. """

            self.ui.comboBox_2.clear()

            self.sport_name = str(self.ui.comboBox.currentText())
            sport_id = self.sports[str(self.ui.comboBox.currentText())]

            self._ligas = take_league(self.sport_name)
            for liga in self._ligas:
                self.ui.comboBox_2.addItem(liga)


        def insert_tabela(dic: dict) -> None:
            """ Insere informações apartir de um dicionário. """

            def get_data(time_now: str) -> str:
                """ Converte o tempo. """

                return time.strftime("%Y-%m-%d %H:%M", time.localtime(int(time_now)))


            self.ui.tableWidget.setRowCount(len(dic))
            plat = plataformas_dic()
            row = 0
            for evento in dic:
                self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(f'{get_data(dic[evento][1])}'))
                self.ui.tableWidget.setVerticalHeaderItem(row, QTableWidgetItem(f'{evento}'))
                for i in range(len(dic[evento][0])):
                    self.ui.tableWidget.setCellWidget(row, plat[dic[evento][0][i][0]]+1, mini_tabela(dic[evento][0][i][1], dic[evento][0][i][2], dic[evento][0][i][3]))
                row += 1

        def verifica_odss(lista_de_odds: list) -> bool:
            """ verifica se a lista de odds é valida. """

            aux = []
            for odd in lista_de_odds:
                aux.append(any(odd))
            if False in aux:
                return False
            else:
                return True

        def buscar_dados() -> None:
            """ Busca as odds conforme os dados. """
            _sport  = str(self.ui.comboBox.currentText())
            _league = str(self.ui.comboBox_2.currentText())


            if _sport in sports().keys():
                if _league != 'Ligas':
                    self._eventos = take_events_name(_league, _sport)

            if self._eventos != None:
                _dic = {}
                for evento in self._eventos:
                    _odds = take_odds(evento[1], _sport)
                    if verifica_odss(_odds):
                        _evento = evento[0].split('versus')
                        _new_name = _evento[0][:3] + ' vs ' + _evento[1][:3]
                        _dic[_new_name] = _odds, evento[-1]
                    else:
                        pass

            insert_tabela(_dic)




        self.ui.comboBox.currentIndexChanged.connect(select_sport)
        QtCore.QObject.connect(self.ui.busa_dados, QtCore.SIGNAL('clicked()'), buscar_dados)









def chamar_tabela():
    app = QtGui.QApplication(sys.argv)
    principal = _main()
    principal.show()
    sys.exit(app.exec_())
