# main.py
from UI_main import Ui_MainWindow
from PySide6.QtWidgets import *
import sys
from arduino import ArduinoHandler
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
        self.arduino = ArduinoHandler('/dev/ttyACM0',)

        # print(self.ui.right_menu.children())
        self.ui.increase_key.clicked.connect(
            lambda: self.handle_button_click("6")
        )
        self.ui.decrease_key.clicked.connect(
            lambda: self.handle_button_click("7")
        )
        self.ui.start_key.clicked.connect(lambda: self.handle_button_click("4")) # start
        self.ui.stop_key.clicked.connect(lambda: self.handle_button_click("5"))
        self.ui.emgstop_key.clicked.connect(
            lambda: self.handle_button_click("8")
        )
        # change page
        self.ui.toolButton_shaft.clicked.connect(lambda: self.change_page("shaft"))
        self.ui.toolButton_temperature.clicked.connect(
            lambda: self.change_page("temperature")
        )
        self.ui.toolButton_pressure.clicked.connect(
            lambda: self.change_page("pressure")
        )
        self.ui.toolButton_keys.clicked.connect(lambda: self.change_page("keys"))
        # design
        self.ui.stackedWidget.setCurrentIndex(0)
        self.design_gauges()

        self.worker_arduino = WorkerArduino(self.arduino)
        self.worker_data = WorkerData(self.ui)        
        self.worker_arduino.start()
        self.worker_arduino.data_received.connect(self.worker_data.get_data)
        
        self.worker_data.start()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)  # Connect timeout to the update function
        self.timer.start(1000)  # 1000 ms = 1 second

        # Call update_time once at startup to set the initial time
        self.update_time()

    def update_time(self):
        # Update the label with the current time
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        self.ui.label_time.setText(current_time)

    def update_gauge(self, val):
        pass
        # self.ui.speed_gauge.value = val
        # # self.ui.airboost_bank_a_temp_gauge.neede
        # self.ui.speed_gauge.setGaugeTheme(val)
        # self.ui.speed_gauge.repaint()


    def change_page(self, page):

        if page == "shaft":
            self.ui.stackedWidget.setCurrentIndex(0)
            
        elif page == "temperature":
            self.ui.stackedWidget.setCurrentIndex(1)
        elif page == "pressure":
            self.ui.stackedWidget.setCurrentIndex(2)
        elif page == "keys":
            self.arduino._send('3')
            self.ui.stackedWidget.setCurrentIndex(3)

    def handle_button_click(self, command):
        # Send commands to Arduino
        self.arduino._send(command)

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
        self.ui.airboost_bank_a_temp_gauge.setGaugeTheme(3)
        self.ui.airboost_bank_b_temp_gauge.setGaugeTheme(3)
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
        # self.ui.speed_gauge.setGaugeTheme(6)
        # self.ui.speed_gauge.setMinValue(0)
        # self.ui.speed_gauge.setMaxValue(255)
        # self.ui.speed_gauge.setMouseTracking(False)
        # self.ui.speed_gauge.units = "RPM"
        # self.ui.rpm_gauge.setGaugeTheme(6)
        # self.ui.rpm_gauge.setMouseTracking(False)
        # self.ui.rpm_gauge.units = "RPM"
        self.ui.airboost_bank_a_temp_gauge.setMouseTracking(False)
        self.ui.exhuast_bank_b_temp_gauge.setMouseTracking(False)
        self.ui.exhuast_bank_a_temp_gauge.setMouseTracking(False)
        self.ui.oil_ntc_temp_gauge.setMouseTracking(False)
        self.ui.oil_temp_gauge.setMouseTracking(False)
        self.ui.airboost_bank_b_temp_gauge.setMouseTracking(False)
        self.ui.sea_water_temp_gauge.setMouseTracking(False)
        self.ui.freshwater_beforethermo_temp_gauge.setMouseTracking(False)
        self.ui.freshwater_afterthermo_temp_gauge.setMouseTracking(False)
        
        # print(i)\
        # time.sleep(1)
        # self.ui.speed_gauge.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
