from PySide6.QtCore import QThread, Signal , QTimer
import random
import time , json
import serial
import datetime
from PySide6.QtWidgets import QApplication ,QTableWidgetItem
class UpdateWorker(QThread):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.data = None
    def update_values(self, data):
        """Receive JSON data and update internal state for gauges."""
        try:
            if not data:
                return
            self.data = data

        except Exception as e:
            print(e)    
    def run(self):
        while True:
            if self.data: 
                data_json = json.loads(self.data)
                self.temperature = data_json['t']
                self.pressure = data_json['p']
                self.keys = data_json['k']
                self.lamps = data_json['l']
                self.update_gauges()
                # print(self.data)
                # time.sleep(0.3)
            time.sleep(1)  # Update every 1 second   
    def update_gauges(self):
        self.ui.airboost_bank_a_temp_gauge.setValue(self.temperature['t1'])
        self.ui.airboost_bank_b_temp_gauge.setValue(self.temperature['t2'])
        self.ui.freshwater_beforethermo_temp_gauge.setValue(self.temperature['t3'])
        self.ui.freshwater_afterthermo_temp_gauge.setValue(self.temperature['t4'])
        self.ui.exhuast_bank_b_temp_gauge.setValue(self.temperature['t5'])
        self.ui.exhuast_bank_a_temp_gauge.setValue(self.temperature['t6'])
        self.ui.sea_water_temp_gauge.setValue(self.temperature['t7'])
        self.ui.oil_temp_gauge.setValue(self.temperature['t8'])
        self.ui.oil_ntc_temp_gauge.setValue(self.temperature['t9'])
        self.ui.airboost_pressure_gauge.setValue(self.pressure['p1'])
        self.ui.sea_water_pressure_gauge.setValue(self.pressure['p2'])
        self.ui.fuel_pressure_gauge.setValue(self.pressure['p3'])
        self.ui.oil_pressure_gauge.setValue(self.pressure['p4'])
        self.ui.oil_switch_pressure_gauge.setValue(self.pressure['p5'])
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
    data_received = Signal(str)

    def __init__(self,ui, port, baud_rate=115200):
        super().__init__()
        self.ui = ui
        self.port = port
        self.baud_rate = baud_rate
        self.running = True
        self.serial_port = None
        self.time_check = time.time()
        self.establish_connection()
        # self.serial_port.write('3'.encode('utf-8'))

    def establish_connection(self):
        try:
            self.serial_port = serial.Serial(self.port, self.baud_rate)
            time.sleep(1)
            print(f"Connected to Arduino on {self.port}")
        except serial.SerialException as e:
            print(f"Error connecting to Arduino: {e}")

    def run(self):
        while self.running:
            try:
                if self.serial_port:
                    if self.serial_port.in_waiting > 0:  # Check if there is data available
                        data = self.serial_port.readline().decode('utf-8').strip()
                        # self.data_received.emit(data)
                        data_json = json.loads(data)
                        print(data_json)
                        self.temperature = data_json['t']
                        # self.pressure = data_json['p']
                        # self.keys = data_json['k']
                        # self.lamps = data_json['l']
                        # self.update_current_page_gauges()
                        # self.update_table()
                    else:
                        self.send_command('3')  # Send '3' if no data is available
                time.sleep(0.1)
            except Exception as e:
                print(f"Error reading from Arduino: {e}")

    def send_command(self, command):
        if self.serial_port:
            self.serial_port.write(command.encode('utf-8'))
            # print(f"Sent: {command}")
    def update_table(self):
        print(1)
        if self.ui.stackedWidget.currentIndex() == 2:
            print(2)
            self.ui.tableWidget_data.setRowCount(14) 
            self.ui.tableWidget_data.setColumnCount(5)
            try:
                for i in range(0,10):
                    self.ui.tableWidget_data.setItem(i,1,QTableWidgetItem(self.temperature[f't{i}']))
                for i in range(10,15):
                    self.ui.tableWidget_data.setItem(i,1,QTableWidgetItem(self.temperature[f't{i-9}']))
                # self.ui.tableWidget_data.repaint()
            except Exception as e:
                print(f'{e}')
            
        # except Exception as e:
        #     print(e)
    def update_gauges_page_0(self):
        print('page0')
        self.ui.airboost_bank_a_temp_gauge.updateValue(self.temperature['t1'])
        # self.ui.airboost_bank_a_temp_gauge.setEnabled(False)
        self.ui.exhuast_bank_b_temp_gauge.updateValue(self.temperature['t2'])
        self.ui.exhuast_bank_a_temp_gauge.updateValue(self.temperature['t3'])

    def update_gauges_page_1(self):
        print('page1')
        self.ui.airboost_bank_b_temp_gauge.updateValue(self.temperature['t4'])
        self.ui.oil_temp_gauge.updateValue(self.temperature['t5'])
        self.ui.oil_ntc_temp_gauge.updateValue(self.temperature['t6'])
    def update_gauges_page_2(self):
        print('pag2')
        self.ui.sea_water_temp_gauge.updateValue(self.temperature['t7'])
        self.ui.freshwater_beforethermo_temp_gauge.updateValue(self.temperature['t8'])
        self.ui.freshwater_afterthermo_temp_gauge.updateValue(self.temperature['t9'])
    def update_gauges_page_3(self):
        # print(self.time_check)
        
        duration = time.time()-self.time_check
        # print(duration)
        minutes = int(duration // 60)
        seconds = duration % 60
        print(f'page 3 {minutes}: {seconds}')
        self.ui.oil_pressure_gauge.updateValue(self.pressure['p1'])
        self.ui.oil_switch_pressure_gauge.updateValue(self.pressure['p2'])
        self.ui.airboost_pressure_gauge.updateValue(self.pressure['p3'])
    def update_gauges_page_4(self):
        print('page4')
        self.ui.sea_water_pressure_gauge.updateValue(self.pressure['p4'])
        self.ui.fuel_pressure_gauge.updateValue(self.pressure['p5'])
    # Add more methods for other pages...

    def update_current_page_gauges(self):
        current_page = self.ui.stackedWidget_sensosr.currentIndex()
        if current_page == 0:
            self.update_gauges_page_0()
        elif current_page == 1:
            self.update_gauges_page_1()
        elif current_page == 2 :
            self.update_gauges_page_2()
        elif current_page == 3 :
            self.update_gauges_page_3()
        elif current_page == 4 :
            self.update_gauges_page_4()