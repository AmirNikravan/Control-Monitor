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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QToolButton, QVBoxLayout,
    QWidget)

from AnalogGaugeWidget import AnalogGaugeWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(697, 607)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"background-color: rgb(191, 191, 191);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_7 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 39))
        self.widget.setStyleSheet(u"background-color: rgb(241, 242, 243);")
        self.horizontalLayout_8 = QHBoxLayout(self.widget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"IRANSansXFaNum"])
        font.setPointSize(11)
        font.setBold(True)
        self.label_2.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_2)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"IRANSansXFaNum"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label)


        self.verticalLayout.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(224, 224, 224);")
        self.testbed = QWidget()
        self.testbed.setObjectName(u"testbed")
        self.testbed.setStyleSheet(u"QToolButton{\n"
"background-color: rgb(91, 122, 208);\n"
"border-radius :5px;\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.testbed)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(6, 6, -1, -1)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.rpm_gauge = AnalogGaugeWidget(self.testbed)
        self.rpm_gauge.setObjectName(u"rpm_gauge")
        self.rpm_gauge.setMinimumSize(QSize(300, 183))

        self.verticalLayout_5.addWidget(self.rpm_gauge)

        self.label_4 = QLabel(self.testbed)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QSize(16777215, 22))
        font2 = QFont()
        font2.setFamilies([u"IRANSansXV Light"])
        font2.setPointSize(10)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.speed_gauge = AnalogGaugeWidget(self.testbed)
        self.speed_gauge.setObjectName(u"speed_gauge")
        self.speed_gauge.setMinimumSize(QSize(300, 183))

        self.verticalLayout_3.addWidget(self.speed_gauge)

        self.label_3 = QLabel(self.testbed)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMaximumSize(QSize(16777215, 22))
        font3 = QFont()
        font3.setFamilies([u"IRANSansXV Light"])
        font3.setPointSize(11)
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.groupBox = QGroupBox(self.testbed)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font1)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolButton_speed1 = QToolButton(self.groupBox)
        self.toolButton_speed1.setObjectName(u"toolButton_speed1")
        self.toolButton_speed1.setMinimumSize(QSize(75, 75))
        self.toolButton_speed1.setFont(font1)

        self.horizontalLayout.addWidget(self.toolButton_speed1)

        self.toolButton_speed2 = QToolButton(self.groupBox)
        self.toolButton_speed2.setObjectName(u"toolButton_speed2")
        self.toolButton_speed2.setMinimumSize(QSize(75, 75))
        self.toolButton_speed2.setFont(font1)

        self.horizontalLayout.addWidget(self.toolButton_speed2)

        self.toolButton_speed3 = QToolButton(self.groupBox)
        self.toolButton_speed3.setObjectName(u"toolButton_speed3")
        self.toolButton_speed3.setMinimumSize(QSize(75, 75))
        self.toolButton_speed3.setFont(font1)

        self.horizontalLayout.addWidget(self.toolButton_speed3)

        self.toolButton_speed4 = QToolButton(self.groupBox)
        self.toolButton_speed4.setObjectName(u"toolButton_speed4")
        self.toolButton_speed4.setMinimumSize(QSize(75, 75))
        self.toolButton_speed4.setFont(font1)

        self.horizontalLayout.addWidget(self.toolButton_speed4)

        self.toolButton_speed5 = QToolButton(self.groupBox)
        self.toolButton_speed5.setObjectName(u"toolButton_speed5")
        self.toolButton_speed5.setMinimumSize(QSize(75, 75))
        self.toolButton_speed5.setFont(font1)

        self.horizontalLayout.addWidget(self.toolButton_speed5)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.toolButton_speed6 = QToolButton(self.groupBox)
        self.toolButton_speed6.setObjectName(u"toolButton_speed6")
        self.toolButton_speed6.setMinimumSize(QSize(75, 75))
        self.toolButton_speed6.setFont(font1)

        self.horizontalLayout_2.addWidget(self.toolButton_speed6)

        self.toolButton_speed7 = QToolButton(self.groupBox)
        self.toolButton_speed7.setObjectName(u"toolButton_speed7")
        self.toolButton_speed7.setMinimumSize(QSize(75, 75))
        self.toolButton_speed7.setFont(font1)

        self.horizontalLayout_2.addWidget(self.toolButton_speed7)

        self.toolButton_speed8 = QToolButton(self.groupBox)
        self.toolButton_speed8.setObjectName(u"toolButton_speed8")
        self.toolButton_speed8.setMinimumSize(QSize(75, 75))
        self.toolButton_speed8.setFont(font1)

        self.horizontalLayout_2.addWidget(self.toolButton_speed8)

        self.toolButton_speed9 = QToolButton(self.groupBox)
        self.toolButton_speed9.setObjectName(u"toolButton_speed9")
        self.toolButton_speed9.setMinimumSize(QSize(75, 75))
        self.toolButton_speed9.setFont(font1)

        self.horizontalLayout_2.addWidget(self.toolButton_speed9)

        self.toolButton_speed10 = QToolButton(self.groupBox)
        self.toolButton_speed10.setObjectName(u"toolButton_speed10")
        self.toolButton_speed10.setMinimumSize(QSize(75, 75))
        self.toolButton_speed10.setFont(font1)

        self.horizontalLayout_2.addWidget(self.toolButton_speed10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.toolButton_increase = QToolButton(self.groupBox)
        self.toolButton_increase.setObjectName(u"toolButton_increase")
        self.toolButton_increase.setMinimumSize(QSize(125, 50))
        self.toolButton_increase.setFont(font1)

        self.horizontalLayout_4.addWidget(self.toolButton_increase)

        self.toolButton_decrease = QToolButton(self.groupBox)
        self.toolButton_decrease.setObjectName(u"toolButton_decrease")
        self.toolButton_decrease.setMinimumSize(QSize(125, 50))
        self.toolButton_decrease.setFont(font1)

        self.horizontalLayout_4.addWidget(self.toolButton_decrease)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.testbed)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font1)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.toolButton_start = QToolButton(self.groupBox_2)
        self.toolButton_start.setObjectName(u"toolButton_start")
        self.toolButton_start.setMinimumSize(QSize(100, 50))
        self.toolButton_start.setFont(font1)

        self.horizontalLayout_3.addWidget(self.toolButton_start)

        self.toolButton_emgstop = QToolButton(self.groupBox_2)
        self.toolButton_emgstop.setObjectName(u"toolButton_emgstop")
        self.toolButton_emgstop.setMinimumSize(QSize(99, 50))
        self.toolButton_emgstop.setFont(font1)
        self.toolButton_emgstop.setStyleSheet(u"background-color: rgb(255, 1, 5);")

        self.horizontalLayout_3.addWidget(self.toolButton_emgstop)

        self.toolButton_stop = QToolButton(self.groupBox_2)
        self.toolButton_stop.setObjectName(u"toolButton_stop")
        self.toolButton_stop.setMinimumSize(QSize(100, 50))
        self.toolButton_stop.setFont(font1)

        self.horizontalLayout_3.addWidget(self.toolButton_stop)

        self.toolButton_reset = QToolButton(self.groupBox_2)
        self.toolButton_reset.setObjectName(u"toolButton_reset")
        self.toolButton_reset.setMinimumSize(QSize(100, 50))
        self.toolButton_reset.setFont(font1)

        self.horizontalLayout_3.addWidget(self.toolButton_reset)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_6.addWidget(self.groupBox_2)

        self.stackedWidget.addWidget(self.testbed)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(80, 0))
        self.widget_2.setStyleSheet(u"QWidget{background-color: rgb(110, 140, 204);}\n"
"QToolButton{\n"
"background-color: rgb(255, 182, 93);\n"
"\n"
"border-radius :5px;\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.toolButton_testbed = QToolButton(self.widget_2)
        self.toolButton_testbed.setObjectName(u"toolButton_testbed")
        self.toolButton_testbed.setMinimumSize(QSize(75, 25))
        self.toolButton_testbed.setMaximumSize(QSize(60, 25))
        font4 = QFont()
        font4.setFamilies([u"IRANSansXFaNum"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.toolButton_testbed.setFont(font4)

        self.verticalLayout_4.addWidget(self.toolButton_testbed)

        self.toolButton_temperature = QToolButton(self.widget_2)
        self.toolButton_temperature.setObjectName(u"toolButton_temperature")
        self.toolButton_temperature.setMinimumSize(QSize(75, 25))
        self.toolButton_temperature.setMaximumSize(QSize(60, 25))
        self.toolButton_temperature.setFont(font4)

        self.verticalLayout_4.addWidget(self.toolButton_temperature)

        self.toolButton_pressure = QToolButton(self.widget_2)
        self.toolButton_pressure.setObjectName(u"toolButton_pressure")
        self.toolButton_pressure.setMinimumSize(QSize(75, 25))
        self.toolButton_pressure.setMaximumSize(QSize(60, 25))
        self.toolButton_pressure.setFont(font4)

        self.verticalLayout_4.addWidget(self.toolButton_pressure)

        self.toolButton_keys = QToolButton(self.widget_2)
        self.toolButton_keys.setObjectName(u"toolButton_keys")
        self.toolButton_keys.setMinimumSize(QSize(75, 25))
        self.toolButton_keys.setMaximumSize(QSize(60, 25))
        self.toolButton_keys.setFont(font4)

        self.verticalLayout_4.addWidget(self.toolButton_keys)


        self.horizontalLayout_7.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 697, 18))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u062f\u0631\u0641\u0634", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0627\u0645\u0648\u0634", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u" \u0648\u0636\u0639\u06cc\u062a \u0645\u0648\u062a\u0648\u0631 :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0648\u0631 \u0645\u0648\u062a\u0648\u0631", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0631\u0639\u062a", None))
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
        self.toolButton_increase.setText(QCoreApplication.translate("MainWindow", u"Increase Speed", None))
        self.toolButton_decrease.setText(QCoreApplication.translate("MainWindow", u"Decrease Speed", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Start", None))
        self.toolButton_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.toolButton_emgstop.setText(QCoreApplication.translate("MainWindow", u"EMG STOP", None))
        self.toolButton_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.toolButton_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.toolButton_testbed.setText(QCoreApplication.translate("MainWindow", u"test bed", None))
        self.toolButton_temperature.setText(QCoreApplication.translate("MainWindow", u"temperature", None))
        self.toolButton_pressure.setText(QCoreApplication.translate("MainWindow", u"Pressure", None))
        self.toolButton_keys.setText(QCoreApplication.translate("MainWindow", u"keys", None))
    # retranslateUi

