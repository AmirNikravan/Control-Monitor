from PySide6.QtCore import QThread, Signal
import random
import time


class WorkerGauge(QThread):
    values = Signal(int)

    def __init__(self):
        super().__init__()
        self.val = []
        self.running = True
        self.data = None  # متغیر برای ذخیره داده‌های دریافتی

    def run(self):
        while self.running:
            for i in range (25):
                self.values.emit(i)
                QThread.sleep(1.5)
    def stop(self):
        self.running = False
        
        
class WorkerArduino(QThread):
    data_received = Signal(int)

    def __init__(self, ):
        super().__init__()
        self.running = True
        # self.arduino_handler = arduino_handler

    def run(self):
        while self.running:
            try:
                # if self.arduino_handler.serial_port.in_waiting > 0:
                #     data = self.arduino_handler.serial_port.readline().decode().strip()
                self.data_received.emit(random.randint(0,1000))
            except Exception as e:
                # print(f"Error reading from Arduino: {e}")
                pass
            time.sleep(0.5)

    def stop(self):
        self.running = False
