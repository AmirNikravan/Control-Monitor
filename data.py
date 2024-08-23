from PySide6.QtCore import QThread,QObject,Signal
import time
import random
class DataProcess(QThread):
    data_gauge = Signal(int)
    
    def __init__(self):
        super().__init__()
        self.data = None
        self.running = True
    def get_data(self, data):
        self.data = data
    
    def run(self):
        while self.running:
            if self.data is not None:
                print
                self.data_gauge.emit(self.data)
                self.data = None
            time.sleep(1)
    def stop(self):
        self.running = False