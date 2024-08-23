from PySide6.QtCore import QThread, Signal , QTimer
import random
import time
import json
from PySide6.QtWidgets import QApplication

class WorkerData(QThread):
    values = Signal(int)

    def __init__(self, ui):
        super().__init__()
        self.val = []
        self.ui = ui
        self.running = True
        self.data = None  # متغیر برای ذخیره داده‌های دریافتی

    def get_data(self, data):
        self.data = data
        print("here")

    def run(self):
        try:
            # i = 1
            # print('moooz')
            while self.running:
                # print(self.data)
                if self.data:
                    # print(f"dataaaaaaaa {self.data['t']}")
                    self.temp_gauges(self.data["t"])
                    # print(self.data["l"])
                    self.lamps(self.data["l"])
                    self.keys(self.data['k'])
                    # self.pressure_gauges(self.data['p'])
                    # pass

                time.sleep(0.8)
        except Exception as e:
            print(f"error{e}")
    def keys(self,val):
        print(val)
        self.ui.stop_key.setEnabled(not val['k1'])
        self.ui.start_key.setEnabled(not val['k2'])
        self.ui.increase_key.setEnabled(not val['k3'])
        self.ui.decrease_key.setEnabled(not val['k4'])
        self.ui.emgstop_key.setEnabled(not val['k5'])
        
    def lamps(self, val):
        """
        lamps numbers:
        l1 = stop
        l2 = start
        l3 = inc
        l4 = dec
        l5 = emg
        """
        print(f"value lamp = {val['l1']}")
        # check lamp status:

        if val["l1"] == True:  # stop
            # self.ui.lamp_stop.setStyleSheet("")
            self.ui.lamp_stop.setStyleSheet(
                """ 
            QLabel {
	            background-color: green;
                border-style: outset;
                border-width: 1px;
                border-radius: 30px;
                }
                """
            )
            # self.ui.lamp_stop.repaint()
            # QApplication.processEvents()
        else:
            self.ui.lamp_stop.setStyleSheet(
                """ 
            QLabel {
	            background-color: red;
                border-style: outset;
                border-width: 1px;
                border-radius: 30px;
                }
                """
            )
            # self.ui.lamp_stop.repaint()
            # QApplication.processEvents()
        if val["l2"] == True:  # start
            self.ui.lamp_start.setStyleSheet(
                """ 
            QLabel {
	            background-color: green;
                border-style: outset;
                border-width: 1px;
                border-radius: 30px;
                }
                """
            )
            # self.ui.lamp_start.repaint()
        else:
            self.ui.lamp_start.setStyleSheet(
                """ 
            QLabel {
	            background-color: red;
                border-style: outset;
                border-width: 1px;
                border-radius: 30px;
                }
                """
            )
            # self.ui.lamp_start.repaint()
        if val["l3"] == True:  # inc
            self.ui.lamp_increase.setStyleSheet(
                """ 
            QLabel {
	            background-color: green;
                border-style: outset;
                border-width: 1px;
                border-radius: 30px;
                }
                """
            )
        else:
            self.ui.lamp_increase.setStyleSheet(
                """ 
            QLabel {
	            background-color: red;
                border-style: outset;
                border-width: 1px;
                border-radius: 30px;
                }
                """
            )
        if val["l4"] == True:  # dec
            self.ui.lamp_decrease.setStyleSheet(
                """ 
            QLabel {
	            background-color: green;
                border-style: outset;
                border-width: 1px;
                border-radius: 30px;
                }
                """
            )
        else:
            self.ui.lamp_decrease.setStyleSheet(
                """ 
            QLabel {
	            background-color: red;
                border-style: outset;
                border-width: 1px;
                border-radius: 30px;
                }
                """
            )
        if val["l5"] == True:  # emg
            self.ui.lamp_emgstop.setStyleSheet(
                """ 
            QLabel {
	            background-color: green;
                border-style: outset;
                border-width: 1px;
                border-radius: 30px;
                }
                """
            )
        else:
            self.ui.lamp_emgstop.setStyleSheet(
                """ 
            QLabel {
	            background-color: red;
                border-style: outset;
                border-width: 1px;
                border-radius: 30px;
                }
                """
            )
        # time.sleep(0.5)
    def temp_gauges(self, val):
        # print(val)
        if val is not None:
            # print('i am here mother fucker bitch')
            self.ui.airboost_bank_a_temp_gauge.value = val["t1"]
            # self.ui.exhuast_bank_b_temp_gauge.value =  random.randint(0,300)
            # self.ui.exhuast_bank_a_temp_gauge.value = random.randint(0,300)
            # self.ui.oil_ntc_temp_gauge.value = random.randint(0,300)
            # self.ui.oil_temp_gauge.value = random.randint(0,300)
            self.ui.airboost_bank_b_temp_gauge.value = val["t2"]
            # self.ui.airboost_bank_b_temp_gauge.valaue = random.randint(0,300)
            self.ui.sea_water_temp_gauge.value = random.randint(0, 300)
            self.ui.freshwater_beforethermo_temp_gauge.value = random.randint(0, 300)
            self.ui.freshwater_afterthermo_temp_gauge.value = random.randint(0, 300)
            # self.ui.freshwater_afterthermo_temp_gauge.repaint()
            # self.ui.freshwater_beforethermo_temp_gauge.repaint()
            # self.ui.sea_water_temp_gauge.repaint()
            self.ui.airboost_bank_b_temp_gauge.repaint()
            # self.ui.oil_temp_gauge.repaint()
            # self.ui.oil_ntc_temp_gauge.repaint()
            # self.ui.exhuast_bank_a_temp_gauge.repaint()
            # self.ui.exhuast_bank_b_temp_gauge.repaint()
            self.ui.airboost_bank_a_temp_gauge.repaint()
            time.sleep(0.3)

    def stop(self):
        self.running = False


class WorkerArduino(QThread):
    data_received = Signal(dict)

    def __init__(self, arduino_handler):
        super().__init__()
        self.running = True
        self.arduino_handler = arduino_handler

    def run(self):
        # print(3234234)
        data = {}
        while self.running:
            try:
                # Print()

                print(f"in yeki {self.arduino_handler.serial_port.in_waiting}")
                if self.arduino_handler.serial_port.in_waiting > 0:
                    raw_data = (
                        self.arduino_handler.serial_port.readline().decode().strip()
                    )
                    data = json.loads(raw_data)
                    # d = data["k"]
                    # print(f"data = {d }" )
                    # print(f"data = {data}" )
                else:
                    self.arduino_handler._send("3")

                # print(data)
                self.data_received.emit(data)
                time.sleep(0.8)

            except Exception as e:
                # print(f"Error reading from Arduino: {e}")
                pass
            # time.sleep(0.5)

    def stop(self):
        self.running = False
