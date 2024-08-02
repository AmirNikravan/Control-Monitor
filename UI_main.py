# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QMainWindow,
    QMenuBar, QSizePolicy, QStackedWidget, QStatusBar,
    QToolButton, QVBoxLayout, QWidget)

from AnalogGaugeWidget import AnalogGaugeWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(646, 480)
        MainWindow.setStyleSheet(u"background-color: rgb(191, 191, 191);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(224, 224, 224);")
        self.speed = QWidget()
        self.speed.setObjectName(u"speed")
        self.speed.setStyleSheet(u"QToolButton{\n"
"background-color: rgb(91, 122, 208);\n"
"border-radius :5px;\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.speed)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = AnalogGaugeWidget(self.speed)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_3.addWidget(self.widget)

        self.groupBox = QGroupBox(self.speed)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolButton_speed1 = QToolButton(self.groupBox)
        self.toolButton_speed1.setObjectName(u"toolButton_speed1")
        self.toolButton_speed1.setMinimumSize(QSize(75, 75))
        font = QFont()
        font.setFamilies([u"IRANSansXFaNum"])
        font.setPointSize(12)
        font.setBold(True)
        self.toolButton_speed1.setFont(font)

        self.horizontalLayout.addWidget(self.toolButton_speed1)

        self.toolButton_speed2 = QToolButton(self.groupBox)
        self.toolButton_speed2.setObjectName(u"toolButton_speed2")
        self.toolButton_speed2.setMinimumSize(QSize(75, 75))
        self.toolButton_speed2.setFont(font)

        self.horizontalLayout.addWidget(self.toolButton_speed2)

        self.toolButton_speed3 = QToolButton(self.groupBox)
        self.toolButton_speed3.setObjectName(u"toolButton_speed3")
        self.toolButton_speed3.setMinimumSize(QSize(75, 75))
        self.toolButton_speed3.setFont(font)

        self.horizontalLayout.addWidget(self.toolButton_speed3)

        self.toolButton_speed4 = QToolButton(self.groupBox)
        self.toolButton_speed4.setObjectName(u"toolButton_speed4")
        self.toolButton_speed4.setMinimumSize(QSize(75, 75))
        self.toolButton_speed4.setFont(font)

        self.horizontalLayout.addWidget(self.toolButton_speed4)

        self.toolButton_speed5 = QToolButton(self.groupBox)
        self.toolButton_speed5.setObjectName(u"toolButton_speed5")
        self.toolButton_speed5.setMinimumSize(QSize(75, 75))
        self.toolButton_speed5.setFont(font)

        self.horizontalLayout.addWidget(self.toolButton_speed5)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.toolButton_speed6 = QToolButton(self.groupBox)
        self.toolButton_speed6.setObjectName(u"toolButton_speed6")
        self.toolButton_speed6.setMinimumSize(QSize(75, 75))
        self.toolButton_speed6.setFont(font)

        self.horizontalLayout_2.addWidget(self.toolButton_speed6)

        self.toolButton_speed7 = QToolButton(self.groupBox)
        self.toolButton_speed7.setObjectName(u"toolButton_speed7")
        self.toolButton_speed7.setMinimumSize(QSize(75, 75))
        self.toolButton_speed7.setFont(font)

        self.horizontalLayout_2.addWidget(self.toolButton_speed7)

        self.toolButton_speed8 = QToolButton(self.groupBox)
        self.toolButton_speed8.setObjectName(u"toolButton_speed8")
        self.toolButton_speed8.setMinimumSize(QSize(75, 75))
        self.toolButton_speed8.setFont(font)

        self.horizontalLayout_2.addWidget(self.toolButton_speed8)

        self.toolButton_speed9 = QToolButton(self.groupBox)
        self.toolButton_speed9.setObjectName(u"toolButton_speed9")
        self.toolButton_speed9.setMinimumSize(QSize(75, 75))
        self.toolButton_speed9.setFont(font)

        self.horizontalLayout_2.addWidget(self.toolButton_speed9)

        self.toolButton_speed10 = QToolButton(self.groupBox)
        self.toolButton_speed10.setObjectName(u"toolButton_speed10")
        self.toolButton_speed10.setMinimumSize(QSize(75, 75))
        self.toolButton_speed10.setFont(font)

        self.horizontalLayout_2.addWidget(self.toolButton_speed10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.toolButton = QToolButton(self.groupBox)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(125, 50))
        self.toolButton.setFont(font)

        self.horizontalLayout_4.addWidget(self.toolButton)

        self.toolButton_2 = QToolButton(self.groupBox)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setMinimumSize(QSize(125, 50))
        self.toolButton_2.setFont(font)

        self.horizontalLayout_4.addWidget(self.toolButton_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.speed)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.toolButton_3 = QToolButton(self.groupBox_2)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setMinimumSize(QSize(100, 50))
        self.toolButton_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.toolButton_3)

        self.toolButton_4 = QToolButton(self.groupBox_2)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setMinimumSize(QSize(100, 50))
        self.toolButton_4.setFont(font)

        self.horizontalLayout_3.addWidget(self.toolButton_4)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.stackedWidget.addWidget(self.speed)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 646, 18))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.toolButton_speed1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.toolButton_speed2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.toolButton_speed3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.toolButton_speed4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.toolButton_speed5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.toolButton_speed6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.toolButton_speed7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.toolButton_speed8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.toolButton_speed9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.toolButton_speed10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"Increase Speed", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"Decrease Speed", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Start", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

