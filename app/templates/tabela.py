# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teste.ui'
#
# Created: Sat May 09 01:18:03 2020
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(775, 507)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet(_fromUtf8("QLabel{\n"
"    font: 14px;\n"
"}\n"
"\n"
"QTableView{\n"
"border-radius: 5px 5px 5px 5px;\n"
"background-color: rgb(85, 100, 100);\n"
"}\n"
"\n"
"QTableView::Item{\n"
"\n"
"color: rgb(255, 255, 200)\n"
"}"))
        MainWindow.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly|QtCore.Qt.ImhHiddenText)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 90, 741, 391))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.tableWidget = QtGui.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 711, 351))
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.tableWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setAutoScrollMargin(100)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(1)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 131, 67))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.selecioneOEsporteLabel = QtGui.QLabel(self.formLayoutWidget)
        self.selecioneOEsporteLabel.setObjectName(_fromUtf8("selecioneOEsporteLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.selecioneOEsporteLabel)
        self.comboBox = QtGui.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.comboBox)
        self.formLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(180, 20, 103, 61))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.selecionaALigaLabel = QtGui.QLabel(self.formLayoutWidget_2)
        self.selecionaALigaLabel.setObjectName(_fromUtf8("selecionaALigaLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.selecionaALigaLabel)
        self.comboBox_2 = QtGui.QComboBox(self.formLayoutWidget_2)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.SpanningRole, self.comboBox_2)
        self.busa_dados = QtGui.QPushButton(self.centralwidget)
        self.busa_dados.setGeometry(QtCore.QRect(300, 41, 91, 23))
        self.busa_dados.setObjectName(_fromUtf8("busa_dados"))
        self.atualizar_tabela = QtGui.QPushButton(self.centralwidget)
        self.atualizar_tabela.setGeometry(QtCore.QRect(400, 41, 91, 23))
        self.atualizar_tabela.setObjectName(_fromUtf8("atualizar_tabela"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Tabela de Cotações", None))
        self.groupBox.setTitle(_translate("MainWindow", "TABELA", None))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Bet365", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "188bet", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Vbet", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Betway", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Pinnacle", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "1xbet", None))
        self.selecioneOEsporteLabel.setText(_translate("MainWindow", "Selecione o esporte:", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Esportes", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "soccer", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "table_tennis", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "tennis", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "volleyball", None))
        self.selecionaALigaLabel.setText(_translate("MainWindow", "Seleciona a liga:", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Ligas", None))
        self.busa_dados.setText(_translate("MainWindow", "Buscar dados", None))
        self.atualizar_tabela.setText(_translate("MainWindow", "Atualizar tabela", None))

