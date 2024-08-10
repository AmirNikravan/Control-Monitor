from PySide6.QtCore import QThread, Signal
import random
import time

class Worker(QThread):
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
