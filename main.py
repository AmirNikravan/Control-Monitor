from UI_main import Ui_MainWindow
from PySide6.QtWidgets import *
import sys
from arduino import ArduinoHandler
class App(QMainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.arduino = ArduinoHandler('COM4')
        #buttons 
        self.ui.toolButton_speed1.clicked.connect(lambda:self.handle_button_click('s1'))
        self.ui.toolButton_speed2.clicked.connect(lambda:self.handle_button_click('s2'))
        self.ui.toolButton_speed3.clicked.connect(lambda:self.handle_button_click('s3'))
        self.ui.toolButton_speed4.clicked.connect(lambda:self.handle_button_click('s4'))
        self.ui.toolButton_speed5.clicked.connect(lambda:self.handle_button_click('s5'))
        self.ui.toolButton_speed6.clicked.connect(lambda:self.handle_button_click('s6'))
        self.ui.toolButton_speed7.clicked.connect(lambda:self.handle_button_click('s7'))
        self.ui.toolButton_speed8.clicked.connect(lambda:self.handle_button_click('s8'))
        self.ui.toolButton_speed9.clicked.connect(lambda:self.handle_button_click('s9'))
        self.ui.toolButton_speed10.clicked.connect(lambda:self.handle_button_click('s10'))
        self.ui.toolButton_increase.clicked.connect(lambda:self.handle_button_click('in'))
        self.ui.toolButton_decrease.clicked.connect(lambda:self.handle_button_click('de'))
        self.ui.toolButton_start.clicked.connect(lambda:self.handle_button_click('st'))
        self.ui.toolButton_stop.clicked.connect(lambda:self.handle_button_click('sp'))
    def handle_button_click(self, code):
        # Prepare the string to send based on the button index
        self.arduino.send_data(code)

    def closeEvent(self, event):
        # Close the serial port when the application is closed
        self.arduino.close()
        event.accept()

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
        
        
