from UI_main import Ui_MainWindow
from PySide6.QtWidgets import *
import sys
class App(QMainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #buttons 
        
    def handle_button_click(self, button_index):
        # Prepare the string to send based on the button index
        data_to_send = ''
        
        self.arduino.send_data(data_to_send)

    def closeEvent(self, event):
        # Close the serial port when the application is closed
        self.arduino.close()
        event.accept()

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
        
        
