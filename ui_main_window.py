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
    QSizePolicy, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(560, 422)
        MainWindow.setStyleSheet(u"QMainWindow, QWidget {\n"
"    background-color: #1e1e1e;\n"
"    color: #d4d4d4;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #2d2d30;\n"
"    color: #ffffff;\n"
"    border: 1px solid #3c3c3c;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c3c3c;\n"
"    border: 1px solid #5a5a5a;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2a2a2a;\n"
"    border: 1px solid #0078d7;  /* Accent blue */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #d4d4d4;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: #2d2d30;\n"
"    color: #ffffff;\n"
"    border: 1px solid #3c3c3c;\n"
"    border-radius: 4px;\n"
"    padding: 4px 8px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #5a5a5a;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 1px solid #333;\n"
"    border-radius: 6px;\n"
"    margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox:title {\n"
"    subcontrol-origin"
                        ": margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 5px;\n"
"    color: #aaaaaa;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QLineEdit, QTextEdit {\n"
"    background-color: #2d2d30;\n"
"    border: 1px solid #444;\n"
"    color: #ffffff;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QStatusBar {\n"
"    background-color: #1e1e1e;\n"
"    color: #888888;\n"
"}\n"
"")
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName(u"actionsave")
        self.actionload = QAction(MainWindow)
        self.actionload.setObjectName(u"actionload")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QMainWindow, QWidget {\n"
"    background-color: #1e1e1e;\n"
"    color: #d4d4d4;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #2d2d30;\n"
"    color: #ffffff;\n"
"    border: 1px solid #3c3c3c;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c3c3c;\n"
"    border: 1px solid #5a5a5a;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2a2a2a;\n"
"    border: 1px solid #0078d7;  /* Accent blue */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #d4d4d4;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: #2d2d30;\n"
"    color: #ffffff;\n"
"    border: 1px solid #3c3c3c;\n"
"    border-radius: 4px;\n"
"    padding: 4px 8px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #5a5a5a;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 1px solid #333;\n"
"    border-radius: 6px;\n"
"    margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox:title {\n"
"    subcontrol-origin"
                        ": margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 5px;\n"
"    color: #aaaaaa;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QLineEdit, QTextEdit {\n"
"    background-color: #2d2d30;\n"
"    border: 1px solid #444;\n"
"    color: #ffffff;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QStatusBar {\n"
"    background-color: #1e1e1e;\n"
"    color: #888888;\n"
"}\n"
"")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 20, 241, 261))
        font = QFont()
        font.setFamilies([u"Segoe UI,sans-serif"])
        self.groupBox.setFont(font)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 71, 16))
        self.label.setFont(font)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 30, 81, 16))
        self.label_2.setFont(font)
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(140, 90, 81, 16))
        self.label_7.setFont(font)
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 90, 81, 16))
        self.label_8.setFont(font)
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
        self.comboBox_14.setGeometry(QRect(140, 50, 73, 22))
        self.comboBox_14.setFont(font)
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
        self.comboBox_13.setGeometry(QRect(140, 110, 73, 22))
        self.comboBox_13.setFont(font)
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
        self.comboBox_12.setGeometry(QRect(30, 50, 73, 22))
        self.comboBox_12.setFont(font)
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
        self.comboBox_7.setGeometry(QRect(30, 110, 73, 22))
        self.comboBox_7.setFont(font)
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
        self.comboBox_22.setGeometry(QRect(30, 160, 73, 22))
        self.comboBox_22.setFont(font)
        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(140, 140, 81, 16))
        self.label_17.setFont(font)
        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(30, 140, 71, 16))
        self.label_18.setFont(font)
        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(140, 200, 81, 16))
        self.label_19.setFont(font)
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
        self.comboBox_23.setGeometry(QRect(140, 220, 73, 22))
        self.comboBox_23.setFont(font)
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
        self.comboBox_24.setGeometry(QRect(30, 220, 73, 22))
        self.comboBox_24.setFont(font)
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
        self.comboBox_25.setGeometry(QRect(140, 160, 73, 22))
        self.comboBox_25.setFont(font)
        self.label_20 = QLabel(self.groupBox)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(30, 200, 81, 16))
        self.label_20.setFont(font)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(260, 30, 131, 251))
        self.groupBox_2.setFont(font)
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 30, 91, 16))
        self.label_9.setFont(font)
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 130, 81, 16))
        self.label_10.setFont(font)
        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(30, 190, 81, 16))
        self.label_15.setFont(font)
        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(30, 80, 91, 16))
        self.label_16.setFont(font)
        self.comboBox_18 = QComboBox(self.groupBox_2)
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.setObjectName(u"comboBox_18")
        self.comboBox_18.setGeometry(QRect(30, 150, 73, 22))
        self.comboBox_18.setFont(font)
        self.comboBox_19 = QComboBox(self.groupBox_2)
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.setObjectName(u"comboBox_19")
        self.comboBox_19.setGeometry(QRect(30, 210, 73, 22))
        self.comboBox_19.setFont(font)
        self.comboBox_20 = QComboBox(self.groupBox_2)
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.setObjectName(u"comboBox_20")
        self.comboBox_20.setGeometry(QRect(30, 50, 73, 22))
        self.comboBox_20.setFont(font)
        self.comboBox_21 = QComboBox(self.groupBox_2)
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.setObjectName(u"comboBox_21")
        self.comboBox_21.setGeometry(QRect(30, 100, 73, 22))
        self.comboBox_21.setFont(font)
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(410, 130, 131, 151))
        self.groupBox_3.setFont(font)
        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 30, 91, 16))
        self.label_11.setFont(font)
        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(30, 80, 91, 16))
        self.label_22.setFont(font)
        self.comboBox_28 = QComboBox(self.groupBox_3)
        self.comboBox_28.addItem("")
        self.comboBox_28.addItem("")
        self.comboBox_28.addItem("")
        self.comboBox_28.setObjectName(u"comboBox_28")
        self.comboBox_28.setGeometry(QRect(30, 50, 73, 22))
        self.comboBox_28.setFont(font)
        self.comboBox_29 = QComboBox(self.groupBox_3)
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.setObjectName(u"comboBox_29")
        self.comboBox_29.setGeometry(QRect(30, 100, 73, 22))
        self.comboBox_29.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(420, 50, 91, 51))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QWidget {\n"
"    background-image: url(:/images/bg.jpg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.label_3.setPixmap(QPixmap(u"../../Users/nikhi/Downloads/Untitled.png"))
        self.label_3.setScaledContents(True)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 300, 181, 61))
        self.pushButton.setFont(font)
        icon = QIcon()
        icon.addFile(u"../../Users/nikhi/Downloads/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(50, 50))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 560, 23))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar_2)

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
        self.comboBox_18.setItemText(0, QCoreApplication.translate("MainWindow", u"LB", None))
        self.comboBox_18.setItemText(1, QCoreApplication.translate("MainWindow", u"HB", None))
        self.comboBox_18.setItemText(2, QCoreApplication.translate("MainWindow", u"DRL/POL", None))
        self.comboBox_18.setItemText(3, QCoreApplication.translate("MainWindow", u"TI", None))
        self.comboBox_18.setItemText(4, QCoreApplication.translate("MainWindow", u"Animation", None))
        self.comboBox_18.setItemText(5, QCoreApplication.translate("MainWindow", u"Stop", None))
        self.comboBox_18.setItemText(6, QCoreApplication.translate("MainWindow", u"Tail", None))
        self.comboBox_18.setItemText(7, QCoreApplication.translate("MainWindow", u"Side Marker", None))
        self.comboBox_18.setItemText(8, QCoreApplication.translate("MainWindow", u"Seq TI", None))

        self.comboBox_19.setItemText(0, QCoreApplication.translate("MainWindow", u"LB", None))
        self.comboBox_19.setItemText(1, QCoreApplication.translate("MainWindow", u"HB", None))
        self.comboBox_19.setItemText(2, QCoreApplication.translate("MainWindow", u"DRL/POL", None))
        self.comboBox_19.setItemText(3, QCoreApplication.translate("MainWindow", u"TI", None))
        self.comboBox_19.setItemText(4, QCoreApplication.translate("MainWindow", u"Animation", None))
        self.comboBox_19.setItemText(5, QCoreApplication.translate("MainWindow", u"Stop", None))
        self.comboBox_19.setItemText(6, QCoreApplication.translate("MainWindow", u"Tail", None))
        self.comboBox_19.setItemText(7, QCoreApplication.translate("MainWindow", u"Side Marker", None))
        self.comboBox_19.setItemText(8, QCoreApplication.translate("MainWindow", u"Seq TI", None))

        self.comboBox_20.setItemText(0, QCoreApplication.translate("MainWindow", u"LB", None))
        self.comboBox_20.setItemText(1, QCoreApplication.translate("MainWindow", u"HB", None))
        self.comboBox_20.setItemText(2, QCoreApplication.translate("MainWindow", u"DRL/POL", None))
        self.comboBox_20.setItemText(3, QCoreApplication.translate("MainWindow", u"TI", None))
        self.comboBox_20.setItemText(4, QCoreApplication.translate("MainWindow", u"Animation", None))
        self.comboBox_20.setItemText(5, QCoreApplication.translate("MainWindow", u"Stop", None))
        self.comboBox_20.setItemText(6, QCoreApplication.translate("MainWindow", u"Tail", None))
        self.comboBox_20.setItemText(7, QCoreApplication.translate("MainWindow", u"Side Marker", None))
        self.comboBox_20.setItemText(8, QCoreApplication.translate("MainWindow", u"Seq TI", None))

        self.comboBox_21.setItemText(0, QCoreApplication.translate("MainWindow", u"LB", None))
        self.comboBox_21.setItemText(1, QCoreApplication.translate("MainWindow", u"HB", None))
        self.comboBox_21.setItemText(2, QCoreApplication.translate("MainWindow", u"DRL/POL", None))
        self.comboBox_21.setItemText(3, QCoreApplication.translate("MainWindow", u"TI", None))
        self.comboBox_21.setItemText(4, QCoreApplication.translate("MainWindow", u"Animation", None))
        self.comboBox_21.setItemText(5, QCoreApplication.translate("MainWindow", u"Stop", None))
        self.comboBox_21.setItemText(6, QCoreApplication.translate("MainWindow", u"Tail", None))
        self.comboBox_21.setItemText(7, QCoreApplication.translate("MainWindow", u"Side Marker", None))
        self.comboBox_21.setItemText(8, QCoreApplication.translate("MainWindow", u"Seq TI", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Project Details", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"MLD Typs", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Lamp Type", None))
        self.comboBox_28.setItemText(0, QCoreApplication.translate("MainWindow", u"MINI", None))
        self.comboBox_28.setItemText(1, QCoreApplication.translate("MainWindow", u"STD", None))
        self.comboBox_28.setItemText(2, QCoreApplication.translate("MainWindow", u"PLUS", None))

        self.comboBox_29.setItemText(0, QCoreApplication.translate("MainWindow", u"Tail Lamp", None))
        self.comboBox_29.setItemText(1, QCoreApplication.translate("MainWindow", u"Head Lamp", None))
        self.comboBox_29.setItemText(2, QCoreApplication.translate("MainWindow", u"Car Body", None))

        self.label_3.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start Test", None))
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"file", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
    # retranslateUi

