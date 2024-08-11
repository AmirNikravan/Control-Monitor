from PySide6.QtCore import QObject


class DataProcess(QObject):
    def __init__(self, arduino, gauge, ui):
        super().__init__()
        self.arduino_thread = arduino
        self.gauge_thread = gauge
        self.ui = ui
        self.recieved_data = {}
        self.arduino_thread.data_received.connect(self.process)

    def process(self,data):
        self.recieved_data["amir "] = 1
        self.gauge_thread.get_data(self.recieved_data)
        pass

    def closeEvent(self, event):
        # Stop the threads and close the serial connection
        self.gauge_thread.stop()
        self.gauge_thread.wait()
        self.arduino_thread.stop()
        self.arduino_thread.wait()
        self.arduino.close()
        event.accept()
