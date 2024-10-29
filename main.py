# main.py
from UI_main import Ui_MainWindow
from PySide6.QtWidgets import *
import sys

# from arduino import ArduinoHandler
from PySide6.QtCore import QTimer
import time
from thread import *
from data import *
from processor import *
import datetime


class App(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.arduino = ArduinoHandler(
        #     "COM3",
        # )
        # self.ui.tableWidget_data.resizeColumnsToContents()
        self.ui.tableWidget_data.setColumnWidth(0, 300)
        self.ui.tableWidget_data.setColumnWidth(1, 100)
        self.ui.tableWidget_data.setColumnWidth(2, 100)
        self.ui.tableWidget_data.setColumnWidth(3, 150)
        self.ui.tableWidget_data.setColumnWidth(4, 100)
        # print(self.ui.right_menu.children())
        self.ui.increase_key.clicked.connect(lambda: self.handle_button_click("6"))
        self.ui.decrease_key.clicked.connect(lambda: self.handle_button_click("7"))
        self.ui.start_key.clicked.connect(
            lambda: self.handle_button_click("4")
        )  # start
        self.ui.stop_key.clicked.connect(lambda: self.handle_button_click("5"))
        self.ui.emgstop_key.clicked.connect(lambda: self.handle_button_click("8"))
        # change page
        self.ui.toolButton_shaft.clicked.connect(lambda: self.change_page("shaft"))
        self.ui.toolButton_temperature.clicked.connect(
            lambda: self.change_page("temperature")
        )
        self.ui.toolButton_table.clicked.connect(lambda: self.change_page("table"))
        self.ui.toolButton_keys.clicked.connect(lambda: self.change_page("keys"))
        self.ui.toolButton_nextpage_sensors.clicked.connect(
            lambda: self.change_page_sensors("next")
        )
        self.ui.toolButton_previouspage_sensors.clicked.connect(
            lambda: self.change_page_sensors("previous")
        )
        # design
        self.ui.stackedWidget.setCurrentIndex(0)
        self.design_gauges()
        # self.worker_arduino = WorkerArduino(self.ui,'COM11')
        self.worker_arduino = WorkerArduino(self.ui, "/dev/ttyACM0")
        # self.worker_arduino.data_received.connect(self.process_serial_data)
        self.worker_arduino.start()
        # self.update_worker = UpdateWorker(self.ui)
        # self.update_worker.start()
        self.check_table()
        self.timer = QTimer(self)
        self.timer.timeout.connect(
            self.update_time
        )  # Connect timeout to the update function
        self.timer.start(1000)  # 1000 ms = 1 second
        # Call update_time once at startup to set the initial time
        self.update_time()

    def check_table(self):
        print(self.ui.tableWidget_data.setColumnCount(5))
        self.ui.tableWidget_data.setRowCount(14)
        self.ui.tableWidget_data.setItem(1, 1, QTableWidgetItem(34))
        self.ui.tableWidget_data.repaint()
        # for i in range(0,10):
        #     self.ui.tableWidget_data.setItem(i,1,QTableWidgetItem(2))
        # for i in range(10,15):
        #     self.ui.tableWidget_data.setItem(i,1,QTableWidgetItem(2))

    def process_serial_data(self, value):
        # print(value)
        pass
        # self.update_worker.update_values(value)

    def update_time(self):

        # Update the label with the current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.ui.label_time.setText(current_time)

    def update_gauge(self, val):
        pass
        # self.ui.speed_gauge.value = val
        # # self.ui.airboost_bank_a_temp_gauge.neede
        # self.ui.speed_gauge.setGaugeTheme(val)
        # self.ui.speed_gauge.repaint()

    def test(self):
        while True:
            for i in range(0, 5):
                self.ui.stackedWidget_sensosr.setCurrentIndex(i)
                time.sleep(1)

    def change_page_sensors(self, page):

        min = 0
        max = 4
        current = self.ui.stackedWidget_sensosr.currentIndex()
        if page == "previous":
            if current == min:
                self.ui.stackedWidget_sensosr.setCurrentIndex(max)
            else:
                self.ui.stackedWidget_sensosr.setCurrentIndex(current - 1)
        elif page == "next":
            if current == max:
                self.ui.stackedWidget_sensosr.setCurrentIndex(min)
            else:

                self.ui.stackedWidget_sensosr.setCurrentIndex(current + 1)
        # time.sleep(0.8)
        # time.sleep(0.6)

    def change_page(self, page):

        if page == "shaft":
            self.ui.stackedWidget.setCurrentIndex(0)

        elif page == "temperature":
            self.ui.stackedWidget.setCurrentIndex(1)
        elif page == "table":
            self.ui.stackedWidget.setCurrentIndex(2)
        elif page == "keys":
            self.worker_arduino.send_command("3")
            self.ui.stackedWidget.setCurrentIndex(3)

    def handle_button_click(self, command):
        # Send commands to Arduino
        self.worker_arduino.send_command(command)

    def update_data_label(self, data):
        # print(f"Raw data received: '{data}'")
        data = data.strip()
        try:
            numeric_value = float(data)
            # print(numeric_value)
            if isinstance(numeric_value, float):
                self.ui.speed_gauge.value = int(numeric_value)
                # self.ui.widget.repaint()
                # time.sleep(511)
                print(f"Numeric value: {numeric_value}")
                # self.ui.listWidget.addItem(f"Numeric value: {numeric_value}")

                print(self.ui.widget.value)
            else:
                # self.ui.listWidget.addItem(f"Data is not recognized as a float: {data}")
                print(f"Data is not recognized as a float: {data}")
        except ValueError:
            # self.ui.listWidget.addItem(f"Ignoring non-numeric data: {data}")
            print(f"Ignoring non-numeric data: {data}")

    def change_color():
        pass

    def design_gauges(self):

        self.ui.airboost_bank_a_temp_gauge.setNeedleColor(245, 66, 93)
        self.ui.exhuast_bank_a_temp_gauge.setNeedleColor(245, 66, 93)
        self.ui.exhuast_bank_b_temp_gauge.setNeedleColor(245, 66, 93)
        self.ui.airboost_bank_b_temp_gauge.setNeedleColor(245, 66, 93)
        self.ui.oil_ntc_temp_gauge.setNeedleColor(245, 66, 93)
        self.ui.oil_temp_gauge.setNeedleColor(245, 66, 93)
        self.ui.freshwater_beforethermo_temp_gauge.setNeedleColor(245, 66, 93)
        self.ui.freshwater_afterthermo_temp_gauge.setNeedleColor(245, 66, 93)
        self.ui.sea_water_temp_gauge.setNeedleColor(245, 66, 93)
        self.ui.airboost_bank_a_temp_gauge.setGaugeTheme(4)
        self.ui.airboost_bank_b_temp_gauge.setGaugeTheme(4)
        self.ui.exhuast_bank_a_temp_gauge.setGaugeTheme(3)
        self.ui.exhuast_bank_b_temp_gauge.setGaugeTheme(3)
        self.ui.oil_ntc_temp_gauge.setGaugeTheme(3)
        self.ui.oil_temp_gauge.setGaugeTheme(3)
        self.ui.freshwater_afterthermo_temp_gauge.setGaugeTheme(3)
        self.ui.freshwater_beforethermo_temp_gauge.setGaugeTheme(3)
        self.ui.sea_water_temp_gauge.setGaugeTheme(3)
        self.ui.oil_pressure_gauge.setGaugeTheme(3)
        self.ui.fuel_pressure_gauge.setGaugeTheme(3)
        self.ui.airboost_pressure_gauge.setGaugeTheme(3)
        self.ui.sea_water_pressure_gauge.setGaugeTheme(3)
        self.ui.oil_switch_pressure_gauge.setGaugeTheme(3)
        self.ui.oil_temp_shaft_gauge.setGaugeTheme(3)
        self.ui.oil_press_shaft_gauge.setGaugeTheme(3)
        self.ui.rpm_gauge_shaft.setGaugeTheme(3)
        # self.ui.speed_gauge.setGaugeTheme(6)
        # self.ui.speed_gauge.setMinValue(0)
        # self.ui.speed_gauge.setMaxValue(255)
        # self.ui.speed_gauge.setMouseTracking(False)
        # self.ui.speed_gauge.units = "RPM"
        # self.ui.rpm_gauge.setGaugeTheme(6)
        # self.ui.rpm_gauge.setMouseTracking(False)
        # self.ui.rpm_gauge.units = "RPM"
        self.ui.oil_temp_shaft_gauge.setMouseTracking(False)
        self.ui.oil_press_shaft_gauge.setMouseTracking(False)
        self.ui.rpm_gauge_shaft.setMouseTracking(False)
        self.ui.airboost_bank_a_temp_gauge.setMouseTracking(False)
        self.ui.exhuast_bank_b_temp_gauge.setMouseTracking(False)
        self.ui.exhuast_bank_a_temp_gauge.setMouseTracking(False)
        self.ui.oil_ntc_temp_gauge.setMouseTracking(False)
        self.ui.oil_temp_gauge.setMouseTracking(False)
        self.ui.airboost_bank_b_temp_gauge.setMouseTracking(False)
        self.ui.sea_water_temp_gauge.setMouseTracking(False)
        self.ui.freshwater_beforethermo_temp_gauge.setMouseTracking(False)
        self.ui.freshwater_afterthermo_temp_gauge.setMouseTracking(False)
        self.ui.airboost_bank_a_temp_gauge.setMaxValue(80)
        self.ui.airboost_bank_b_temp_gauge.setMaxValue(80)
        self.ui.airboost_bank_a_temp_gauge.setMinValue(-14)
        self.ui.airboost_bank_b_temp_gauge.setMinValue(-14)
        self.ui.freshwater_afterthermo_temp_gauge.setMaxValue(95)
        self.ui.freshwater_beforethermo_temp_gauge.setMaxValue(95)
        self.ui.freshwater_afterthermo_temp_gauge.setMinValue(-6)
        self.ui.freshwater_beforethermo_temp_gauge.setMinValue(-6)
        self.ui.exhuast_bank_a_temp_gauge.setMaxValue(800)
        self.ui.exhuast_bank_b_temp_gauge.setMaxValue(800)
        self.ui.exhuast_bank_a_temp_gauge.setMinValue(-14)
        self.ui.exhuast_bank_b_temp_gauge.setMinValue(-14)
        self.ui.sea_water_temp_gauge.setMaxValue(50)
        self.ui.sea_water_temp_gauge.setMinValue(-3)
        self.ui.oil_temp_gauge.setMaxValue(110)
        self.ui.oil_temp_gauge.setMinValue(0)
        self.ui.oil_ntc_temp_gauge.setMaxValue(110)
        self.ui.oil_ntc_temp_gauge.setMinValue(0)
        self.ui.airboost_pressure_gauge.setMaxValue(4)
        self.ui.airboost_pressure_gauge.setMinValue(0)
        self.ui.sea_water_pressure_gauge.setMaxValue(4)
        self.ui.sea_water_pressure_gauge.setMinValue(0)
        self.ui.fuel_pressure_gauge.setMaxValue(4)
        self.ui.fuel_pressure_gauge.setMinValue(0)
        self.ui.oil_switch_pressure_gauge.setMaxValue(10)
        self.ui.oil_switch_pressure_gauge.setMinValue(0)
        self.ui.oil_pressure_gauge.setMaxValue(10)
        self.ui.oil_pressure_gauge.setMinValue(0)
        # self.ui.oil_press_shaft_gauge.setMaxValue = 5
        # self.ui.oil_pressure_gauge.setMaxValue = 5
        # self.ui.fuel_pressure_gauge.setMaxValue = 5
        # self.ui.airboost_pressure_gauge.setMaxValue = 5
        # self.ui.oil_switch_pressure_gauge.setMaxValue = 5
        # print(i)\
        # time.sleep(1)
        # self.ui.speed_gauge.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
