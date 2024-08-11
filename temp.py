# main.py
from UI_main import Ui_MainWindow
from PySide6.QtWidgets import *
import sys
from arduino import ArduinoHandler
from thread import WorkerGauge, WorkerArduino
from PySide6.QtCore import Signal

class App(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.arduino = ArduinoHandler("COM4", self.ui.speed_gauge)
        self.ui.widget.setMouseTracking(False)
        
        # Connect buttons to their respective handlers
        self.setup_buttons()

        # Initialize the gauges and pages
        self.ui.stackedWidget.setCurrentIndex(0)
        self.design_gauges()

        # Thread to handle the gauge update
        self.worker_gauge = WorkerGauge()
        self.worker_gauge.values.connect(self.update_gauge)
        self.worker_gauge.start()

        # Thread to handle Arduino communication
        self.worker_arduino = WorkerArduino(self.arduino)
        self.worker_arduino.data_received.connect(self.update_arduino_data)
        self.worker_arduino.start()

    def setup_buttons(self):
        self.ui.toolButton_speed1.clicked.connect(lambda: self.handle_button_click("s1"))
        self.ui.toolButton_speed2.clicked.connect(lambda: self.handle_button_click("s2"))
        self.ui.toolButton_speed3.clicked.connect(lambda: self.handle_button_click("s3"))
        self.ui.toolButton_speed4.clicked.connect(lambda: self.handle_button_click("s4"))
        self.ui.toolButton_speed5.clicked.connect(lambda: self.handle_button_click("s5"))
        self.ui.toolButton_speed6.clicked.connect(lambda: self.handle_button_click("s6"))
        self.ui.toolButton_speed7.clicked.connect(lambda: self.handle_button_click("s7"))
        self.ui.toolButton_speed8.clicked.connect(lambda: self.handle_button_click("s8"))
        self.ui.toolButton_speed9.clicked.connect(lambda: self.handle_button_click("s9"))
        self.ui.toolButton_speed10.clicked.connect(lambda: self.handle_button_click("s10"))
        self.ui.toolButton_increase.clicked.connect(lambda: self.handle_button_click("in"))
        self.ui.toolButton_decrease.clicked.connect(lambda: self.handle_button_click("de"))
        self.ui.toolButton_start.clicked.connect(lambda: self.handle_button_click("st"))
        self.ui.toolButton_stop.clicked.connect(lambda: self.handle_button_click("sp"))
        self.ui.toolButton_emgstop.clicked.connect(lambda: self.handle_button_click("mg"))
        self.ui.toolButton_reset.clicked.connect(lambda: self.handle_button_click("re"))
        self.ui.toolButton_testbed.clicked.connect(lambda: self.change_page("testbed"))
        self.ui.toolButton_temperature.clicked.connect(lambda: self.change_page("temperature"))
        self.ui.toolButton_pressure.clicked.connect(lambda:self.change_page("pressure"))

    def update_gauge(self, val):
        self.ui.airboost_bank_a_temp_gauge.value = val[0]
        self.ui.airboost_bank_a_temp_gauge.repaint()

    def update_arduino_data(self, data):
        # Handle incoming data from Arduino
        print(f"Data received from Arduino: {data}")
        # You can update the UI or process the data as needed

    def handle_button_click(self, command):
        # Send commands to Arduino
        self.arduino._send(command)

    def closeEvent(self, event):
        # Stop the threads and close the serial connection
        self.worker_gauge.stop()
        self.worker_gauge.wait()
        self.worker_arduino.stop()
        self.worker_arduino.wait()
        self.arduino.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
