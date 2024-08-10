# main.py
from UI_main import Ui_MainWindow
from PySide6.QtWidgets import *
import sys
from arduino import ArduinoHandler
from PySide6.QtCore import Signal
import time
from thread import *

class App(QMainWindow):
    update_ui_signal = Signal(float)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.arduino = ArduinoHandler("COM4", self.ui.speed_gauge)
        self.ui.widget.setMouseTracking(False)
        # Buttons
        self.ui.toolButton_speed1.clicked.connect(
            lambda: self.handle_button_click("s1")
        )
        self.ui.toolButton_speed2.clicked.connect(
            lambda: self.handle_button_click("s2")
        )
        self.ui.toolButton_speed3.clicked.connect(
            lambda: self.handle_button_click("s3")
        )
        self.ui.toolButton_speed4.clicked.connect(
            lambda: self.handle_button_click("s4")
        )
        self.ui.toolButton_speed5.clicked.connect(
            lambda: self.handle_button_click("s5")
        )
        self.ui.toolButton_speed6.clicked.connect(
            lambda: self.handle_button_click("s6")
        )
        self.ui.toolButton_speed7.clicked.connect(
            lambda: self.handle_button_click("s7")
        )
        self.ui.toolButton_speed8.clicked.connect(
            lambda: self.handle_button_click("s8")
        )
        self.ui.toolButton_speed9.clicked.connect(
            lambda: self.handle_button_click("s9")
        )
        self.ui.toolButton_speed10.clicked.connect(
            lambda: self.handle_button_click("s10")
        )
        self.ui.toolButton_increase.clicked.connect(
            lambda: self.handle_button_click("in")
        )
        self.ui.toolButton_decrease.clicked.connect(
            lambda: self.handle_button_click("de")
        )
        self.ui.toolButton_start.clicked.connect(lambda: self.handle_button_click("st"))
        self.ui.toolButton_stop.clicked.connect(lambda: self.handle_button_click("sp"))
        self.ui.toolButton_emgstop.clicked.connect(
            lambda: self.handle_button_click("mg")
        )
        self.ui.toolButton_reset.clicked.connect(lambda: self.handle_button_click("re"))
        #change page
        self.ui.toolButton_testbed.clicked.connect(lambda: self.change_page("testbed"))
        self.ui.toolButton_temperature.clicked.connect(
            lambda: self.change_page("temperature")
        )
        self.ui.toolButton_pressure.clicked.connect(lambda:self.change_page("pressure"))
        # design
        self.ui.stackedWidget.setCurrentIndex(0)
        self.design_gauges()
        # Connect the signal to the slot
        self.arduino.data_received.connect(self.update_data_label)
        #thread
        self.worker = Worker()
        self.start()
        self.worker.values.connect(self.update)
    def update(self,val):
        self.ui.airboost_bank_a_temp_gauge.value = val[0]
        self.ui.airboost_bank_a_temp_gauge.repaint()
    def start(self):
        self.worker.start()
    def closeEvent(self,event):
        self.worker.stop()
        self.worker.wait()
        event.accept()
    def change_page(self, page):

        if page == "testbed":
            self.ui.stackedWidget.setCurrentIndex(0)
        elif page == "temperature":
            self.ui.stackedWidget.setCurrentIndex(1)
        elif page == "pressure":
            self.ui.stackedWidget.setCurrentIndex(2)
    def handle_button_click(self, code):
        if code == "st":
            self.ui.label_2.setText("روشن")
        if code == "sp" or code == "mg":
            self.ui.label_2.setText("خاموش")
        # Prepare the string to send based on the button index
        self.arduino.send_data(code)

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

    def closeEvent(self, event):
        # Close the serial port when the application is closed
        self.arduino.close()
        event.accept()

    def design_gauges(self):

        self.ui.speed_gauge.setGaugeTheme(6)
        self.ui.speed_gauge.setMinValue(0)
        self.ui.speed_gauge.setMaxValue(255)
        self.ui.speed_gauge.setMouseTracking(False)
        self.ui.speed_gauge.units = "RPM"
        self.ui.rpm_gauge.setGaugeTheme(6)
        self.ui.rpm_gauge.setMouseTracking(False)
        self.ui.rpm_gauge.units = "RPM"
        # print(i)\
        # time.sleep(1)
        # self.ui.speed_gauge.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
