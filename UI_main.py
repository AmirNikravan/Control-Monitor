# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QMainWindow, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)

from AnalogGaugeWidget import AnalogGaugeWidget
import src_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(893, 549)
        MainWindow.setMinimumSize(QSize(255, 212))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"IRANSansXFaNum"])
        font.setPointSize(10)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"background-color: #405D72")
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
        self.up_label.setStyleSheet(u"background-color: #405D72")
        self.horizontalLayout_8 = QHBoxLayout(self.up_label)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, -1)
        self.label_time = QLabel(self.up_label)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setMinimumSize(QSize(102, 0))
        font1 = QFont()
        font1.setFamilies([u"IRANSansXFaNum"])
        font1.setBold(True)
        self.label_time.setFont(font1)
        self.label_time.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_time.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_time)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.label_engine_name = QLabel(self.up_label)
        self.label_engine_name.setObjectName(u"label_engine_name")
        font2 = QFont()
        font2.setFamilies([u"IRANSansXFaNum"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_engine_name.setFont(font2)
        self.label_engine_name.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.label_engine_name)

        self.label_3 = QLabel(self.up_label)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.up_label)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setFamilies([u"IRANSansXFaNum"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.label_2)

        self.label = QLabel(self.up_label)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.label)


        self.verticalLayout.addWidget(self.up_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: #758694")
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
        self.oil_temp_shaft_gauge.setMinimumSize(QSize(0, 192))

        self.verticalLayout_28.addWidget(self.oil_temp_shaft_gauge)

        self.label_27 = QLabel(self.shaft)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(16777215, 22))
        font4 = QFont()
        font4.setFamilies([u"IRANSansXFaNum Black"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.label_27.setFont(font4)
        self.label_27.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_27, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_3.addLayout(self.verticalLayout_28)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.rpm_gauge_shaft = AnalogGaugeWidget(self.shaft)
        self.rpm_gauge_shaft.setObjectName(u"rpm_gauge_shaft")
        self.rpm_gauge_shaft.setMinimumSize(QSize(0, 192))

        self.verticalLayout_29.addWidget(self.rpm_gauge_shaft)

        self.label_25 = QLabel(self.shaft)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 22))
        self.label_25.setFont(font4)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_25, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_3.addLayout(self.verticalLayout_29)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.oil_press_shaft_gauge = AnalogGaugeWidget(self.shaft)
        self.oil_press_shaft_gauge.setObjectName(u"oil_press_shaft_gauge")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oil_press_shaft_gauge.sizePolicy().hasHeightForWidth())
        self.oil_press_shaft_gauge.setSizePolicy(sizePolicy)
        self.oil_press_shaft_gauge.setMinimumSize(QSize(1, 192))

        self.verticalLayout_30.addWidget(self.oil_press_shaft_gauge)

        self.label_4 = QLabel(self.shaft)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 22))
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_3.addLayout(self.verticalLayout_30)


        self.verticalLayout_41.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_7 = QSpacerItem(23, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_41.addItem(self.verticalSpacer_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(23)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_shaft_airflap = QLabel(self.shaft)
        self.label_shaft_airflap.setObjectName(u"label_shaft_airflap")
        self.label_shaft_airflap.setMinimumSize(QSize(107, 0))
        self.label_shaft_airflap.setFont(font1)
        self.label_shaft_airflap.setStyleSheet(u"            QLabel {\n"
"\n"
"	\n"
"	background-color: rgb(143, 143, 143);\n"
"                color: black;\n"
"                padding: 20px;\n"
"                border-radius: 45px;\n"
"                border: 2px solid rgba(255, 255, 255, 100);\n"
"            }")
        self.label_shaft_airflap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_shaft_airflap, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_shaft_stop = QLabel(self.shaft)
        self.label_shaft_stop.setObjectName(u"label_shaft_stop")
        self.label_shaft_stop.setMinimumSize(QSize(107, 0))
        self.label_shaft_stop.setFont(font1)
        self.label_shaft_stop.setStyleSheet(u"            QLabel {\n"
"\n"
"	\n"
"	background-color: rgb(143, 143, 143);\n"
"                color: black;\n"
"                padding: 20px;\n"
"                border-radius: 45px;\n"
"                border: 2px solid rgba(255, 255, 255, 100);\n"
"            }")
        self.label_shaft_stop.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_shaft_stop, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_shaft_start = QLabel(self.shaft)
        self.label_shaft_start.setObjectName(u"label_shaft_start")
        self.label_shaft_start.setMinimumSize(QSize(107, 0))
        self.label_shaft_start.setFont(font1)
        self.label_shaft_start.setStyleSheet(u"            QLabel {\n"
"\n"
"	\n"
"	background-color: rgb(143, 143, 143);\n"
"                color: black;\n"
"                padding: 20px;\n"
"                border-radius: 45px;\n"
"                border: 2px solid rgba(255, 255, 255, 100);\n"
"            }")
        self.label_shaft_start.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_shaft_start, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_shaft_water_level = QLabel(self.shaft)
        self.label_shaft_water_level.setObjectName(u"label_shaft_water_level")
        self.label_shaft_water_level.setFont(font1)
        self.label_shaft_water_level.setStyleSheet(u"            QLabel {\n"
"\n"
"	\n"
"	background-color: rgb(143, 143, 143);\n"
"                color: black;\n"
"                padding: 20px;\n"
"                border-radius: 45px;\n"
"                border: 2px solid rgba(255, 255, 255, 100);\n"
"            }")
        self.label_shaft_water_level.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_shaft_water_level, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

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
        font5 = QFont()
        font5.setFamilies([u"IRANSansXFaNum"])
        font5.setPointSize(14)
        font5.setBold(True)
        self.label_5.setFont(font5)

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
        self.label_31 = QLabel(self.page)
        self.label_31.setObjectName(u"label_31")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy1)
        self.label_31.setMaximumSize(QSize(16777215, 27))
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 10pt \"IRANSansXFaNum\";")

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
        self.exhuast_bank_a_temp_gauge.setMouseTracking(True)

        self.verticalLayout_7.addWidget(self.exhuast_bank_a_temp_gauge)

        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 19))
        self.label_6.setFont(font)
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
        self.exhuast_bank_b_gauge.setFont(font)
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
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_11)


        self.horizontalLayout_9.addLayout(self.verticalLayout_12)


        self.verticalLayout_31.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_3 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_31.addItem(self.verticalSpacer_3)

        self.stackedWidget_sensosr.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_40 = QVBoxLayout(self.page_3)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_30 = QLabel(self.page_3)
        self.label_30.setObjectName(u"label_30")
        sizePolicy1.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy1)
        self.label_30.setMaximumSize(QSize(16777215, 27))
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 10pt \"IRANSansXFaNum\";")

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
        self.label_12.setFont(font)
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
        self.label_10.setFont(font)
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
        self.label_15.setFont(font)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_15)


        self.horizontalLayout_10.addLayout(self.verticalLayout_16)


        self.verticalLayout_40.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_2 = QSpacerItem(20, 153, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_40.addItem(self.verticalSpacer_2)

        self.stackedWidget_sensosr.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_20 = QVBoxLayout(self.page_2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_28 = QLabel(self.page_2)
        self.label_28.setObjectName(u"label_28")
        sizePolicy1.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy1)
        self.label_28.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 10pt \"IRANSansXFaNum\";")

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
        self.label_16.setFont(font)
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
        self.label_17.setFont(font)
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
        self.label_18.setFont(font)
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_18)


        self.horizontalLayout_11.addLayout(self.verticalLayout_19)


        self.verticalLayout_20.addLayout(self.horizontalLayout_11)

        self.verticalSpacer = QSpacerItem(10, 153, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_20.addItem(self.verticalSpacer)

        self.stackedWidget_sensosr.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_26 = QVBoxLayout(self.page_4)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_29 = QLabel(self.page_4)
        self.label_29.setObjectName(u"label_29")
        sizePolicy1.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy1)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 10pt \"IRANSansXFaNum\";")

        self.horizontalLayout_14.addWidget(self.label_29)


        self.verticalLayout_26.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.oil_pressure_gauge = AnalogGaugeWidget(self.page_4)
        self.oil_pressure_gauge.setObjectName(u"oil_pressure_gauge")
        self.oil_pressure_gauge.setMinimumSize(QSize(255, 212))
        self.oil_pressure_gauge.setMaximumSize(QSize(255, 212))

        self.verticalLayout_21.addWidget(self.oil_pressure_gauge)

        self.label_19 = QLabel(self.page_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 19))
        self.label_19.setFont(font)
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_19)


        self.horizontalLayout_12.addLayout(self.verticalLayout_21)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.oil_switch_pressure_gauge = AnalogGaugeWidget(self.page_4)
        self.oil_switch_pressure_gauge.setObjectName(u"oil_switch_pressure_gauge")
        self.oil_switch_pressure_gauge.setMinimumSize(QSize(255, 212))
        self.oil_switch_pressure_gauge.setMaximumSize(QSize(255, 212))

        self.verticalLayout_22.addWidget(self.oil_switch_pressure_gauge)

        self.label_20 = QLabel(self.page_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 19))
        self.label_20.setFont(font)
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_20)


        self.horizontalLayout_12.addLayout(self.verticalLayout_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.airboost_pressure_gauge = AnalogGaugeWidget(self.page_4)
        self.airboost_pressure_gauge.setObjectName(u"airboost_pressure_gauge")
        self.airboost_pressure_gauge.setMinimumSize(QSize(255, 212))
        self.airboost_pressure_gauge.setMaximumSize(QSize(255, 212))

        self.verticalLayout_23.addWidget(self.airboost_pressure_gauge)

        self.label_21 = QLabel(self.page_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 19))
        self.label_21.setFont(font)
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_21)


        self.horizontalLayout_12.addLayout(self.verticalLayout_23)


        self.verticalLayout_26.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_4 = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_26.addItem(self.verticalSpacer_4)

        self.stackedWidget_sensosr.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_42 = QVBoxLayout(self.page_5)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_33 = QLabel(self.page_5)
        self.label_33.setObjectName(u"label_33")
        sizePolicy1.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy1)
        self.label_33.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 10pt \"IRANSansXFaNum\";")

        self.horizontalLayout_17.addWidget(self.label_33)


        self.verticalLayout_42.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.sea_water_pressure_gauge = AnalogGaugeWidget(self.page_5)
        self.sea_water_pressure_gauge.setObjectName(u"sea_water_pressure_gauge")
        self.sea_water_pressure_gauge.setMinimumSize(QSize(255, 212))
        self.sea_water_pressure_gauge.setMaximumSize(QSize(255, 212))

        self.verticalLayout_25.addWidget(self.sea_water_pressure_gauge)

        self.label_23 = QLabel(self.page_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(16777215, 19))
        self.label_23.setFont(font)
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_23)


        self.horizontalLayout_13.addLayout(self.verticalLayout_25)

        self.horizontalSpacer_4 = QSpacerItem(82, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.fuel_pressure_gauge = AnalogGaugeWidget(self.page_5)
        self.fuel_pressure_gauge.setObjectName(u"fuel_pressure_gauge")
        self.fuel_pressure_gauge.setMinimumSize(QSize(255, 212))
        self.fuel_pressure_gauge.setMaximumSize(QSize(255, 212))

        self.verticalLayout_24.addWidget(self.fuel_pressure_gauge)

        self.label_22 = QLabel(self.page_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 19))
        self.label_22.setFont(font)
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_22)


        self.horizontalLayout_13.addLayout(self.verticalLayout_24)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)


        self.verticalLayout_42.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_5 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_42.addItem(self.verticalSpacer_5)

        self.stackedWidget_sensosr.addWidget(self.page_5)

        self.verticalLayout_39.addWidget(self.stackedWidget_sensosr)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.toolButton_previouspage_sensors = QToolButton(self.temperature)
        self.toolButton_previouspage_sensors.setObjectName(u"toolButton_previouspage_sensors")
        self.toolButton_previouspage_sensors.setMinimumSize(QSize(93, 64))
        self.toolButton_previouspage_sensors.setFont(font)
        self.toolButton_previouspage_sensors.setStyleSheet(u"QToolButton{\n"
"background-color: rgb(193, 233, 255);\n"
"border-radius : 15;\n"
"color: rgb(13, 13, 13);\n"
"}\n"
"QToolButton::hover{\n"
"	background-color: rgb(215, 255, 218);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/icons8-back-arrow-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_previouspage_sensors.setIcon(icon)
        self.toolButton_previouspage_sensors.setIconSize(QSize(47, 39))
        self.toolButton_previouspage_sensors.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_4.addWidget(self.toolButton_previouspage_sensors)

        self.toolButton_nextpage_sensors = QToolButton(self.temperature)
        self.toolButton_nextpage_sensors.setObjectName(u"toolButton_nextpage_sensors")
        self.toolButton_nextpage_sensors.setMinimumSize(QSize(93, 64))
        font6 = QFont()
        font6.setFamilies([u"IRANSansXFaNum Black"])
        font6.setPointSize(10)
        font6.setBold(True)
        self.toolButton_nextpage_sensors.setFont(font6)
        self.toolButton_nextpage_sensors.setStyleSheet(u"QToolButton{\n"
"background-color: rgb(193, 233, 255);\n"
"border-radius : 15;\n"
"color: rgb(13, 13, 13);\n"
"}\n"
"QToolButton::hover{\n"
"	background-color: rgb(215, 255, 218);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/icons8-forward-button-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_nextpage_sensors.setIcon(icon1)
        self.toolButton_nextpage_sensors.setIconSize(QSize(47, 39))
        self.toolButton_nextpage_sensors.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_4.addWidget(self.toolButton_nextpage_sensors)


        self.verticalLayout_39.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.temperature)
        self.table = QWidget()
        self.table.setObjectName(u"table")
        self.verticalLayout_43 = QVBoxLayout(self.table)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.scrollArea = QScrollArea(self.table)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 781, 488))
        self.verticalLayout_44 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_data = QTableWidget(self.scrollAreaWidgetContents)
        if (self.tableWidget_data.columnCount() < 7):
            self.tableWidget_data.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget_data.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tableWidget_data.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tableWidget_data.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tableWidget_data.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.tableWidget_data.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        font7 = QFont()
        font7.setFamilies([u"IRANSansXFaNum"])
        font7.setPointSize(10)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font7);
        self.tableWidget_data.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.tableWidget_data.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tableWidget_data.rowCount() < 14):
            self.tableWidget_data.setRowCount(14)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_data.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_data.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_data.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_data.setVerticalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_data.setVerticalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_data.setVerticalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_data.setVerticalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_data.setVerticalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_data.setVerticalHeaderItem(8, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_data.setVerticalHeaderItem(9, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_data.setVerticalHeaderItem(10, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_data.setVerticalHeaderItem(11, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_data.setVerticalHeaderItem(12, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_data.setVerticalHeaderItem(13, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_data.setItem(0, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_data.setItem(0, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_data.setItem(0, 3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(0, 4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_data.setItem(0, 5, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(0, 6, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_data.setItem(1, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_data.setItem(1, 1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(1, 4, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_data.setItem(1, 5, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(1, 6, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_data.setItem(2, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_data.setItem(2, 1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(2, 4, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_data.setItem(2, 5, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(2, 6, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_data.setItem(3, 0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_data.setItem(3, 1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(3, 4, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_data.setItem(3, 5, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(3, 6, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_data.setItem(4, 0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_data.setItem(4, 1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(4, 4, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_data.setItem(4, 5, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(4, 6, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_data.setItem(5, 0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_data.setItem(5, 1, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(5, 4, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_data.setItem(5, 5, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(5, 6, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget_data.setItem(6, 0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget_data.setItem(6, 1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(6, 4, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget_data.setItem(6, 5, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(6, 6, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget_data.setItem(7, 0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget_data.setItem(7, 1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(7, 4, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget_data.setItem(7, 5, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(7, 6, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget_data.setItem(8, 0, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableWidget_data.setItem(8, 1, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(8, 4, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableWidget_data.setItem(8, 5, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(8, 6, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tableWidget_data.setItem(9, 0, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tableWidget_data.setItem(9, 1, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tableWidget_data.setItem(9, 5, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(9, 6, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tableWidget_data.setItem(10, 0, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tableWidget_data.setItem(10, 1, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tableWidget_data.setItem(10, 5, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(10, 6, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tableWidget_data.setItem(11, 0, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tableWidget_data.setItem(11, 1, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableWidget_data.setItem(11, 5, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(11, 6, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget_data.setItem(12, 0, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget_data.setItem(12, 1, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        __qtablewidgetitem81.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(12, 6, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tableWidget_data.setItem(13, 0, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tableWidget_data.setItem(13, 1, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tableWidget_data.setItem(13, 3, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_data.setItem(13, 6, __qtablewidgetitem85)
        self.tableWidget_data.setObjectName(u"tableWidget_data")
        self.tableWidget_data.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tableWidget_data.setStyleSheet(u"    QTableWidget::item {\n"
"        background-color: #FFFFFF;\n"
"    }\n"
"    QTableWidget::item:alternate {\n"
"        background-color: #F0F0F0;\n"
"    }")
        self.tableWidget_data.setFrameShape(QFrame.Shape.Box)
        self.tableWidget_data.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_data.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_data.setAlternatingRowColors(True)
        self.tableWidget_data.setShowGrid(True)
        self.tableWidget_data.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget_data.setSortingEnabled(False)
        self.tableWidget_data.setWordWrap(True)
        self.tableWidget_data.setCornerButtonEnabled(True)
        self.tableWidget_data.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_data.horizontalHeader().setMinimumSectionSize(49)
        self.tableWidget_data.horizontalHeader().setDefaultSectionSize(192)
        self.tableWidget_data.horizontalHeader().setHighlightSections(True)
        self.tableWidget_data.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget_data.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_data.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_data.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_44.addWidget(self.tableWidget_data)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_43.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.table)
        self.keys = QWidget()
        self.keys.setObjectName(u"keys")
        self.verticalLayout_38 = QVBoxLayout(self.keys)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_7 = QLabel(self.keys)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_38.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.lamp_increase = QLabel(self.keys)
        self.lamp_increase.setObjectName(u"lamp_increase")
        self.lamp_increase.setMinimumSize(QSize(94, 99))
        self.lamp_increase.setStyleSheet(u"    QLabel {\n"
"\n"
"\n"
"	background-color: rgb(195, 195, 195);\n"
"                border-style: outset;\n"
"                border-width: 1px;\n"
"                border-radius: 45px;\n"
"        }")

        self.verticalLayout_32.addWidget(self.lamp_increase, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_32 = QLabel(self.keys)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(83, 13))
        self.label_32.setFont(font6)
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_32, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_15.addLayout(self.verticalLayout_32)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.lamp_decrease = QLabel(self.keys)
        self.lamp_decrease.setObjectName(u"lamp_decrease")
        self.lamp_decrease.setMinimumSize(QSize(94, 99))
        self.lamp_decrease.setStyleSheet(u"    QLabel {\n"
"\n"
"\n"
"	background-color: rgb(195, 195, 195);\n"
"                border-style: outset;\n"
"                border-width: 1px;\n"
"                border-radius: 45px;\n"
"        }")

        self.verticalLayout_33.addWidget(self.lamp_decrease, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_34 = QLabel(self.keys)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(83, 13))
        self.label_34.setFont(font6)
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_34, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_15.addLayout(self.verticalLayout_33)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.lamp_start = QLabel(self.keys)
        self.lamp_start.setObjectName(u"lamp_start")
        self.lamp_start.setMinimumSize(QSize(94, 99))
        self.lamp_start.setMaximumSize(QSize(16777215, 16777215))
        self.lamp_start.setStyleSheet(u"    QLabel {\n"
"\n"
"\n"
"	background-color: rgb(195, 195, 195);\n"
"                border-style: outset;\n"
"                border-width: 1px;\n"
"                border-radius: 45px;\n"
"        }")

        self.verticalLayout_34.addWidget(self.lamp_start, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_35 = QLabel(self.keys)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(83, 13))
        self.label_35.setFont(font6)
        self.label_35.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_35, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_15.addLayout(self.verticalLayout_34)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.lamp_stop = QLabel(self.keys)
        self.lamp_stop.setObjectName(u"lamp_stop")
        self.lamp_stop.setMinimumSize(QSize(94, 99))
        self.lamp_stop.setStyleSheet(u"    QLabel {\n"
"\n"
"\n"
"	background-color: rgb(195, 195, 195);\n"
"                border-style: outset;\n"
"                border-width: 1px;\n"
"                border-radius: 45px;\n"
"        }")

        self.verticalLayout_36.addWidget(self.lamp_stop, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_37 = QLabel(self.keys)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(83, 13))
        self.label_37.setFont(font6)
        self.label_37.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_37, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_15.addLayout(self.verticalLayout_36)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.lamp_emgstop = QLabel(self.keys)
        self.lamp_emgstop.setObjectName(u"lamp_emgstop")
        self.lamp_emgstop.setMinimumSize(QSize(94, 99))
        self.lamp_emgstop.setStyleSheet(u"    QLabel {\n"
"\n"
"\n"
"	background-color: rgb(195, 195, 195);\n"
"                border-style: outset;\n"
"                border-width: 1px;\n"
"                border-radius: 45px;\n"
"        }")

        self.verticalLayout_35.addWidget(self.lamp_emgstop, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_36 = QLabel(self.keys)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(83, 13))
        self.label_36.setFont(font6)
        self.label_36.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_35.addWidget(self.label_36, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_15.addLayout(self.verticalLayout_35)


        self.verticalLayout_38.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_6 = QSpacerItem(35, 182, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_38.addItem(self.verticalSpacer_6)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.widget_3 = QWidget(self.keys)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_8 = QVBoxLayout(self.widget_3)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, -1)
        self.increase_key = QToolButton(self.widget_3)
        self.increase_key.setObjectName(u"increase_key")
        self.increase_key.setMinimumSize(QSize(95, 70))
        self.increase_key.setMaximumSize(QSize(95, 70))
        self.increase_key.setStyleSheet(u"QToolButton{\n"
"border:none;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/icons8-add-64.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.increase_key.setIcon(icon2)
        self.increase_key.setIconSize(QSize(50, 73))

        self.verticalLayout_8.addWidget(self.increase_key, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 12))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_8)


        self.horizontalLayout_16.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.widget_4 = QWidget(self.keys)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_9 = QVBoxLayout(self.widget_4)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 9)
        self.decrease_key = QToolButton(self.widget_4)
        self.decrease_key.setObjectName(u"decrease_key")
        self.decrease_key.setMinimumSize(QSize(95, 70))
        self.decrease_key.setMaximumSize(QSize(95, 70))
        self.decrease_key.setStyleSheet(u"QToolButton{\n"
"border:none;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/icons8-remove-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.decrease_key.setIcon(icon3)
        self.decrease_key.setIconSize(QSize(53, 70))

        self.verticalLayout_9.addWidget(self.decrease_key, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 12))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_9)


        self.horizontalLayout_16.addWidget(self.widget_4, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.widget_5 = QWidget(self.keys)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_10 = QVBoxLayout(self.widget_5)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.start_key = QToolButton(self.widget_5)
        self.start_key.setObjectName(u"start_key")
        self.start_key.setMinimumSize(QSize(95, 70))
        self.start_key.setMaximumSize(QSize(95, 70))
        self.start_key.setStyleSheet(u"QToolButton{\n"
"border:none;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/icons8-start-button-64.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start_key.setIcon(icon4)
        self.start_key.setIconSize(QSize(92, 67))

        self.verticalLayout_10.addWidget(self.start_key, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_14 = QLabel(self.widget_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 12))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_14)


        self.horizontalLayout_16.addWidget(self.widget_5, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.widget_7 = QWidget(self.keys)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_37 = QVBoxLayout(self.widget_7)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, -1, 0, 0)
        self.stop_key = QToolButton(self.widget_7)
        self.stop_key.setObjectName(u"stop_key")
        self.stop_key.setMinimumSize(QSize(95, 70))
        self.stop_key.setMaximumSize(QSize(95, 70))
        self.stop_key.setStyleSheet(u"QToolButton{\n"
"border:none;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/icons8-stop-button-67.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stop_key.setIcon(icon5)
        self.stop_key.setIconSize(QSize(45, 61))

        self.verticalLayout_37.addWidget(self.stop_key, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_26 = QLabel(self.widget_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 25))
        self.label_26.setMaximumSize(QSize(16777215, 12))
        self.label_26.setFont(font)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_26, 0, Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_16.addWidget(self.widget_7, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.widget_6 = QWidget(self.keys)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_15 = QVBoxLayout(self.widget_6)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.emgstop_key = QToolButton(self.widget_6)
        self.emgstop_key.setObjectName(u"emgstop_key")
        self.emgstop_key.setMinimumSize(QSize(95, 70))
        self.emgstop_key.setMaximumSize(QSize(95, 70))
        self.emgstop_key.setStyleSheet(u"QToolButton{\n"
"border:none;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/icons8-stop-sign-60.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.emgstop_key.setIcon(icon6)
        self.emgstop_key.setIconSize(QSize(66, 80))

        self.verticalLayout_15.addWidget(self.emgstop_key, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_24 = QLabel(self.widget_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(16777215, 12))
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_24)


        self.horizontalLayout_16.addWidget(self.widget_6, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_38.addLayout(self.horizontalLayout_16)

        self.stackedWidget.addWidget(self.keys)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(10, 0))
        self.frame.setStyleSheet(u"background-color: #F7E7DC")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(0)

        self.horizontalLayout.addWidget(self.frame)

        self.right_menu = QWidget(self.centralwidget)
        self.right_menu.setObjectName(u"right_menu")
        self.right_menu.setMinimumSize(QSize(80, 0))
        self.right_menu.setStyleSheet(u"QToolButton{\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
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
        self.toolButton_shaft.setFont(font)

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
        self.toolButton_temperature.setFont(font)

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
        self.toolButton_table = QToolButton(self.right_menu)
        self.toolButton_table.setObjectName(u"toolButton_table")
        self.toolButton_table.setMinimumSize(QSize(75, 60))
        self.toolButton_table.setMaximumSize(QSize(60, 25))
        self.toolButton_table.setFont(font)

        self.verticalLayout_4.addWidget(self.toolButton_table)

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
        self.toolButton_keys.setFont(font)

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
        self.toolButton.setFont(font)

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

        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_sensosr.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u062f\u0631\u0641\u0634", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_engine_name.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0645\u0648\u062a\u0648\u0631:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0627\u0645\u0648\u0634", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u" \u0648\u0636\u0639\u06cc\u062a \u0645\u0648\u062a\u0648\u0631 :", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0645\u0627\u06cc \u0631\u0648\u063a\u0646", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"RPM", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0634\u0627\u0631 \u0631\u0648\u063a\u0646", None))
        self.label_shaft_airflap.setText(QCoreApplication.translate("MainWindow", u"Air flap", None))
        self.label_shaft_stop.setText(QCoreApplication.translate("MainWindow", u"Stoped", None))
        self.label_shaft_start.setText(QCoreApplication.translate("MainWindow", u"Started", None))
        self.label_shaft_water_level.setText(QCoreApplication.translate("MainWindow", u"Water Level", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0646\u0633\u0648\u0631 \u0647\u0627", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0645\u0627", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Exhuast Bank A", None))
        self.exhuast_bank_b_gauge.setText(QCoreApplication.translate("MainWindow", u"Exhuast Bank B", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Air Boost Bank A", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0645\u0627", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Air Boost Bank B", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Oil", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Oil NTC", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0645\u0627", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Fresh Water after Thermostat", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Fresh Water before Thermostat", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Sea Water", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0634\u0627\u0631", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Oil", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Oil Switch", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Air Boost", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0634\u0627\u0631", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Sea Water Pressure", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Fuel Pressure", None))
        self.toolButton_previouspage_sensors.setText(QCoreApplication.translate("MainWindow", u"\u0635\u0641\u062d\u0647 \u0642\u0628\u0644", None))
        self.toolButton_nextpage_sensors.setText(QCoreApplication.translate("MainWindow", u"\u0635\u0641\u062d\u0647 \u0628\u0639\u062f", None))
        ___qtablewidgetitem = self.tableWidget_data.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0631\u062f\u06cc\u0641", None));
        ___qtablewidgetitem1 = self.tableWidget_data.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0633\u0646\u0633\u0648\u0631", None));
        ___qtablewidgetitem2 = self.tableWidget_data.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0631\u06cc\u0627\u0646", None));
        ___qtablewidgetitem3 = self.tableWidget_data.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0642\u062f\u0627\u0631", None));
        ___qtablewidgetitem4 = self.tableWidget_data.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a", None));
        ___qtablewidgetitem5 = self.tableWidget_data.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0632\u0647", None));
        ___qtablewidgetitem6 = self.tableWidget_data.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u06cc\u06a9\u0627", None));

        __sortingEnabled = self.tableWidget_data.isSortingEnabled()
        self.tableWidget_data.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tableWidget_data.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem8 = self.tableWidget_data.item(0, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Air Boost Bank A Temperature", None));
        ___qtablewidgetitem9 = self.tableWidget_data.item(0, 5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"-14 - 74", None));
        ___qtablewidgetitem10 = self.tableWidget_data.item(0, 6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"centigrade", None));
        ___qtablewidgetitem11 = self.tableWidget_data.item(1, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem12 = self.tableWidget_data.item(1, 1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Air Boost Bank B Temperature", None));
        ___qtablewidgetitem13 = self.tableWidget_data.item(1, 5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"-14 - 74", None));
        ___qtablewidgetitem14 = self.tableWidget_data.item(1, 6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"centigrade", None));
        ___qtablewidgetitem15 = self.tableWidget_data.item(2, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem16 = self.tableWidget_data.item(2, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Fresh Water before Thermostat Temperature", None));
        ___qtablewidgetitem17 = self.tableWidget_data.item(2, 5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"1 - 87", None));
        ___qtablewidgetitem18 = self.tableWidget_data.item(2, 6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"centigrade", None));
        ___qtablewidgetitem19 = self.tableWidget_data.item(3, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem20 = self.tableWidget_data.item(3, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Fresh Water after Thermostat Temperature ", None));
        ___qtablewidgetitem21 = self.tableWidget_data.item(3, 5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"1 - 87", None));
        ___qtablewidgetitem22 = self.tableWidget_data.item(3, 6)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"centigrade", None));
        ___qtablewidgetitem23 = self.tableWidget_data.item(4, 0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem24 = self.tableWidget_data.item(4, 1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Exhuast Bank A Temperature", None));
        ___qtablewidgetitem25 = self.tableWidget_data.item(4, 5)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"-14 - 745", None));
        ___qtablewidgetitem26 = self.tableWidget_data.item(4, 6)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"centigrade", None));
        ___qtablewidgetitem27 = self.tableWidget_data.item(5, 0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem28 = self.tableWidget_data.item(5, 1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Exhuast Bank B Temperature", None));
        ___qtablewidgetitem29 = self.tableWidget_data.item(5, 5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"-14 - 745", None));
        ___qtablewidgetitem30 = self.tableWidget_data.item(5, 6)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"centigrade", None));
        ___qtablewidgetitem31 = self.tableWidget_data.item(6, 0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem32 = self.tableWidget_data.item(6, 1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Sea Water Temperature", None));
        ___qtablewidgetitem33 = self.tableWidget_data.item(6, 5)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"1- 43", None));
        ___qtablewidgetitem34 = self.tableWidget_data.item(6, 6)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"centigrade", None));
        ___qtablewidgetitem35 = self.tableWidget_data.item(7, 0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem36 = self.tableWidget_data.item(7, 1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Oil Temperature", None));
        ___qtablewidgetitem37 = self.tableWidget_data.item(7, 5)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"6 - 103", None));
        ___qtablewidgetitem38 = self.tableWidget_data.item(7, 6)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"centigrade", None));
        ___qtablewidgetitem39 = self.tableWidget_data.item(8, 0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem40 = self.tableWidget_data.item(8, 1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Oil NTC Temperature", None));
        ___qtablewidgetitem41 = self.tableWidget_data.item(8, 5)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"6 - 103", None));
        ___qtablewidgetitem42 = self.tableWidget_data.item(8, 6)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"centigrade", None));
        ___qtablewidgetitem43 = self.tableWidget_data.item(9, 0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem44 = self.tableWidget_data.item(9, 1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Air Boost Pressure", None));
        ___qtablewidgetitem45 = self.tableWidget_data.item(9, 5)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"0 - 3.8", None));
        ___qtablewidgetitem46 = self.tableWidget_data.item(9, 6)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"bar", None));
        ___qtablewidgetitem47 = self.tableWidget_data.item(10, 0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem48 = self.tableWidget_data.item(10, 1)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Sea Water Pressure", None));
        ___qtablewidgetitem49 = self.tableWidget_data.item(10, 5)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"0.22 -3.8", None));
        ___qtablewidgetitem50 = self.tableWidget_data.item(10, 6)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"bar", None));
        ___qtablewidgetitem51 = self.tableWidget_data.item(11, 0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem52 = self.tableWidget_data.item(11, 1)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Fuel Pressure", None));
        ___qtablewidgetitem53 = self.tableWidget_data.item(11, 5)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"0.55 - 3.8", None));
        ___qtablewidgetitem54 = self.tableWidget_data.item(11, 6)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"bar", None));
        ___qtablewidgetitem55 = self.tableWidget_data.item(12, 0)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem56 = self.tableWidget_data.item(12, 1)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Oil Switch Pressure", None));
        ___qtablewidgetitem57 = self.tableWidget_data.item(12, 6)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"bar", None));
        ___qtablewidgetitem58 = self.tableWidget_data.item(13, 0)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qtablewidgetitem59 = self.tableWidget_data.item(13, 1)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Oil Pressure", None));
        ___qtablewidgetitem60 = self.tableWidget_data.item(13, 6)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"bar", None));
        self.tableWidget_data.setSortingEnabled(__sortingEnabled)

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0644\u06cc\u062f \u0647\u0627", None))
        self.lamp_increase.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.lamp_decrease.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.lamp_start.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.lamp_stop.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.lamp_emgstop.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"EMG Stop", None))
        self.increase_key.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"increase", None))
        self.decrease_key.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.start_key.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stop_key.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.emgstop_key.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"EMG Stop", None))
        self.toolButton_shaft.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0641\u062a", None))
        self.toolButton_temperature.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0646\u0633\u0648\u0631\u0647\u0627", None))
        self.toolButton_table.setText(QCoreApplication.translate("MainWindow", u"\u062c\u062f\u0648\u0644", None))
        self.toolButton_keys.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0644\u06cc\u062f\u0647\u0627", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"\u06af\u0631\u0627\u0641", None))
    # retranslateUi

