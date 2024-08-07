import serial
from PySide6.QtWidgets import *
from PySide6.QtCore import QObject, Signal
import threading

class ArduinoHandler(QObject):
    data_received = Signal(str)

    def __init__(self, port,list, baud_rate=115200):
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
            # Start the thread to read data
            threading.Thread(target=self.read_data, daemon=True).start()
        except serial.SerialException as e:
            # self.list.addItem(f"Error connecting to Arduino: {e}")
            print(f"Error connecting to Arduino: {e}")

    def send_data(self, data):
        if self.serial_port and self.serial_port.is_open:
            thread = threading.Thread(target=self._send, args=(data,))
            thread.start()
        else:
            # self.list.addItem("Serial port is not open")
            print("Serial port is not open")

    def _send(self, data):
        try:
            self.serial_port.write(data.encode())
            # self.list.addItem(f"Sent: {data.strip()}")
            print(f"Sent: {data.strip()}")
        except Exception as e:
            # self.list.addItem(f"Error sending data: {e}")
            print(f"Error sending data: {e}")

    def close(self):
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
            # self.list.addItem("Serial port closed")
            print("Serial port closed")

    def read_data(self):
        while True:
            if self.serial_port and self.serial_port.is_open:
                try:
                    # Read incoming data from Arduino
                    line = self.serial_port.readline()
                    # Attempt to decode the line, ignoring errors
                    line = line.decode('utf-8', errors='ignore').strip()
                    if line:
                        self.data_received.emit(line)  # Emit the received data
                except Exception as e:
                    # self.list.addItem(f"Error reading data: {e}")
                    print(f"Error reading data: {e}")
                    break
