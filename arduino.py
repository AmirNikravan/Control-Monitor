import serial
from PySide6.QtWidgets import *
from PySide6.QtCore import QObject, Signal
import threading

class ArduinoHandler(QObject):
    def __init__(self, port, baud_rate=115200):
        super().__init__()
        self.port = port
        self.list = list
        self.baud_rate = baud_rate
        self.serial_port = None
        self.establish_connection()

    def establish_connection(self):
        try:
            self.serial_port = serial.Serial(self.port, self.baud_rate)
            # self.list.addItem(f"Connected to Arduino on {self.port}")
            print(f"Connected to Arduino on {self.port}")
        except serial.SerialException as e:
            # self.list.addItem(f"Error connecting to Arduino: {e}")
            print(f"Error connecting to Arduino: {e}")

    # def _send(self, data):
    #     try:
    #         if data == None:
    #             data = '3'
    #             self.serial_port.write(data)
    #             print('injam')
    #             print(f"Sent: {data}")
    #         else:
    #             self.serial_port.write(data.encode())
    #         # self.list.addItem(f"Sent: {data.strip()}")
    #             print(f"Sent: {data.strip()}")
    #     except Exception as e:
    #         # self.list.addItem(f"Error sending data: {e}")
    #         print(f"Error sending data: {e}")

    # def close(self):
    #     if self.serial_port and self.serial_port.is_open:
    #         self.serial_port.close()
    #         # self.list.addItem("Serial port closed")
    #         print("Serial port closed")
