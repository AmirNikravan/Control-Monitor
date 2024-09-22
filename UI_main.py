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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QSizePolicy, QSpacerItem,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)

from AnalogGaugeWidget import AnalogGaugeWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(905, 594)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"background-color: rgb(243, 243, 243);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.up_label = QWidget(self.centralwidget)
        self.up_label.setObjectName(u"up_label")
        self.up_label.setMinimumSize(QSize(0, 39))
        self.up_label.setStyleSheet(u"background-color: rgb(241, 242, 243);")
        self.horizontalLayout_8 = QHBoxLayout(self.up_label)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, -1)
        self.label_time = QLabel(self.up_label)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setMinimumSize(QSize(102, 0))
        font = QFont()
        font.setFamilies([u"IRANSansXFaNum"])
        font.setBold(True)
        self.label_time.setFont(font)
        self.label_time.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_time)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.label_engine_name = QLabel(self.up_label)
        self.label_engine_name.setObjectName(u"label_engine_name")
        font1 = QFont()
        font1.setFamilies([u"IRANSansXFaNum"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_engine_name.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_engine_name)

        self.label_3 = QLabel(self.up_label)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.up_label)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"IRANSansXFaNum"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_2.setFont(font2)

        self.horizontalLayout_8.addWidget(self.label_2)

        self.label = QLabel(self.up_label)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label)


        self.verticalLayout.addWidget(self.up_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(221, 221, 221);")
        self.stackedWidget.setLineWidth(0)
        self.shaft = QWidget()
        self.shaft.setObjectName(u"shaft")
        self.shaft.setStyleSheet(u"")
        self.verticalLayout_41 = QVBoxLayout(self.shaft)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.oil_temp_shaft_gauge = AnalogGaugeWidget(self.shaft)
        self.oil_temp_shaft_gauge.setObjectName(u"oil_temp_shaft_gauge")

        self.verticalLayout_28.addWidget(self.oil_temp_shaft_gauge)

        self.label_27 = QLabel(self.shaft)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(16777215, 22))
        font3 = QFont()
        font3.setFamilies([u"IRANSansXFaNum Black"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_27.setFont(font3)
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_27)


        self.horizontalLayout_3.addLayout(self.verticalLayout_28)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.rpm_gauge_shaft = AnalogGaugeWidget(self.shaft)
        self.rpm_gauge_shaft.setObjectName(u"rpm_gauge_shaft")

        self.verticalLayout_29.addWidget(self.rpm_gauge_shaft)

        self.label_25 = QLabel(self.shaft)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 22))
        self.label_25.setFont(font3)
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_25)


        self.horizontalLayout_3.addLayout(self.verticalLayout_29)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.oil_press_shaft_gauge = AnalogGaugeWidget(self.shaft)
        self.oil_press_shaft_gauge.setObjectName(u"oil_press_shaft_gauge")

        self.verticalLayout_30.addWidget(self.oil_press_shaft_gauge)

        self.label_4 = QLabel(self.shaft)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 22))
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_30)


        self.verticalLayout_41.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(23)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_shaft_airflap = QLabel(self.shaft)
        self.label_shaft_airflap.setObjectName(u"label_shaft_airflap")
        self.label_shaft_airflap.setFont(font)
        self.label_shaft_airflap.setStyleSheet(u"            QLabel {\n"
"\n"
"	\n"
"	background-color: rgb(143, 143, 143);\n"
"                color: black;\n"
"                padding: 20px;\n"
"                border-radius: 15px;\n"
"                border: 2px solid rgba(255, 255, 255, 100);\n"
"            }")
        self.label_shaft_airflap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_shaft_airflap)

        self.label_shaft_stop = QLabel(self.shaft)
        self.label_shaft_stop.setObjectName(u"label_shaft_stop")
        self.label_shaft_stop.setFont(font)
        self.label_shaft_stop.setStyleSheet(u"            QLabel {\n"
"\n"
"	\n"
"	background-color: rgb(143, 143, 143);\n"
"                color: black;\n"
"                padding: 20px;\n"
"                border-radius: 15px;\n"
"                border: 2px solid rgba(255, 255, 255, 100);\n"
"            }")
        self.label_shaft_stop.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_shaft_stop)

        self.label_shaft_start = QLabel(self.shaft)
        self.label_shaft_start.setObjectName(u"label_shaft_start")
        self.label_shaft_start.setFont(font)
        self.label_shaft_start.setStyleSheet(u"            QLabel {\n"
"\n"
"	\n"
"	background-color: rgb(143, 143, 143);\n"
"                color: black;\n"
"                padding: 20px;\n"
"                border-radius: 15px;\n"
"                border: 2px solid rgba(255, 255, 255, 100);\n"
"            }")
        self.label_shaft_start.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_shaft_start)

        self.label_shaft_water_level = QLabel(self.shaft)
        self.label_shaft_water_level.setObjectName(u"label_shaft_water_level")
        self.label_shaft_water_level.setFont(font)
        self.label_shaft_water_level.setStyleSheet(u"            QLabel {\n"
"\n"
"	\n"
"	background-color: rgb(143, 143, 143);\n"
"                color: black;\n"
"                padding: 20px;\n"
"                border-radius: 15px;\n"
"                border: 2px solid rgba(255, 255, 255, 100);\n"
"            }")
        self.label_shaft_water_level.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_shaft_water_level)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 2)

        self.verticalLayout_41.addLayout(self.horizontalLayout_2)

        self.stackedWidget.addWidget(self.shaft)
        self.temperature = QWidget()
        self.temperature.setObjectName(u"temperature")
        self.verticalLayout_39 = QVBoxLayout(self.temperature)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_5 = QLabel(self.temperature)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 23))
        self.label_5.setMaximumSize(QSize(16777215, 28))
        font4 = QFont()
        font4.setFamilies([u"IRANSansXFaNum"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.label_5.setFont(font4)

        self.verticalLayout_39.addWidget(self.label_5)

        self.stackedWidget_sensosr = QStackedWidget(self.temperature)
        self.stackedWidget_sensosr.setObjectName(u"stackedWidget_sensosr")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_31 = QVBoxLayout(self.page)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_8 = QSpacerItem(68, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.label_31 = QLabel(self.page)
        self.label_31.setObjectName(u"label_31")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setMaximumSize(QSize(16777215, 27))

        self.horizontalLayout_7.addWidget(self.label_31)


        self.verticalLayout_31.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.exhuast_bank_a_temp_gauge = AnalogGaugeWidget(self.page)
        self.exhuast_bank_a_temp_gauge.setObjectName(u"exhuast_bank_a_temp_gauge")
        self.exhuast_bank_a_temp_gauge.setMinimumSize(QSize(255, 212))
        self.exhuast_bank_a_temp_gauge.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_7.addWidget(self.exhuast_bank_a_temp_gauge)

        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 19))
        font5 = QFont()
        font5.setFamilies([u"IRANSansXFaNum"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.label_6.setFont(font5)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.exhuast_bank_b_temp_gauge = AnalogGaugeWidget(self.page)
        self.exhuast_bank_b_temp_gauge.setObjectName(u"exhuast_bank_b_temp_gauge")
        self.exhuast_bank_b_temp_gauge.setMinimumSize(QSize(255, 212))
        self.exhuast_bank_b_temp_gauge.setMaximumSize(QSize(255, 212))

        self.verticalLayout_11.addWidget(self.exhuast_bank_b_temp_gauge)

        self.exhuast_bank_b_gauge = QLabel(self.page)
        self.exhuast_bank_b_gauge.setObjectName(u"exhuast_bank_b_gauge")
        self.exhuast_bank_b_gauge.setMaximumSize(QSize(16777215, 19))
        self.exhuast_bank_b_gauge.setFont(font5)
        self.exhuast_bank_b_gauge.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.exhuast_bank_b_gauge)


        self.horizontalLayout_9.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.airboost_bank_a_temp_gauge = AnalogGaugeWidget(self.page)
        self.airboost_bank_a_temp_gauge.setObjectName(u"airboost_bank_a_temp_gauge")
        self.airboost_bank_a_temp_gauge.setMinimumSize(QSize(255, 212))
        self.airboost_bank_a_temp_gauge.setMaximumSize(QSize(255, 212))

        self.verticalLayout_12.addWidget(self.airboost_bank_a_temp_gauge)

        self.label_11 = QLabel(self.page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 19))
        self.label_11.setFont(font5)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_11)


        self.horizontalLayout_9.addLayout(self.verticalLayout_12)


        self.verticalLayout_31.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_3 = QSpacerItem(20, 153, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_31.addItem(self.verticalSpacer_3)

        self.stackedWidget_sensosr.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_40 = QVBoxLayout(self.page_3)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_7 = QSpacerItem(68, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.label_30 = QLabel(self.page_3)
        self.label_30.setObjectName(u"label_30")
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setMaximumSize(QSize(16777215, 27))

        self.horizontalLayout_6.addWidget(self.label_30)


        self.verticalLayout_40.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.airboost_bank_b_temp_gauge = AnalogGaugeWidget(self.page_3)
        self.airboost_bank_b_temp_gauge.setObjectName(u"airboost_bank_b_temp_gauge")
        self.airboost_bank_b_temp_gauge.setMinimumSize(QSize(255, 212))
        self.airboost_bank_b_temp_gauge.setMaximumSize(QSize(255, 212))

        self.verticalLayout_13.addWidget(self.airboost_bank_b_temp_gauge)

        self.label_12 = QLabel(self.page_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 19))
        self.label_12.setFont(font5)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_12)


        self.horizontalLayout_10.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.oil_temp_gauge = AnalogGaugeWidget(self.page_3)
        self.oil_temp_gauge.setObjectName(u"oil_temp_gauge")
        self.oil_temp_gauge.setMinimumSize(QSize(255, 212))
        self.oil_temp_gauge.setMaximumSize(QSize(255, 212))

        self.verticalLayout_14.addWidget(self.oil_temp_gauge)

        self.label_10 = QLabel(self.page_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 19))
        self.label_10.setFont(font5)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_10)


        self.horizontalLayout_10.addLayout(self.verticalLayout_14)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.oil_ntc_temp_gauge = AnalogGaugeWidget(self.page_3)
        self.oil_ntc_temp_gauge.setObjectName(u"oil_ntc_temp_gauge")
        self.oil_ntc_temp_gauge.setMinimumSize(QSize(255, 212))
        self.oil_ntc_temp_gauge.setMaximumSize(QSize(255, 212))

        self.verticalLayout_16.addWidget(self.oil_ntc_temp_gauge)

        self.label_15 = QLabel(self.page_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 19))
        self.label_15.setFont(font5)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_15)


        self.horizontalLayout_10.addLayout(self.verticalLayout_16)


        self.verticalLayout_40.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_2 = QSpacerItem(20, 153, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_40.addItem(self.verticalSpacer_2)

        self.stackedWidget_sensosr.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_20 = QVBoxLayout(self.page_2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_6 = QSpacerItem(40, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.label_28 = QLabel(self.page_2)
        self.label_28.setObjectName(u"label_28")
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_28)


        self.verticalLayout_20.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.freshwater_afterthermo_temp_gauge = AnalogGaugeWidget(self.page_2)
        self.freshwater_afterthermo_temp_gauge.setObjectName(u"freshwater_afterthermo_temp_gauge")
        self.freshwater_afterthermo_temp_gauge.setMinimumSize(QSize(255, 212))
        self.freshwater_afterthermo_temp_gauge.setMaximumSize(QSize(255, 212))

        self.verticalLayout_17.addWidget(self.freshwater_afterthermo_temp_gauge)

        self.label_16 = QLabel(self.page_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 19))
        self.label_16.setFont(font5)
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_16)


        self.horizontalLayout_11.addLayout(self.verticalLayout_17)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.freshwater_beforethermo_temp_gauge = AnalogGaugeWidget(self.page_2)
        self.freshwater_beforethermo_temp_gauge.setObjectName(u"freshwater_beforethermo_temp_gauge")
        self.freshwater_beforethermo_temp_gauge.setMinimumSize(QSize(255, 212))
        self.freshwater_beforethermo_temp_gauge.setMaximumSize(QSize(255, 212))

        self.verticalLayout_18.addWidget(self.freshwater_beforethermo_temp_gauge)

        self.label_17 = QLabel(self.page_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 19))
        self.label_17.setFont(font5)
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_17)


        self.horizontalLayout_11.addLayout(self.verticalLayout_18)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.sea_water_temp_gauge = AnalogGaugeWidget(self.page_2)
        self.sea_water_temp_gauge.setObjectName(u"sea_water_temp_gauge")
        self.sea_water_temp_gauge.setMinimumSize(QSize(255, 212))
        self.sea_water_temp_gauge.setMaximumSize(QSize(255, 212))

        self.verticalLayout_19.addWidget(self.sea_water_temp_gauge)

        self.label_18 = QLabel(self.page_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 19))
        self.label_18.setFont(font5)
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_18)


        self.horizontalLayout_11.addLayout(self.verticalLayout_19)


        self.verticalLayout_20.addLayout(self.horizontalLayout_11)

        self.verticalSpacer = QSpacerItem(10, 153, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_20.addItem(self.verticalSpacer)

        self.stackedWidget_sensosr.addWidget(self.page_2)

        self.verticalLayout_39.addWidget(self.stackedWidget_sensosr)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.toolButton_previouspage_sensors = QToolButton(self.temperature)
        self.toolButton_previouspage_sensors.setObjectName(u"toolButton_previouspage_sensors")
        self.toolButton_previouspage_sensors.setMinimumSize(QSize(93, 59))

        self.horizontalLayout_4.addWidget(self.toolButton_previouspage_sensors)

        self.toolButton_nextpage_sensors = QToolButton(self.temperature)
        self.toolButton_nextpage_sensors.setObjectName(u"toolButton_nextpage_sensors")
        self.toolButton_nextpage_sensors.setMinimumSize(QSize(93, 59))

        self.horizontalLayout_4.addWidget(self.toolButton_nextpage_sensors)


        self.verticalLayout_39.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.temperature)
        self.pressure = QWidget()
        self.pressure.setObjectName(u"pressure")
        self.verticalLayout_26 = QVBoxLayout(self.pressure)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_13 = QLabel(self.pressure)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 28))
        self.label_13.setFont(font4)

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
        self.label_19.setFont(font5)
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

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
        self.label_20.setFont(font5)
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

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
        self.label_21.setFont(font5)
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

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
        self.label_23.setFont(font5)
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

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
        self.label_22.setFont(font5)
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_22)


        self.horizontalLayout_13.addLayout(self.verticalLayout_24)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)


        self.verticalLayout_26.addLayout(self.horizontalLayout_13)

        self.stackedWidget.addWidget(self.pressure)
        self.keys = QWidget()
        self.keys.setObjectName(u"keys")
        self.verticalLayout_38 = QVBoxLayout(self.keys)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_7 = QLabel(self.keys)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_38.addWidget(self.label_7)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.lamp_increase = QLabel(self.keys)
        self.lamp_increase.setObjectName(u"lamp_increase")
        self.lamp_increase.setMinimumSize(QSize(62, 0))
        self.lamp_increase.setStyleSheet(u"    QLabel {\n"
"\n"
"\n"
"	background-color: red;\n"
"                border-style: outset;\n"
"                border-width: 1px;\n"
"                border-radius: 30px;\n"
"        }")

        self.verticalLayout_32.addWidget(self.lamp_increase)

        self.label_32 = QLabel(self.keys)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(83, 13))
        font6 = QFont()
        font6.setFamilies([u"IRANSansXFaNum Black"])
        font6.setPointSize(10)
        font6.setBold(True)
        self.label_32.setFont(font6)
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_32)


        self.horizontalLayout_15.addLayout(self.verticalLayout_32)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.lamp_decrease = QLabel(self.keys)
        self.lamp_decrease.setObjectName(u"lamp_decrease")
        self.lamp_decrease.setMinimumSize(QSize(62, 0))
        self.lamp_decrease.setStyleSheet(u"    QLabel {\n"
"\n"
"\n"
"	background-color: red;\n"
"                border-style: outset;\n"
"                border-width: 1px;\n"
"                border-radius: 30px;\n"
"        }")

        self.verticalLayout_33.addWidget(self.lamp_decrease)

        self.label_34 = QLabel(self.keys)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(83, 13))
        self.label_34.setFont(font6)
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_34)


        self.horizontalLayout_15.addLayout(self.verticalLayout_33)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.lamp_start = QLabel(self.keys)
        self.lamp_start.setObjectName(u"lamp_start")
        self.lamp_start.setMinimumSize(QSize(62, 0))
        self.lamp_start.setStyleSheet(u"    QLabel {\n"
"\n"
"\n"
"	background-color: red;\n"
"                border-style: outset;\n"
"                border-width: 1px;\n"
"                border-radius: 30px;\n"
"        }")

        self.verticalLayout_34.addWidget(self.lamp_start)

        self.label_35 = QLabel(self.keys)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(83, 13))
        self.label_35.setFont(font6)
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_35)


        self.horizontalLayout_15.addLayout(self.verticalLayout_34)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.lamp_emgstop = QLabel(self.keys)
        self.lamp_emgstop.setObjectName(u"lamp_emgstop")
        self.lamp_emgstop.setMinimumSize(QSize(62, 0))
        self.lamp_emgstop.setStyleSheet(u"    QLabel {\n"
"\n"
"\n"
"	background-color: red;\n"
"                border-style: outset;\n"
"                border-width: 1px;\n"
"                border-radius: 30px;\n"
"        }")

        self.verticalLayout_35.addWidget(self.lamp_emgstop)

        self.label_36 = QLabel(self.keys)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(83, 13))
        self.label_36.setFont(font6)
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_35.addWidget(self.label_36)


        self.horizontalLayout_15.addLayout(self.verticalLayout_35)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.lamp_stop = QLabel(self.keys)
        self.lamp_stop.setObjectName(u"lamp_stop")
        self.lamp_stop.setMinimumSize(QSize(62, 0))
        self.lamp_stop.setStyleSheet(u"    QLabel {\n"
"\n"
"\n"
"	background-color: red;\n"
"                border-style: outset;\n"
"                border-width: 1px;\n"
"                border-radius: 30px;\n"
"        }")

        self.verticalLayout_36.addWidget(self.lamp_stop)

        self.label_37 = QLabel(self.keys)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(83, 13))
        self.label_37.setFont(font6)
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_37)


        self.horizontalLayout_15.addLayout(self.verticalLayout_36)


        self.verticalLayout_38.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.widget_3 = QWidget(self.keys)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_8 = QVBoxLayout(self.widget_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.increase_key = QToolButton(self.widget_3)
        self.increase_key.setObjectName(u"increase_key")
        self.increase_key.setMinimumSize(QSize(66, 60))
        self.increase_key.setStyleSheet(u"background-color: rgb(158, 255, 226);")

        self.verticalLayout_8.addWidget(self.increase_key)

        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 12))
        self.label_8.setFont(font5)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_8)


        self.horizontalLayout_16.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.keys)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_9 = QVBoxLayout(self.widget_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.decrease_key = QToolButton(self.widget_4)
        self.decrease_key.setObjectName(u"decrease_key")
        self.decrease_key.setMinimumSize(QSize(66, 60))
        self.decrease_key.setStyleSheet(u"background-color: rgb(130, 121, 255);")

        self.verticalLayout_9.addWidget(self.decrease_key)

        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 12))
        self.label_9.setFont(font5)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_9)


        self.horizontalLayout_16.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.keys)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_10 = QVBoxLayout(self.widget_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.start_key = QToolButton(self.widget_5)
        self.start_key.setObjectName(u"start_key")
        self.start_key.setMinimumSize(QSize(66, 60))
        self.start_key.setStyleSheet(u"background-color: rgb(23, 154, 255);")

        self.verticalLayout_10.addWidget(self.start_key)

        self.label_14 = QLabel(self.widget_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 12))
        self.label_14.setFont(font5)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_14)


        self.horizontalLayout_16.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.keys)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_15 = QVBoxLayout(self.widget_6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.emgstop_key = QToolButton(self.widget_6)
        self.emgstop_key.setObjectName(u"emgstop_key")
        self.emgstop_key.setMinimumSize(QSize(66, 60))
        self.emgstop_key.setStyleSheet(u"background-color: rgb(192, 255, 227);")

        self.verticalLayout_15.addWidget(self.emgstop_key)

        self.label_24 = QLabel(self.widget_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(16777215, 12))
        self.label_24.setFont(font5)
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_24)


        self.horizontalLayout_16.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.keys)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_37 = QVBoxLayout(self.widget_7)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.stop_key = QToolButton(self.widget_7)
        self.stop_key.setObjectName(u"stop_key")
        self.stop_key.setMinimumSize(QSize(66, 60))
        self.stop_key.setStyleSheet(u"")

        self.verticalLayout_37.addWidget(self.stop_key)

        self.label_26 = QLabel(self.widget_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(16777215, 12))
        self.label_26.setFont(font5)
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_26)


        self.horizontalLayout_16.addWidget(self.widget_7)


        self.verticalLayout_38.addLayout(self.horizontalLayout_16)

        self.stackedWidget.addWidget(self.keys)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(10, 0))
        self.frame.setStyleSheet(u"background-color: rgb(31, 68, 141);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(0)

        self.horizontalLayout.addWidget(self.frame)

        self.right_menu = QWidget(self.centralwidget)
        self.right_menu.setObjectName(u"right_menu")
        self.right_menu.setMinimumSize(QSize(80, 0))
        self.right_menu.setStyleSheet(u"QToolButton{\n"
"border:none\n"
"\n"
"}\n"
"QToolButton::hover{\n"
"	background-color: rgb(183, 183, 183);\n"
"\n"
"}")
        self.verticalLayout_27 = QVBoxLayout(self.right_menu)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.toolButton_shaft = QToolButton(self.right_menu)
        self.toolButton_shaft.setObjectName(u"toolButton_shaft")
        self.toolButton_shaft.setMinimumSize(QSize(75, 60))
        self.toolButton_shaft.setMaximumSize(QSize(60, 25))
        self.toolButton_shaft.setFont(font5)

        self.verticalLayout_2.addWidget(self.toolButton_shaft)

        self.line = QFrame(self.right_menu)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 2))
        self.line.setStyleSheet(u"background-color: rgb(125, 125, 125);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)


        self.verticalLayout_27.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolButton_temperature = QToolButton(self.right_menu)
        self.toolButton_temperature.setObjectName(u"toolButton_temperature")
        self.toolButton_temperature.setMinimumSize(QSize(75, 60))
        self.toolButton_temperature.setMaximumSize(QSize(60, 25))
        self.toolButton_temperature.setFont(font5)

        self.verticalLayout_3.addWidget(self.toolButton_temperature)

        self.line_2 = QFrame(self.right_menu)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMaximumSize(QSize(16777215, 2))
        self.line_2.setStyleSheet(u"background-color: rgb(125, 125, 125);")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)


        self.verticalLayout_27.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.toolButton_pressure = QToolButton(self.right_menu)
        self.toolButton_pressure.setObjectName(u"toolButton_pressure")
        self.toolButton_pressure.setMinimumSize(QSize(75, 60))
        self.toolButton_pressure.setMaximumSize(QSize(60, 25))
        self.toolButton_pressure.setFont(font5)

        self.verticalLayout_4.addWidget(self.toolButton_pressure)

        self.line_3 = QFrame(self.right_menu)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMaximumSize(QSize(16777215, 2))
        self.line_3.setStyleSheet(u"background-color: rgb(125, 125, 125);")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)


        self.verticalLayout_27.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.toolButton_keys = QToolButton(self.right_menu)
        self.toolButton_keys.setObjectName(u"toolButton_keys")
        self.toolButton_keys.setMinimumSize(QSize(75, 60))
        self.toolButton_keys.setMaximumSize(QSize(60, 25))
        self.toolButton_keys.setFont(font5)

        self.verticalLayout_5.addWidget(self.toolButton_keys)

        self.line_4 = QFrame(self.right_menu)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMaximumSize(QSize(16777215, 2))
        self.line_4.setStyleSheet(u"background-color: rgb(125, 125, 125);")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_4)


        self.verticalLayout_27.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.toolButton = QToolButton(self.right_menu)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(75, 60))
        self.toolButton.setFont(font5)

        self.verticalLayout_6.addWidget(self.toolButton)

        self.line_5 = QFrame(self.right_menu)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMaximumSize(QSize(16777215, 2))
        self.line_5.setStyleSheet(u"background-color: rgb(125, 125, 125);")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_5)


        self.verticalLayout_27.addLayout(self.verticalLayout_6)


        self.horizontalLayout.addWidget(self.right_menu)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_sensosr.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u062f\u0631\u0641\u0634", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_engine_name.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u06f1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0645\u0648\u062a\u0648\u0631:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0627\u0645\u0648\u0634", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u" \u0648\u0636\u0639\u06cc\u062a \u0645\u0648\u062a\u0648\u0631 :", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0645\u0627\u06cc \u0631\u0648\u063a\u0646", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"RPM", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0634\u0627\u0631\u0631\u0648\u063a\u0646", None))
        self.label_shaft_airflap.setText(QCoreApplication.translate("MainWindow", u"Air flap", None))
        self.label_shaft_stop.setText(QCoreApplication.translate("MainWindow", u"Stoped", None))
        self.label_shaft_start.setText(QCoreApplication.translate("MainWindow", u"Started", None))
        self.label_shaft_water_level.setText(QCoreApplication.translate("MainWindow", u"Water Level", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0646\u0633\u0648\u0631 \u0647\u0627", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0645\u0627", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Exhuast Bank B", None))
        self.exhuast_bank_b_gauge.setText(QCoreApplication.translate("MainWindow", u"Exhuast Bank A", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Air Boost Bank A", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0645\u0627", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Air Boost Bank B", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Oil", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Oil NTC", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0645\u0627", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Fresh Water after Thermostat", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Fresh Water before Thermostat", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Sea Water", None))
        self.toolButton_previouspage_sensors.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_nextpage_sensors.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0646\u0633\u0648\u0631 \u0641\u0634\u0627\u0631", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Oil", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Oil Switch", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Air Boost", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Sea Water", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Fuel Pressure", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0644\u06cc\u062f \u0647\u0627", None))
        self.lamp_increase.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.lamp_decrease.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.lamp_start.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.lamp_emgstop.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"EMG Stop", None))
        self.lamp_stop.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.increase_key.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"increase", None))
        self.decrease_key.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.start_key.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.emgstop_key.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"EMG Stop", None))
        self.stop_key.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.toolButton_shaft.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0641\u062a", None))
        self.toolButton_temperature.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0645\u0627", None))
        self.toolButton_pressure.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0634\u0627\u0631", None))
        self.toolButton_keys.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0644\u06cc\u062f\u0647\u0627", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0627\u06cc\u0631", None))
    # retranslateUi

