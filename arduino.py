import serial
from PySide6.QtWidgets import *
import threading


class ArduinoHandler:
    def __init__(self, port, baud_rate=9600):
        self.port = port
        self.baud_rate = baud_rate
        self.serial_port = None
        self.connect()

    def connect(self):
        try:
            self.serial_port = serial.Serial(self.port, self.baud_rate)
            QMessageBox.warning(
                self, "هشدار", f"برنامه توسط پورت {self.serial_port} به آردوینو متصل شد"
            )
        except serial.SerialException as e:
            QMessageBox.warning(self, "error", f"Error connecting to Arduino: {e}")

    def send_data(self, data):
        if self.serial_port and self.serial_port.is_open:
            thread = threading.Thread(target=self._send, args=(data,))
            thread.start()
        else:
            print("Serial port is not open")

    def _send(self, data):
        try:
            self.serial_port.write(data.encode())
            print(f"Sent: {data.strip()}")
        except Exception as e:
            print(f"Error sending data: {e}")

    def close(self):
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
            print("Serial port closed")
