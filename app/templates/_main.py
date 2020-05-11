# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_.ui'
#
# Created: Sun May 10 20:34:03 2020
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
        MainWindow.resize(381, 312)
        MainWindow.setStyleSheet(_fromUtf8("QLabel{\n"
"font: 14px;\n"
"color: white;\n"
"}\n"
"\n"
"#parar:hover{\n"
"    \n"
"    background-color: rgb(229, 0, 0);\n"
"}\n"
"\n"
"#iniciar:hover{\n"
"    \n"
"    background-color: rgb(0, 144, 106);\n"
"}\n"
"\n"
"#iniciar{\n"
"color: white;\n"
"background-color: rgb(0, 170, 127);\n"
"transition: 0,2s;\n"
"}\n"
"\n"
"#parar{\n"
"color: white;\n"
"background-color: rgb(255, 85, 0);\n"
"transition: 0,2s;\n"
"\n"
"}\n"
"\n"
"QMainWindow{\n"
"    background-color: rgb(85, 85, 127);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"color: white;\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 9, 361, 51))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 100, 171, 161))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.iniciar = QtGui.QPushButton(self.groupBox)
        self.iniciar.setGeometry(QtCore.QRect(10, 30, 151, 23))
        self.iniciar.setObjectName(_fromUtf8("iniciar"))
        self.parar = QtGui.QPushButton(self.groupBox)
        self.parar.setGeometry(QtCore.QRect(10, 60, 151, 23))
        self.parar.setObjectName(_fromUtf8("parar"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(13, 90, 151, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 151, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(190, 100, 181, 161))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(14, 30, 151, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(14, 60, 151, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 381, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuConfigura_es = QtGui.QMenu(self.menuBar)
        self.menuConfigura_es.setObjectName(_fromUtf8("menuConfigura_es"))
        MainWindow.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menuConfigura_es.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ODDS -BOT", None))
        self.label.setText(_translate("MainWindow", "Painel de controle", None))
        self.groupBox.setTitle(_translate("MainWindow", "Requisições", None))
        self.iniciar.setText(_translate("MainWindow", "INICIAR", None))
        self.parar.setText(_translate("MainWindow", "PARAR", None))
        self.label_2.setText(_translate("MainWindow", "Próxima requisição em:", None))
        self.label_3.setText(_translate("MainWindow", "60 minutos", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Janelas", None))
        self.pushButton_3.setText(_translate("MainWindow", "SPORT INDIVIDUAL", None))
        self.pushButton_4.setText(_translate("MainWindow", "TABELA ODDS/LIGA", None))
        self.menuConfigura_es.setTitle(_translate("MainWindow", "Configurações", None))

