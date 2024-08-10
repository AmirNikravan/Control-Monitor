from PySide6.QtCore import QThread, Signal
import random
import time


class WorkerGauge(QThread):
    values = Signal(list)

    def __init__(self):
        super().__init__()
        self.val = []
        self.running = True  # To control the loop

    def run(self):
        while self.running:  # Infinite loop for generating random numbers
            self.val.clear()
            for _ in range(10):
                self.val.append(random.randint(0, 1000))
            print(self.val[0])
            self.values.emit(self.val)
            time.sleep(1)  # Delay for 1 second

    def stop(self):
        self.running = False  # Stop the loop when needed


class WorkerArduino(QThread):
    data_recieved = Signal(str)

    def __init__(self, arduino_handler):
        super().__init__()
        self.running = True
        self.arduino_handler = arduino_handler

    def run(self):
        while self.running:
            try:
                if self.arduino_handler.serial_port.in_waiting > 0:
                    data = self.arduino_handler.serial_port.readline().decode().strip()
                    self.data_received.emit(data)
            except Exception as e:
                print(f"Error reading from Arduino: {e}")
            time.sleep(0.1)

    def stop(self):
        self.running = False
