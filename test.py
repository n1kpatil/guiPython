# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 1280)
        MainWindow.setStyleSheet(u"/* Closed (default) QComboBox view */\n"
"QComboBox {\n"
"    background-color: white;\n"
"    color: black;\n"
"    min-width: 120px;\n"
"    min-height: 30px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Drop-down arrow */\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    background-color: #f0742f;\n"
"    border-left: 1px solid #888;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"\n"
"/* Drop-down list (popup) */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #5c55e9;  /* Popup background */\n"
"    color: white;               /* Popup text */\n"
"    selection-background-color: #3d4ef2;\n"
"    selection-color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"QComboBox {\n"
"    background-color: #292f45;\n"
"    color: #ffffff;\n"
"    border: 1px solid #f0742f;\n"
"    padding-right: 20px;  "
                        "    /* make room for the arrow */\n"
"}\n"
"\n"
"/* drop-down \u201cbutton\u201d area */\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #f0742f;\n"
"}\n"
"\n"
"/* hide any default icon */\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    /* zero-size box so borders form the triangle */\n"
"    width: 0;\n"
"    height: 0;\n"
"    /* left and right edges transparent */\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    /* top edge colored \u2192 points down */\n"
"    border-top: 7px solid white;\n"
"}\n"
"\n"
"/* when pressed, you can nudge it if you like */\n"
"QComboBox::down-arrow:on {\n"
"    border-top-color: lightgray;  /* optional press effect */\n"
"    margin-top: 2px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    background: transparent;\n"
"    width: 0;\n"
"    height: 0;\n"
"    border-left: 5px solid transparent;\n"
"    "
                        "border-right:5px solid transparent;\n"
"    border-top: 5px solid white;    /* \u2190 this is your white arrow */\n"
"}\n"
"/*Copyright (c) DevSec Studio. All rights reserved.\n"
"\n"
"MIT License\n"
"\n"
"Permission is hereby granted, free of charge, to any person obtaining a copy\n"
"of this software and associated documentation files (the \"Software\"), to deal\n"
"in the Software without restriction, including without limitation the rights\n"
"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
"copies of the Software, and to permit persons to whom the Software is\n"
"furnished to do so, subject to the following conditions:\n"
"\n"
"The above copyright notice and this permission notice shall be included in all\n"
"copies or substantial portions of the Software.\n"
"\n"
"THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO"
                        " EVENT SHALL THE\n"
"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
"LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
"*/\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color: #292f45;\n"
"	color: #b9b9bb;\n"
"	border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: #292f45;\n"
"	color: #b9b9bb;\n"
"	border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: #f0742f;\n"
"	color: #fff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 17px;\n"
"	border-color: #f0742f;\n"
"	padding: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #fc7c11;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #ff6b35;\n"
"	color: #fff;\n"
"\n"
""
                        "}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton\n"
"{\n"
"	background-color: #292f45;\n"
"	color: #000000;\n"
"	border-style: solid;\n"
"	border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::hover\n"
"{\n"
"	background-color: #fc7c11;\n"
"	color: #000000;\n"
"	padding: 2px;\n"
"	border-radius: 15px;\n"
"	border-color: #fc7c11;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::pressed\n"
"{\n"
"	background-color: #fc7c11;\n"
"	color: #000000;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit{\n"
"	background-color: #292f45;\n"
"	color: #b9b9bb;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-top: 0px;\n"
"	border-left: 0px;\n"
"	border-right: 0px;\n"
"	border-color: #b9b9bb;\n"
"	padding: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"	background-color: transparent;\n"
"	color: #b9b9bb;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    color"
                        ": #b1b1b1;\n"
"    background-color: #00111d;\n"
"    border: 1px solid #f0742f;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\"); /*To replace*/\n"
"	background-color: #1f2b2b;\n"
"    border: 1px solid #f0742f;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 1px solid #f0742f;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"")
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName(u"actionsave")
        self.actionload = QAction(MainWindow)
        self.actionload.setObjectName(u"actionload")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 130, 681, 321))
        font = QFont()
        font.setFamilies([u"Segoe UI,sans-serif"])
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 40, 111, 16))
        font1 = QFont()
        font1.setBold(True)
        self.label.setFont(font1)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 40, 91, 16))
        self.label_2.setFont(font1)
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(270, 140, 101, 16))
        self.label_7.setFont(font1)
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 140, 121, 16))
        self.label_8.setFont(font1)
        self.comboBox_14 = QComboBox(self.groupBox)
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.setObjectName(u"comboBox_14")
        self.comboBox_14.setGeometry(QRect(260, 60, 147, 42))
        self.comboBox_14.setFont(font1)
        self.comboBox_13 = QComboBox(self.groupBox)
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.setObjectName(u"comboBox_13")
        self.comboBox_13.setGeometry(QRect(260, 160, 147, 42))
        self.comboBox_13.setFont(font1)
        self.comboBox_12 = QComboBox(self.groupBox)
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.setObjectName(u"comboBox_12")
        self.comboBox_12.setGeometry(QRect(60, 60, 147, 42))
        self.comboBox_12.setFont(font1)
        self.comboBox_7 = QComboBox(self.groupBox)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setGeometry(QRect(60, 160, 147, 42))
        self.comboBox_7.setFont(font1)
        self.comboBox_22 = QComboBox(self.groupBox)
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.setObjectName(u"comboBox_22")
        self.comboBox_22.setGeometry(QRect(470, 60, 147, 42))
        self.comboBox_22.setFont(font1)
        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(270, 230, 111, 16))
        self.label_17.setFont(font1)
        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(480, 40, 111, 16))
        self.label_18.setFont(font1)
        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(70, 230, 111, 16))
        self.label_19.setFont(font1)
        self.comboBox_23 = QComboBox(self.groupBox)
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.setObjectName(u"comboBox_23")
        self.comboBox_23.setGeometry(QRect(60, 250, 147, 42))
        self.comboBox_23.setFont(font1)
        self.comboBox_24 = QComboBox(self.groupBox)
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.setObjectName(u"comboBox_24")
        self.comboBox_24.setGeometry(QRect(470, 160, 147, 42))
        self.comboBox_24.setFont(font1)
        self.comboBox_25 = QComboBox(self.groupBox)
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.setObjectName(u"comboBox_25")
        self.comboBox_25.setGeometry(QRect(260, 250, 147, 42))
        self.comboBox_25.setFont(font1)
        self.label_20 = QLabel(self.groupBox)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(480, 140, 111, 16))
        self.label_20.setFont(font1)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 500, 681, 221))
        self.groupBox_2.setFont(font)
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(80, 40, 121, 16))
        self.label_9.setFont(font1)
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(500, 40, 111, 16))
        self.label_10.setFont(font1)
        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(80, 130, 121, 16))
        self.label_15.setFont(font1)
        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(280, 40, 121, 16))
        self.label_16.setFont(font1)
        self.comboBox_20 = QComboBox(self.groupBox_2)
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.setObjectName(u"comboBox_20")
        self.comboBox_20.setGeometry(QRect(60, 60, 147, 42))
        self.comboBox_20.setFont(font1)
        self.label_21 = QLabel(self.groupBox_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(280, 130, 121, 16))
        self.label_21.setFont(font1)
        self.label_23 = QLabel(self.groupBox_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(490, 130, 121, 16))
        self.label_23.setFont(font1)
        self.comboBox_21 = QComboBox(self.groupBox_2)
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.setObjectName(u"comboBox_21")
        self.comboBox_21.setGeometry(QRect(260, 60, 147, 42))
        self.comboBox_21.setFont(font1)
        self.comboBox_26 = QComboBox(self.groupBox_2)
        self.comboBox_26.addItem("")
        self.comboBox_26.addItem("")
        self.comboBox_26.setObjectName(u"comboBox_26")
        self.comboBox_26.setGeometry(QRect(480, 60, 147, 42))
        self.comboBox_26.setFont(font1)
        self.comboBox_27 = QComboBox(self.groupBox_2)
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.comboBox_27.setObjectName(u"comboBox_27")
        self.comboBox_27.setGeometry(QRect(260, 150, 147, 42))
        self.comboBox_27.setFont(font1)
        self.comboBox_30 = QComboBox(self.groupBox_2)
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.setObjectName(u"comboBox_30")
        self.comboBox_30.setGeometry(QRect(480, 150, 147, 42))
        self.comboBox_30.setFont(font1)
        self.comboBox_31 = QComboBox(self.groupBox_2)
        self.comboBox_31.addItem("")
        self.comboBox_31.addItem("")
        self.comboBox_31.setObjectName(u"comboBox_31")
        self.comboBox_31.setGeometry(QRect(60, 150, 147, 42))
        self.comboBox_31.setFont(font1)
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 770, 681, 151))
        self.groupBox_3.setFont(font)
        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(140, 40, 91, 16))
        self.label_11.setFont(font1)
        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(340, 40, 91, 16))
        self.label_22.setFont(font1)
        self.comboBox_28 = QComboBox(self.groupBox_3)
        self.comboBox_28.addItem("")
        self.comboBox_28.addItem("")
        self.comboBox_28.addItem("")
        self.comboBox_28.setObjectName(u"comboBox_28")
        self.comboBox_28.setGeometry(QRect(140, 60, 147, 42))
        self.comboBox_28.setFont(font1)
        self.comboBox_29 = QComboBox(self.groupBox_3)
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.setObjectName(u"comboBox_29")
        self.comboBox_29.setGeometry(QRect(340, 60, 147, 42))
        self.comboBox_29.setFont(font1)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(280, 1000, 141, 61))
        self.pushButton.setFont(font1)
        icon = QIcon()
        icon.addFile(u"../../Users/nikhi/Downloads/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(50, 50))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 50, 161, 61))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"QLabel {\n"
"    min-width: 100px;    /* Optional: Width */\n"
"    min-height: 30px;    /* Optional: Height */\n"
"    font-size: 34px;     /* Adjust font size */\n"
"    font-weight: bold;   /* Optional: make text bold */\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 720, 26))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menufile.menuAction())
        self.menufile.addAction(self.actionsave)
        self.menufile.addAction(self.actionload)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionsave.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.actionload.setText(QCoreApplication.translate("MainWindow", u"load", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Digital Inputs ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Logic Input 1 ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Logic Input 2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Logic Input 6", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Logic Input 5", None))
        self.comboBox_14.setItemText(0, QCoreApplication.translate("MainWindow", u"LB", None))
        self.comboBox_14.setItemText(1, QCoreApplication.translate("MainWindow", u"HB", None))
        self.comboBox_14.setItemText(2, QCoreApplication.translate("MainWindow", u"DRL/POL", None))
        self.comboBox_14.setItemText(3, QCoreApplication.translate("MainWindow", u"TI", None))
        self.comboBox_14.setItemText(4, QCoreApplication.translate("MainWindow", u"Animation", None))
        self.comboBox_14.setItemText(5, QCoreApplication.translate("MainWindow", u"Stop", None))
        self.comboBox_14.setItemText(6, QCoreApplication.translate("MainWindow", u"Tail", None))
        self.comboBox_14.setItemText(7, QCoreApplication.translate("MainWindow", u"Side Marker", None))
        self.comboBox_14.setItemText(8, QCoreApplication.translate("MainWindow", u"Seq TI", None))

        self.comboBox_13.setItemText(0, QCoreApplication.translate("MainWindow", u"LB", None))
        self.comboBox_13.setItemText(1, QCoreApplication.translate("MainWindow", u"HB", None))
        self.comboBox_13.setItemText(2, QCoreApplication.translate("MainWindow", u"DRL/POL", None))
        self.comboBox_13.setItemText(3, QCoreApplication.translate("MainWindow", u"TI", None))
        self.comboBox_13.setItemText(4, QCoreApplication.translate("MainWindow", u"Animation", None))
        self.comboBox_13.setItemText(5, QCoreApplication.translate("MainWindow", u"Stop", None))
        self.comboBox_13.setItemText(6, QCoreApplication.translate("MainWindow", u"Tail", None))
        self.comboBox_13.setItemText(7, QCoreApplication.translate("MainWindow", u"Side Marker", None))
        self.comboBox_13.setItemText(8, QCoreApplication.translate("MainWindow", u"Seq TI", None))

        self.comboBox_12.setItemText(0, QCoreApplication.translate("MainWindow", u"LB", None))
        self.comboBox_12.setItemText(1, QCoreApplication.translate("MainWindow", u"HB", None))
        self.comboBox_12.setItemText(2, QCoreApplication.translate("MainWindow", u"DRL/POL", None))
        self.comboBox_12.setItemText(3, QCoreApplication.translate("MainWindow", u"TI", None))
        self.comboBox_12.setItemText(4, QCoreApplication.translate("MainWindow", u"Animation", None))
        self.comboBox_12.setItemText(5, QCoreApplication.translate("MainWindow", u"Stop", None))
        self.comboBox_12.setItemText(6, QCoreApplication.translate("MainWindow", u"Tail", None))
        self.comboBox_12.setItemText(7, QCoreApplication.translate("MainWindow", u"Side Marker", None))
        self.comboBox_12.setItemText(8, QCoreApplication.translate("MainWindow", u"Seq TI", None))

        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"LB", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"HB", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("MainWindow", u"DRL/POL", None))
        self.comboBox_7.setItemText(3, QCoreApplication.translate("MainWindow", u"TI", None))
        self.comboBox_7.setItemText(4, QCoreApplication.translate("MainWindow", u"Animation", None))
        self.comboBox_7.setItemText(5, QCoreApplication.translate("MainWindow", u"Stop", None))
        self.comboBox_7.setItemText(6, QCoreApplication.translate("MainWindow", u"Tail", None))
        self.comboBox_7.setItemText(7, QCoreApplication.translate("MainWindow", u"Side Marker", None))
        self.comboBox_7.setItemText(8, QCoreApplication.translate("MainWindow", u"Seq TI", None))

        self.comboBox_22.setItemText(0, QCoreApplication.translate("MainWindow", u"LB", None))
        self.comboBox_22.setItemText(1, QCoreApplication.translate("MainWindow", u"HB", None))
        self.comboBox_22.setItemText(2, QCoreApplication.translate("MainWindow", u"DRL/POL", None))
        self.comboBox_22.setItemText(3, QCoreApplication.translate("MainWindow", u"TI", None))
        self.comboBox_22.setItemText(4, QCoreApplication.translate("MainWindow", u"Animation", None))
        self.comboBox_22.setItemText(5, QCoreApplication.translate("MainWindow", u"Stop", None))
        self.comboBox_22.setItemText(6, QCoreApplication.translate("MainWindow", u"Tail", None))
        self.comboBox_22.setItemText(7, QCoreApplication.translate("MainWindow", u"Side Marker", None))
        self.comboBox_22.setItemText(8, QCoreApplication.translate("MainWindow", u"Seq TI", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Logic Input 4", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Logic Input 3", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Logic Input 8", None))
        self.comboBox_23.setItemText(0, QCoreApplication.translate("MainWindow", u"LB", None))
        self.comboBox_23.setItemText(1, QCoreApplication.translate("MainWindow", u"HB", None))
        self.comboBox_23.setItemText(2, QCoreApplication.translate("MainWindow", u"DRL/POL", None))
        self.comboBox_23.setItemText(3, QCoreApplication.translate("MainWindow", u"TI", None))
        self.comboBox_23.setItemText(4, QCoreApplication.translate("MainWindow", u"Animation", None))
        self.comboBox_23.setItemText(5, QCoreApplication.translate("MainWindow", u"Stop", None))
        self.comboBox_23.setItemText(6, QCoreApplication.translate("MainWindow", u"Tail", None))
        self.comboBox_23.setItemText(7, QCoreApplication.translate("MainWindow", u"Side Marker", None))
        self.comboBox_23.setItemText(8, QCoreApplication.translate("MainWindow", u"Seq TI", None))

        self.comboBox_24.setItemText(0, QCoreApplication.translate("MainWindow", u"LB", None))
        self.comboBox_24.setItemText(1, QCoreApplication.translate("MainWindow", u"HB", None))
        self.comboBox_24.setItemText(2, QCoreApplication.translate("MainWindow", u"DRL/POL", None))
        self.comboBox_24.setItemText(3, QCoreApplication.translate("MainWindow", u"TI", None))
        self.comboBox_24.setItemText(4, QCoreApplication.translate("MainWindow", u"Animation", None))
        self.comboBox_24.setItemText(5, QCoreApplication.translate("MainWindow", u"Stop", None))
        self.comboBox_24.setItemText(6, QCoreApplication.translate("MainWindow", u"Tail", None))
        self.comboBox_24.setItemText(7, QCoreApplication.translate("MainWindow", u"Side Marker", None))
        self.comboBox_24.setItemText(8, QCoreApplication.translate("MainWindow", u"Seq TI", None))

        self.comboBox_25.setItemText(0, QCoreApplication.translate("MainWindow", u"LB", None))
        self.comboBox_25.setItemText(1, QCoreApplication.translate("MainWindow", u"HB", None))
        self.comboBox_25.setItemText(2, QCoreApplication.translate("MainWindow", u"DRL/POL", None))
        self.comboBox_25.setItemText(3, QCoreApplication.translate("MainWindow", u"TI", None))
        self.comboBox_25.setItemText(4, QCoreApplication.translate("MainWindow", u"Animation", None))
        self.comboBox_25.setItemText(5, QCoreApplication.translate("MainWindow", u"Stop", None))
        self.comboBox_25.setItemText(6, QCoreApplication.translate("MainWindow", u"Tail", None))
        self.comboBox_25.setItemText(7, QCoreApplication.translate("MainWindow", u"Side Marker", None))
        self.comboBox_25.setItemText(8, QCoreApplication.translate("MainWindow", u"Seq TI", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Logic Input 7", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Analog inputs ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Analog Input 1 ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Analog Input 2", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Analog Input 4", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Analog Input 3", None))
        self.comboBox_20.setItemText(0, QCoreApplication.translate("MainWindow", u"BIN", None))
        self.comboBox_20.setItemText(1, QCoreApplication.translate("MainWindow", u"NTC", None))

        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Analog Input 4", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Analog Input 4", None))
        self.comboBox_21.setItemText(0, QCoreApplication.translate("MainWindow", u"BIN", None))
        self.comboBox_21.setItemText(1, QCoreApplication.translate("MainWindow", u"NTC", None))

        self.comboBox_26.setItemText(0, QCoreApplication.translate("MainWindow", u"BIN", None))
        self.comboBox_26.setItemText(1, QCoreApplication.translate("MainWindow", u"NTC", None))

        self.comboBox_27.setItemText(0, QCoreApplication.translate("MainWindow", u"BIN", None))
        self.comboBox_27.setItemText(1, QCoreApplication.translate("MainWindow", u"NTC", None))

        self.comboBox_30.setItemText(0, QCoreApplication.translate("MainWindow", u"BIN", None))
        self.comboBox_30.setItemText(1, QCoreApplication.translate("MainWindow", u"NTC", None))

        self.comboBox_31.setItemText(0, QCoreApplication.translate("MainWindow", u"BIN", None))
        self.comboBox_31.setItemText(1, QCoreApplication.translate("MainWindow", u"NTC", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Project Details", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"MLD Typs", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Lamp Type", None))
        self.comboBox_28.setItemText(0, QCoreApplication.translate("MainWindow", u"MINI", None))
        self.comboBox_28.setItemText(1, QCoreApplication.translate("MainWindow", u"STD", None))
        self.comboBox_28.setItemText(2, QCoreApplication.translate("MainWindow", u"PLUS", None))

        self.comboBox_29.setItemText(0, QCoreApplication.translate("MainWindow", u"Tail Lamp", None))
        self.comboBox_29.setItemText(1, QCoreApplication.translate("MainWindow", u"Head Lamp", None))
        self.comboBox_29.setItemText(2, QCoreApplication.translate("MainWindow", u"Car Body", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start Test", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Test App ", None))
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"file", None))
    # retranslateUi

