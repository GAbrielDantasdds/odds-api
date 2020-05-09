from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from app.control.tratar_banco import take_league, take_events_name
from app.control.tratar_banco import take_odds
from app.config import sports, plataformas_dic

from app.templates.tabela import *


class _main(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QFrame.__init__(self, parent=None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sports = sports()
        self._eventos = None

        # print(dir(self.ui.tableWidget))
        def mini_tabela(home_od: str, draw_od: str, away_od: str) -> QTableWidgetItem:
            """ Retorna uma mini tabela. """

            tabela = QTableWidget()
            tabela.setRowCount(1)
            tabela.setColumnCount(3)
            tabela.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            tabela.horizontalHeader().setVisible(False)
            tabela.verticalHeader().setVisible(False)
            tabela.horizontalHeader().setDefaultSectionSize(33)
            tabela.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
            tabela.setItem(0, 0,  QTableWidgetItem(f"{home_od}"))
            tabela.setItem(0, 1,  QTableWidgetItem(f"{draw_od}"))
            tabela.setItem(0, 2,  QTableWidgetItem(f"{away_od}"))
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

            self.ui.tableWidget.setRowCount(len(dic))
            plat = plataformas_dic()
            row = 0
            for evento in dic:
                self.ui.tableWidget.setVerticalHeaderItem(row, QTableWidgetItem(f'{evento}'))
                for i in range(len(dic[evento])):
                    print(dic[evento][i][0])
                    self.ui.tableWidget.setCellWidget(row, plat[dic[evento][i][0]], mini_tabela(dic[evento][i][1], dic[evento][i][2], dic[evento][i][3]))
                row += 1


        def buscar_dados() -> None:
            """ Busca as odds conforme os dados. """
            _sport  = str(self.ui.comboBox.currentText())
            _league = str(self.ui.comboBox_2.currentText())


            if _sport in self.sports.keys():
                if _league != 'Ligas':
                    self._eventos = take_events_name(_league, _sport)

            if self._eventos != None:
                _dic = {}
                for evento in self._eventos:
                    _odds = take_odds(evento[1], _sport)
                    _dic[evento[0]] = _odds

            insert_tabela(_dic)




        self.ui.comboBox.currentIndexChanged.connect(select_sport)
        QtCore.QObject.connect(self.ui.busa_dados, QtCore.SIGNAL('clicked()'), buscar_dados)









def chamar_tabela():
    app = QtGui.QApplication(sys.argv)
    principal = _main()
    principal.show()
    sys.exit(app.exec_())
