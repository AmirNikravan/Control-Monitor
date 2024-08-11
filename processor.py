from PySide6.QtCore import QThread
import time
import random


class Gauge(QThread):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.data = None
        self.running = True

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

    def process_data(self, data):
        # داده‌های دریافتی از DataProcessor را پردازش کنید
        print(f"Processing pressure data: {data}")
        self.data = data
