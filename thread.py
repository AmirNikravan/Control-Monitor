from PySide6.QtCore import QThread, Signal
import random
import time


class WorkerGauge(QThread):
    values = Signal(list)

    def __init__(self,ui):
        super().__init__()
        self.val = []
        self.running = True
        self.data = None  # متغیر برای ذخیره داده‌های دریافتی

    def run(self):
        while self.running:
            # بررسی و استفاده از داده‌های ذخیره شده
            if self.data is not None:
                print(f"Processing data: {self.data}")
                # پردازش داده‌ها و به‌روزرسانی مقادیر
                # برای مثال، به‌روزرسانی مقادیر شاخص‌ها
                self.val = [int(self.data)]  # تبدیل داده به لیست برای مثال
                self.values.emit(self.val)
                self.data = None  # بعد از پردازش داده، آن را پاک کنید
            else:
                # داده‌ای برای پردازش وجود ندارد
                print("No data to process.")
            time.sleep(1)

    def handle_data_received(self, data):
        # دریافت داده‌ها از WorkerArduino و ذخیره آن
        print(f"Data received: {data}")
        self.data = data  # ذخیره داده برای پردازش در تابع run

    def stop(self):
        self.running = False
class WorkerArduino(QThread):
    data_received = Signal(int)

    def __init__(self, arduino_handler):
        super().__init__()
        self.running = True
        self.arduino_handler = arduino_handler

    def run(self):
        while self.running:
            try:
                # if self.arduino_handler.serial_port.in_waiting > 0:
                #     data = self.arduino_handler.serial_port.readline().decode().strip()
                self.data_received.emit(random.randint(0,1000))
            except Exception as e:
                # print(f"Error reading from Arduino: {e}")
                pass
            time.sleep(0.1)

    def stop(self):
        self.running = False
