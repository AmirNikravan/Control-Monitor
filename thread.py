from PySide6.QtCore import QThread, Signal
import random
import time


class WorkerData(QThread):
    values = Signal(int)

    def __init__(self,ui):
        super().__init__()
        self.val = []
        self.ui = ui
        self.running = True
        self.data = None  # متغیر برای ذخیره داده‌های دریافتی

    def run(self):
        try:
            while self.running:
                if self.data:
                    self.ui.airboost_bank_a_temp_gauge.value = self.data
                    self.ui.exhuast_bank_b_temp_gauge.value = self.data + 123
                    self.ui.exhuast_bank_a_temp_gauge.value = self.data - 99
                    self.ui.oil_ntc_temp_gauge.value = self.data + 96
                    self.ui.oil_temp_gauge.value = self.data *2 -444
                    self.ui.airboost_bank_b_temp_gauge.value = self.data
                    self.ui.airboost_bank_b_temp_gauge.valaue = self.data +300
                    self.ui.sea_water_temp_gauge.value = self.data -240
                    self.ui.freshwater_beforethermo_temp_gauge.value = self.data +222
                    self.ui.freshwater_afterthermo_temp_gauge.value = self.data -222
                    self.ui.freshwater_afterthermo_temp_gauge.repaint()
                    self.ui.freshwater_beforethermo_temp_gauge.repaint()
                    self.ui.sea_water_temp_gauge.repaint()
                    self.ui.airboost_bank_b_temp_gauge.repaint()
                    self.ui.oil_temp_gauge.repaint()
                    self.ui.oil_ntc_temp_gauge.repaint()
                    self.ui.exhuast_bank_a_temp_gauge.repaint()
                    self.ui.exhuast_bank_b_temp_gauge.repaint()
                    self.ui.airboost_bank_a_temp_gauge.repaint()
                    time.sleep(1)
        except Exception as e:
            print(f"error{e}")
    def stop(self):
        self.running = False
        
        
class WorkerArduino(QThread):
    data_received = Signal(int)

    def __init__(self, arduino_handler):
        super().__init__()
        self.running = True
        self.arduino_handler = arduino_handler

    def run(self):
        # print(3234234)
        while self.running:
            try:
                # Print()
                print(self.arduino_handler.serial_port.in_waiting)
                if self.arduino_handler.serial_port.in_waiting > 0:
                    data = self.arduino_handler.serial_port.readline().decode().strip()
                    print(f"data = {data}" )
                else:
                    self.arduino_handler._send('3')
                    time.sleep(0.8)
                self.data_received.emit(data)
                
            except Exception as e:
                # print(f"Error reading from Arduino: {e}")
                pass
            # time.sleep(0.5)

    def stop(self):
        self.running = False
