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
        MainWindow.resize(724, 773)
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

        self.groupBox_3 = QGroupBox(self.testbed)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 130))
        self.groupBox_3.setFont(font1)
        self.horizontalLayout_14 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_5 = QSpacerItem(90, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_5)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(4)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.lamp_start_testbed = QLabel(self.groupBox_3)
        self.lamp_start_testbed.setObjectName(u"lamp_start_testbed")
        self.lamp_start_testbed.setMinimumSize(QSize(62, 0))
        self.lamp_start_testbed.setStyleSheet(u"    QLabel {\n"
"\n"
"	background-color: rgb(117, 117, 117);\n"
"                border-style: outset;\n"
"                border-width: 1px;\n"
"                border-radius: 30px;\n"
"        }")

        self.verticalLayout_27.addWidget(self.lamp_start_testbed)

        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(80, 13))
        font4 = QFont()
        font4.setFamilies([u"IRANSansXFaNum Black"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.label_25.setFont(font4)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_25)


        self.horizontalLayout_14.addLayout(self.verticalLayout_27)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.lamp_stop_testbed = QLabel(self.groupBox_3)
        self.lamp_stop_testbed.setObjectName(u"lamp_stop_testbed")
        self.lamp_stop_testbed.setMinimumSize(QSize(62, 0))
        self.lamp_stop_testbed.setStyleSheet(u"    QLabel {\n"
"\n"
"	background-color: rgb(117, 117, 117);\n"
"                border-style: outset;\n"
"                border-width: 1px;\n"
"                border-radius: 30px;\n"
"        }")

        self.verticalLayout_28.addWidget(self.lamp_stop_testbed)

        self.label_27 = QLabel(self.groupBox_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(83, 13))
        self.label_27.setFont(font4)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_27)


        self.horizontalLayout_14.addLayout(self.verticalLayout_28)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.lamp_emgstop_testbed = QLabel(self.groupBox_3)
        self.lamp_emgstop_testbed.setObjectName(u"lamp_emgstop_testbed")
        self.lamp_emgstop_testbed.setMinimumSize(QSize(62, 0))
        self.lamp_emgstop_testbed.setStyleSheet(u"    QLabel {\n"
"\n"
"	background-color: rgb(117, 117, 117);\n"
"                border-style: outset;\n"
"                border-width: 1px;\n"
"                border-radius: 30px;\n"
"        }")

        self.verticalLayout_29.addWidget(self.lamp_emgstop_testbed)

        self.label_29 = QLabel(self.groupBox_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(83, 13))
        self.label_29.setFont(font4)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_29)


        self.horizontalLayout_14.addLayout(self.verticalLayout_29)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.lamp_increase_testbed = QLabel(self.groupBox_3)
        self.lamp_increase_testbed.setObjectName(u"lamp_increase_testbed")
        self.lamp_increase_testbed.setMinimumSize(QSize(62, 0))
        self.lamp_increase_testbed.setStyleSheet(u"    QLabel {\n"
"\n"
"	background-color: rgb(117, 117, 117);\n"
"                border-style: outset;\n"
"                border-width: 1px;\n"
"                border-radius: 30px;\n"
"        }")

        self.verticalLayout_30.addWidget(self.lamp_increase_testbed)

        self.label_31 = QLabel(self.groupBox_3)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(83, 13))
        self.label_31.setFont(font4)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_31)


        self.horizontalLayout_14.addLayout(self.verticalLayout_30)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.lamp_decrease_test_bed = QLabel(self.groupBox_3)
        self.lamp_decrease_test_bed.setObjectName(u"lamp_decrease_test_bed")
        self.lamp_decrease_test_bed.setMinimumSize(QSize(62, 0))
        self.lamp_decrease_test_bed.setStyleSheet(u"    QLabel {\n"
"\n"
"	background-color: rgb(117, 117, 117);\n"
"                border-style: outset;\n"
"                border-width: 1px;\n"
"                border-radius: 30px;\n"
"        }")

        self.verticalLayout_31.addWidget(self.lamp_decrease_test_bed)

        self.label_33 = QLabel(self.groupBox_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(80, 13))
        self.label_33.setFont(font4)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_33)


        self.horizontalLayout_14.addLayout(self.verticalLayout_31)

        self.horizontalSpacer_6 = QSpacerItem(90, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_6)


        self.verticalLayout_6.addWidget(self.groupBox_3)

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
        self.temperature = QWidget()
        self.temperature.setObjectName(u"temperature")
        self.verticalLayout_20 = QVBoxLayout(self.temperature)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_5 = QLabel(self.temperature)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 12))
        self.label_5.setMaximumSize(QSize(16777215, 28))
        font5 = QFont()
        font5.setFamilies([u"IRANSansXFaNum"])
        font5.setPointSize(14)
        font5.setBold(True)
        self.label_5.setFont(font5)

        self.verticalLayout_20.addWidget(self.label_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.exhuast_bank_a_temp_gauge = AnalogGaugeWidget(self.temperature)
        self.exhuast_bank_a_temp_gauge.setObjectName(u"exhuast_bank_a_temp_gauge")

        self.verticalLayout_7.addWidget(self.exhuast_bank_a_temp_gauge)

        self.label_6 = QLabel(self.temperature)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 19))
        font6 = QFont()
        font6.setFamilies([u"IRANSansXFaNum"])
        font6.setPointSize(10)
        font6.setBold(True)
        self.label_6.setFont(font6)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.exhuast_bank_b_temp_gauge = AnalogGaugeWidget(self.temperature)
        self.exhuast_bank_b_temp_gauge.setObjectName(u"exhuast_bank_b_temp_gauge")

        self.verticalLayout_11.addWidget(self.exhuast_bank_b_temp_gauge)

        self.exhuast_bank_b_gauge = QLabel(self.temperature)
        self.exhuast_bank_b_gauge.setObjectName(u"exhuast_bank_b_gauge")
        self.exhuast_bank_b_gauge.setMaximumSize(QSize(16777215, 19))
        self.exhuast_bank_b_gauge.setFont(font6)
        self.exhuast_bank_b_gauge.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.exhuast_bank_b_gauge)


        self.horizontalLayout_9.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.airboost_bank_a_temp_gauge = AnalogGaugeWidget(self.temperature)
        self.airboost_bank_a_temp_gauge.setObjectName(u"airboost_bank_a_temp_gauge")

        self.verticalLayout_12.addWidget(self.airboost_bank_a_temp_gauge)

        self.label_11 = QLabel(self.temperature)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 19))
        self.label_11.setFont(font6)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_11)


        self.horizontalLayout_9.addLayout(self.verticalLayout_12)


        self.verticalLayout_20.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.airboost_bank_b_temp_gauge = AnalogGaugeWidget(self.temperature)
        self.airboost_bank_b_temp_gauge.setObjectName(u"airboost_bank_b_temp_gauge")

        self.verticalLayout_13.addWidget(self.airboost_bank_b_temp_gauge)

        self.label_12 = QLabel(self.temperature)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 19))
        self.label_12.setFont(font6)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_12)


        self.horizontalLayout_10.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.oil_temp_gauge = AnalogGaugeWidget(self.temperature)
        self.oil_temp_gauge.setObjectName(u"oil_temp_gauge")

        self.verticalLayout_14.addWidget(self.oil_temp_gauge)

        self.label_10 = QLabel(self.temperature)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 19))
        self.label_10.setFont(font6)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_10)


        self.horizontalLayout_10.addLayout(self.verticalLayout_14)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.oil_ntc_temp_gauge = AnalogGaugeWidget(self.temperature)
        self.oil_ntc_temp_gauge.setObjectName(u"oil_ntc_temp_gauge")

        self.verticalLayout_16.addWidget(self.oil_ntc_temp_gauge)

        self.label_15 = QLabel(self.temperature)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 19))
        self.label_15.setFont(font6)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_15)


        self.horizontalLayout_10.addLayout(self.verticalLayout_16)


        self.verticalLayout_20.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.freshwater_afterthermo_temp_gauge = AnalogGaugeWidget(self.temperature)
        self.freshwater_afterthermo_temp_gauge.setObjectName(u"freshwater_afterthermo_temp_gauge")

        self.verticalLayout_17.addWidget(self.freshwater_afterthermo_temp_gauge)

        self.label_16 = QLabel(self.temperature)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 19))
        self.label_16.setFont(font6)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_16)


        self.horizontalLayout_11.addLayout(self.verticalLayout_17)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.freshwater_beforethermo_temp_gauge = AnalogGaugeWidget(self.temperature)
        self.freshwater_beforethermo_temp_gauge.setObjectName(u"freshwater_beforethermo_temp_gauge")

        self.verticalLayout_18.addWidget(self.freshwater_beforethermo_temp_gauge)

        self.label_17 = QLabel(self.temperature)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 19))
        self.label_17.setFont(font6)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_17)


        self.horizontalLayout_11.addLayout(self.verticalLayout_18)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.sea_water_temp_gauge = AnalogGaugeWidget(self.temperature)
        self.sea_water_temp_gauge.setObjectName(u"sea_water_temp_gauge")

        self.verticalLayout_19.addWidget(self.sea_water_temp_gauge)

        self.label_18 = QLabel(self.temperature)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 19))
        self.label_18.setFont(font6)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_18)


        self.horizontalLayout_11.addLayout(self.verticalLayout_19)


        self.verticalLayout_20.addLayout(self.horizontalLayout_11)

        self.stackedWidget.addWidget(self.temperature)
        self.pressure = QWidget()
        self.pressure.setObjectName(u"pressure")
        self.verticalLayout_26 = QVBoxLayout(self.pressure)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_13 = QLabel(self.pressure)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 28))
        self.label_13.setFont(font5)

        self.verticalLayout_26.addWidget(self.label_13)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.oil_pressure_gauge = AnalogGaugeWidget(self.pressure)
        self.oil_pressure_gauge.setObjectName(u"oil_pressure_gauge")
        self.oil_pressure_gauge.setMaximumSize(QSize(16777215, 220))

        self.verticalLayout_21.addWidget(self.oil_pressure_gauge)

        self.label_19 = QLabel(self.pressure)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 19))
        self.label_19.setFont(font6)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_19)


        self.horizontalLayout_12.addLayout(self.verticalLayout_21)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.oil_switch_pressure_gauge = AnalogGaugeWidget(self.pressure)
        self.oil_switch_pressure_gauge.setObjectName(u"oil_switch_pressure_gauge")
        self.oil_switch_pressure_gauge.setMaximumSize(QSize(16777215, 220))

        self.verticalLayout_22.addWidget(self.oil_switch_pressure_gauge)

        self.label_20 = QLabel(self.pressure)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 19))
        self.label_20.setFont(font6)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_20)


        self.horizontalLayout_12.addLayout(self.verticalLayout_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.airboost_pressure_gauge = AnalogGaugeWidget(self.pressure)
        self.airboost_pressure_gauge.setObjectName(u"airboost_pressure_gauge")
        self.airboost_pressure_gauge.setMaximumSize(QSize(16777215, 220))

        self.verticalLayout_23.addWidget(self.airboost_pressure_gauge)

        self.label_21 = QLabel(self.pressure)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 19))
        self.label_21.setFont(font6)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_21)


        self.horizontalLayout_12.addLayout(self.verticalLayout_23)


        self.verticalLayout_26.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.sea_water_pressure_gauge = AnalogGaugeWidget(self.pressure)
        self.sea_water_pressure_gauge.setObjectName(u"sea_water_pressure_gauge")
        self.sea_water_pressure_gauge.setMinimumSize(QSize(196, 0))
        self.sea_water_pressure_gauge.setMaximumSize(QSize(16777215, 220))

        self.verticalLayout_25.addWidget(self.sea_water_pressure_gauge)

        self.label_23 = QLabel(self.pressure)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(16777215, 19))
        self.label_23.setFont(font6)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_23)


        self.horizontalLayout_13.addLayout(self.verticalLayout_25)

        self.horizontalSpacer_4 = QSpacerItem(82, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.fuel_pressure_gauge = AnalogGaugeWidget(self.pressure)
        self.fuel_pressure_gauge.setObjectName(u"fuel_pressure_gauge")
        self.fuel_pressure_gauge.setMinimumSize(QSize(196, 0))
        self.fuel_pressure_gauge.setMaximumSize(QSize(16777215, 220))

        self.verticalLayout_24.addWidget(self.fuel_pressure_gauge)

        self.label_22 = QLabel(self.pressure)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 19))
        self.label_22.setFont(font6)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_22)


        self.horizontalLayout_13.addLayout(self.verticalLayout_24)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)


        self.verticalLayout_26.addLayout(self.horizontalLayout_13)

        self.stackedWidget.addWidget(self.pressure)

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
        self.verticalLayout_4.setContentsMargins(2, 0, 0, 0)
        self.toolButton_testbed = QToolButton(self.widget_2)
        self.toolButton_testbed.setObjectName(u"toolButton_testbed")
        self.toolButton_testbed.setMinimumSize(QSize(75, 25))
        self.toolButton_testbed.setMaximumSize(QSize(60, 25))
        self.toolButton_testbed.setFont(font6)

        self.verticalLayout_4.addWidget(self.toolButton_testbed)

        self.toolButton_temperature = QToolButton(self.widget_2)
        self.toolButton_temperature.setObjectName(u"toolButton_temperature")
        self.toolButton_temperature.setMinimumSize(QSize(75, 25))
        self.toolButton_temperature.setMaximumSize(QSize(60, 25))
        self.toolButton_temperature.setFont(font6)

        self.verticalLayout_4.addWidget(self.toolButton_temperature)

        self.toolButton_pressure = QToolButton(self.widget_2)
        self.toolButton_pressure.setObjectName(u"toolButton_pressure")
        self.toolButton_pressure.setMinimumSize(QSize(75, 25))
        self.toolButton_pressure.setMaximumSize(QSize(60, 25))
        self.toolButton_pressure.setFont(font6)

        self.verticalLayout_4.addWidget(self.toolButton_pressure)

        self.toolButton_keys = QToolButton(self.widget_2)
        self.toolButton_keys.setObjectName(u"toolButton_keys")
        self.toolButton_keys.setMinimumSize(QSize(75, 25))
        self.toolButton_keys.setMaximumSize(QSize(60, 25))
        self.toolButton_keys.setFont(font6)

        self.verticalLayout_4.addWidget(self.toolButton_keys)

        self.toolButton = QToolButton(self.widget_2)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(75, 25))
        self.toolButton.setFont(font6)

        self.verticalLayout_4.addWidget(self.toolButton)


        self.horizontalLayout_7.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 724, 18))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u062f\u0631\u0641\u0634", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0627\u0645\u0648\u0634", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u" \u0648\u0636\u0639\u06cc\u062a \u0645\u0648\u062a\u0648\u0631 :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0648\u0631 \u0645\u0648\u062a\u0648\u0631", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0631\u0639\u062a", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Lamps", None))
        self.lamp_start_testbed.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.lamp_stop_testbed.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.lamp_emgstop_testbed.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"EMG Stop", None))
        self.lamp_increase_testbed.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.lamp_decrease_test_bed.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
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
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0646\u0633\u0648\u0631 \u0647\u0627\u06cc \u062f\u0645\u0627", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Exhuast Bank B", None))
        self.exhuast_bank_b_gauge.setText(QCoreApplication.translate("MainWindow", u"Exhuast Bank A", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Air Boost Bank A", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Air Boost Bank B", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Oil", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Oil NTC", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Fresh Water after Thermostat", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Fresh Water before Thermostat", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Sea Water", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0646\u0633\u0648\u0631 \u0641\u0634\u0627\u0631", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Oil", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Oil Switch", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Air Boost", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Sea Water", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Fuel Pressure", None))
        self.toolButton_testbed.setText(QCoreApplication.translate("MainWindow", u"test bed", None))
        self.toolButton_temperature.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0645\u0627", None))
        self.toolButton_pressure.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0634\u0627\u0631", None))
        self.toolButton_keys.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0644\u06cc\u062f\u0647\u0627", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0627\u06cc\u0631", None))
    # retranslateUi

