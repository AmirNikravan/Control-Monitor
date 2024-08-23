from PySide6.QtCore import QThread, Signal
import random
import time
import json


class WorkerData(QThread):
    values = Signal(int)

    def __init__(self,ui):
        super().__init__()
        self.val = []
        self.ui = ui
        self.running = True
        self.data = None  # متغیر برای ذخیره داده‌های دریافتی
    def get_data(self,data):
        self.data = data
        print('here')
    def run(self):
        try:
            # print('moooz')
            while self.running:
                # print(self.data)
                if self.data:
                    # print(f"dataaaaaaaa {self.data['t']}")
                    self.temp_gauges(self.data['t'])
                    print(self.data['l'])
                    # self.pressure_gauges(self.data['p'])
                    pass

                time.sleep(0.8)
        except Exception as e:
            print(f"error{e}")
    def keys(self,val):
        """
        lamps numbers:
        l1 = stop
        l2 = start
        l3 = inc
        l4 = dec       
        l5 = emg
        """
        #check lamp status:
        
        pass
    def temp_gauges(self,val):
        # print(val)
        if val is not None:
            # print('i am here mother fucker bitch')
            self.ui.airboost_bank_a_temp_gauge.value = val['t1']
            # self.ui.exhuast_bank_b_temp_gauge.value =  random.randint(0,300)
            # self.ui.exhuast_bank_a_temp_gauge.value = random.randint(0,300)
            # self.ui.oil_ntc_temp_gauge.value = random.randint(0,300)
            # self.ui.oil_temp_gauge.value = random.randint(0,300)
            self.ui.airboost_bank_b_temp_gauge.value = val['t2']
            # self.ui.airboost_bank_b_temp_gauge.valaue = random.randint(0,300)
            self.ui.sea_water_temp_gauge.value = random.randint(0,300)
            self.ui.freshwater_beforethermo_temp_gauge.value = random.randint(0,300)
            self.ui.freshwater_afterthermo_temp_gauge.value = random.randint(0,300)
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
                    raw_data = self.arduino_handler.serial_port.readline().decode().strip()
                    data = json.loads(raw_data)
                    # d = data["k"]
                    # print(f"data = {d }" )
                    # print(f"data = {data}" )
                else:
                    self.arduino_handler._send('3')
                  
                # print(data)
                self.data_received.emit(data)
                time.sleep(0.8) 
                
            except Exception as e:
                # print(f"Error reading from Arduino: {e}")
                pass
            # time.sleep(0.5)

    def stop(self):
        self.running = False
