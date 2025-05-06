# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plot.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 1002)
        MainWindow.setStyleSheet(u"/*Copyright (c) DevSec Studio. All rights reserved.\n"
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
"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
"LIABILITY, WHETHER IN AN ACT"
                        "ION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
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
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton\n"
"{\n"
"	background-color: #292f45;\n"
"	color: #000000;\n"
""
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
"    color: #b1b1b1;\n"
"    background-color: #00111d;\n"
"    border: 1px solid #f0742f;\n"
"    width: 12px;\n"
"    height: 12p"
                        "x;\n"
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 10, 741, 931))
        self.tabWidget = QTabWidget(self.groupBox)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 590, 721, 331))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayoutWidget = QWidget(self.tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 10, 701, 231))
        self.plotContainer = QVBoxLayout(self.verticalLayoutWidget)
        self.plotContainer.setObjectName(u"plotContainer")
        self.plotContainer.setContentsMargins(0, 0, 0, 0)
        self.pushButton_13 = QPushButton(self.tab)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(270, 250, 151, 41))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 641, 271))
        self.tabWidget.addTab(self.tab_2, "")
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 30, 701, 221))
        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 40, 111, 41))
        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(190, 40, 111, 41))
        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(360, 40, 111, 41))
        self.pushButton_4 = QPushButton(self.groupBox_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(530, 40, 111, 41))
        self.pushButton_5 = QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 120, 111, 41))
        self.pushButton_6 = QPushButton(self.groupBox_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(190, 120, 111, 41))
        self.pushButton_7 = QPushButton(self.groupBox_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(360, 120, 111, 41))
        self.pushButton_8 = QPushButton(self.groupBox_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(530, 120, 111, 41))
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 280, 691, 131))
        self.pushButton_9 = QPushButton(self.groupBox_4)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(20, 50, 111, 41))
        self.pushButton_10 = QPushButton(self.groupBox_4)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(180, 50, 111, 41))
        self.pushButton_11 = QPushButton(self.groupBox_4)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(350, 50, 111, 41))
        self.pushButton_12 = QPushButton(self.groupBox_4)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(510, 50, 111, 41))
        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(20, 450, 691, 131))
        self.pushButton_22 = QPushButton(self.groupBox_5)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(20, 50, 111, 61))
        self.pushButton_23 = QPushButton(self.groupBox_5)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(520, 50, 111, 61))
        self.pushButton_24 = QPushButton(self.groupBox_5)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(190, 50, 111, 61))
        self.pushButton_25 = QPushButton(self.groupBox_5)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setGeometry(QRect(360, 50, 111, 61))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Start Recording", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"outage line", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Current values", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Logic Inputs", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Sequences", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Lock Vehicle", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Unlock Vehicle", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Ignition on ", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Seq Turn", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Animations", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Walk Up \n"
" Day", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Walk Away \n"
" Day", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Walk up \n"
" Night", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Walk Away \n"
" Night", None))
    # retranslateUi

