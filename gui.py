# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import recuros_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(312, 255)
        icon = QIcon()
        icon.addFile(u":/icones/Icons8-Windows-8-Systems-Windows-Logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"background-color: rgb(38, 36, 39);")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionSalvar = QAction(MainWindow)
        self.actionSalvar.setObjectName(u"actionSalvar")
        self.actionversao_1_0 = QAction(MainWindow)
        self.actionversao_1_0.setObjectName(u"actionversao_1_0")
        self.actionabrir = QAction(MainWindow)
        self.actionabrir.setObjectName(u"actionabrir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(301, 221))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"border-color: rgb(248, 237, 178);\n"
"background-color: rgb(38, 36, 39);")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QRect(100, 150, 80, 51))
        font = QFont()
        font.setFamily(u"Nyala")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(248, 200, 76);\n"
"color: rgb(75, 60, 41);")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setFlat(False)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(13, 40, 221, 21))
        self.label.setStyleSheet(u"background-color: rgb(248, 237, 178);\n"
"border-top-color: rgb(205, 174, 82);")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setLineWidth(2)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 40, 41, 21))
        self.pushButton.setStyleSheet(u"background-color: rgb(205, 196, 147);\n"
"border-color: rgb(205, 196, 147);\n"
"image: url(:/icones/find.ico);\n"
"color: rgb(60,60,60);\n"
"font: 8pt \"hooge 05_55\";\n"
"border-color: rgb(99, 98, 99);")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 80, 271, 51))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"image: url(:/icones/EYE_WALLEroxo.gif);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 271, 20))
        font1 = QFont()
        font1.setFamily(u"Dotum")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(205, 196, 147);")
        self.label_3.setFrameShape(QFrame.Panel)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 312, 21))
        self.menubar.setStyleSheet(u"color: rgb(248, 246, 169);\n"
"background-color: rgb(68, 65, 70);\n"
"selection-background-color: rgb(134, 134, 134);")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setStyleSheet(u"")
        self.menuSobre = QMenu(self.menubar)
        self.menuSobre.setObjectName(u"menuSobre")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())
        self.menuFile.addAction(self.actionabrir)

        self.retranslateUi(MainWindow)
        self.actionabrir.triggered.connect(self.pushButton.click)

        self.pushButton_2.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyExe NST", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionSalvar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.actionversao_1_0.setText(QCoreApplication.translate("MainWindow", u"versao 1.0", None))
        self.actionabrir.setText(QCoreApplication.translate("MainWindow", u"abrir", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Converter", None))
        self.label.setText("")
        self.pushButton.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Selecione um arquivo .py", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSobre.setTitle(QCoreApplication.translate("MainWindow", u"Sobre", None))
    # retranslateUi

